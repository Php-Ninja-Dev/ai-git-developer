

def send_email(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    recipients = args["recipients"]
    subject = args["subject"]
    body = args["body"]
    print_sandbox_action("Sending email to", ', '.join(recipients))

    try:
        # Add here the code to send an email using a preferred library or service
        print_sandbox_action("Email sent", f'Subject: {subject}')
        return "success"
    except Exception as e:
        return f"Error: {e}"
