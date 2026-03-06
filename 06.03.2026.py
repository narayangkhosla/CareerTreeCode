# JSON - JavaScript Object Notation
# JSON - text format for storing structured data, It looks like python dictionaries.
# JSON support strings, booleans, null, arrays[], lists, and objects[]
# Serialisation --> Deserialisation
# We nedd to convert our objects to dicts (serialize) and back (de-serailize)


class Task:
    def __init__(self, task_id, title, priority="low"):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.done = False
        self.tags = []

    def complete(self):
        self.done = True

    # Serialisation
    def to_dict(self) -> dict:
        """Convert this Task into a JSON dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "done": self.done,
            "tags": self.tags,
            "type": self.__class__.__name__,
        }

    # "Deserisation"
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a task from dictionary"""
        task = cls(data["id"], data["title"], data.get("priority", "low"))
        task.done = data.get("done", False)
        task.tags = data.get("tags", [])
        return task


# t = Task("Go to Gym", "high")
# t.tags = ["exercise", "energetic"]

# d = t.to_dict()
# print(d)

# t2 = Task.from_dict(d)
# print("=" * 70)
# print(t2.title)
# print(t2.tags)
# Task Manager - Saving and Loading
import json
import os
from unittest import result


class TaskManager:
    """Manages a collection of tasks with JSON persistence"""

    DATA_FILE = "tasks.json"

    def __init__(self):
        self.tasks: list[Task] = []
        self.next_id = 1
        self.load()  # load from disk on startup

    # CRUD - Create, Read, Update, Delete
    def add_task(self, title, priority="low") -> Task:
        task = Task(self.next_id, title, priority)
        self.tasks.append(task)
        self.next_id += 1
        self.save()  # need to make this
        return task

    def get_task(self, task_id: int) -> Task | None:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save()
            return True
        return False

    def complete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            task.complete()
            self.save()
            return True
        return False

    # Lists all the tasks
    def list_tasks(self, show_done=True) -> list[Task]:
        if show_done:
            return self.tasks

        result = []
        for t in self.tasks:
            if not t.done:
                result.append(t)
        return result

    def save(self):
        """Save all the tasks to the JSON file"""
        tasks_list = []
        done_count = 0
        for t in self.tasks:
            tasks_list.append(t.to_dict())
            if t.done:
                done_count += 1

        data = {
            "tasks": tasks_list,
            "meta": {
                "total": len(self.tasks),
                "done": done_count,
                "next_id": self.next_id,
            },
        }
        with open(self.DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        """Load tasks from the JSON file"""
        if not os.path.exists(self.DATA_FILE):
            return
        try:
            with open(self.DATA_FILE, "r") as f:
                data = json.load(f)
            self.tasks = []
            task_list = data.get("tasks", [])
            for d in task_list:
                task = Task.from_dict(d)
                self.tasks.append(task)

            meta = data.get("meta", {})

            if "next_id" in meta:
                self.next_id = meta["next_id"]
            else:
                self.next_id = len(self.tasks) + 1

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not load data file :{e}")
            self.tasks = []
            self.next_id = 1

    def __repr__(self):
        return f"TaskManager({len(self.tasks)} tasks.)"


tm = TaskManager()

tm.add_task("Buy Milk", "high")
tm.add_task("Finish Python Project", "medium")
tm.add_task("Go for a walk")

print("All tasks:")
for task in tm.list_tasks():
    print(task.id, task.title, task.priority, task.done)

tm.complete_task(1)
print("After completing task 1:")
for task in tm.list_tasks():
    print(task.id, task.title, task.priority, task.done)

tm.delete_task(2)
print("After completing task 2:")
for task in tm.list_tasks():
    print(task.id, task.title, task.priority, task.done)
