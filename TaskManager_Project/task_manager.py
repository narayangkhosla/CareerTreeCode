import json  # built-in modules - Standard library
import os
from task import Task
from task import *  # import eveyrthing
import pandas

# Third party packages - 500,000 packages
# module, packages


class TaskManager:
    DATA_FILE = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load()

    def add_task(self, title, priority="low"):
        task = Task(self.next_id, title, priority)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
        return task

    def get_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save()
            return True
        return False

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.complete()
            self.save()
            return True
        return False

    def list_tasks(self, show_done=True):
        if show_done:
            return self.tasks

        result = []
        for t in self.tasks:
            if not t.done:
                result.append(t)
        return result

    def save(self):
        data = {
            "tasks": [t.to_dict() for t in self.tasks],
            "meta": {
                "total": len(self.tasks),
                "done": sum(1 for t in self.tasks if t.done),
                "next_id": self.next_id,
            },
        }

        with open(self.DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        if not os.path.exists(self.DATA_FILE):
            return

        try:
            with open(self.DATA_FILE, "r") as f:
                data = json.load(f)

            self.tasks = [Task.from_dict(d) for d in data.get("tasks", [])]
            self.next_id = data.get("meta", {}).get("next_id", len(self.tasks) + 1)

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not load data file: {e}")
            self.tasks = []
            self.next_id = 1

    def __repr__(self):
        return f"TaskManager({len(self.tasks)} tasks)"
