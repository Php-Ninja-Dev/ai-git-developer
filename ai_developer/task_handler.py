import time

class TaskHandler:
    def __init__(self, client, sandbox, assistant, console):
        self.client = client
        self.sandbox = sandbox
        self.console = console
        self.assistant = assistant

    def handle_new_task(self, user_task, repo_url):
        thread_id = self.create_thread(user_task, repo_url)
        run_id = self.create_run(thread_id)
        self.process_run(thread_id, run_id)

    def create_thread(self, user_task, repo_url):
        thread = self.client.beta.threads.create(
            messages=[{
                "role": "user",
                "content": f"Carefully plan this task and start working on it: {user_task} in the {repo_url} repo."
            }],
        )
        return thread.id

    def create_run(self, thread_id):
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id, assistant_id=self.assistant.id
        )
        return run.id

    def process_run(self, thread_id, run_id):
        spinner = ""
        with self.console.status(spinner):
            self.monitor_run(thread_id, run_id)

    def monitor_run(self, thread_id, run_id):
        previous_status = None
        run = self.retrieve_run(thread_id, run_id)

        while True:
            if self.has_status_changed(run, previous_status):
                self.display_status(run)

            if run.status == "requires_action":
                self.handle_action_required(thread_id, run)
            elif run.status == "completed":
                self.handle_completion(thread_id)
                break
            elif run.status in ["cancelled", "cancelling", "expired", "failed"]:
                break
            elif run.status in ["queued", "in_progress"]:
                pass
            else:
                print(f"Unknown status: {run.status}")
                break

            run = self.retrieve_run(thread_id, run_id)

    def has_status_changed(self, run, previous_status):
        if run.status != previous_status:
            return True
        return False

    def display_status(self, run):
        self.console.print(
            f"[bold #FF8800]>[/bold #FF8800] Assistant is currently in status: {run.status} [#666666](waiting for OpenAI)[/#666666]")
        return run.status

    def handle_action_required(self, thread_id, run):
        outputs = self.sandbox.openai.actions.run(run)
        if len(outputs) > 0:
            self.client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id, run_id=run.id, tool_outputs=outputs)

    def handle_completion(self, thread_id):
        self.console.print("\n✅[#666666] Run completed[/#666666]")
        messages = self.client.beta.threads.messages.list(thread_id=thread_id).data[0].content
        text_messages = [message for message in messages if message.type == "text"]
        self.console.print("Thread finished:", text_messages[0].text.value)

    def retrieve_run(self, thread_id, run_id):
        run = self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        time.sleep(0.1)
        return run
