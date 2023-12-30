from typing import Callable, Any


class PluginSystem:
    def __init__(self):
        self.actions = {}
        self.filters = {}

    def add_action(self, hook_name: str, function: Callable):
        if hook_name not in self.actions:
            self.actions[hook_name] = []
        self.actions[hook_name].append(function)

    def add_filter(self, hook_name: str, function: Callable):
        if hook_name not in self.filters:
            self.filters[hook_name] = []
        self.filters[hook_name].append(function)

    def do_action(self, hook_name: str, *args):
        if hook_name in self.actions:
            for function in self.actions[hook_name]:
                function(*args)

    def apply_filters(self, hook_name: str, value, *args) -> Any:
        if hook_name in self.filters:
            for function in self.filters[hook_name]:
                value = function(value, *args)
        return value
