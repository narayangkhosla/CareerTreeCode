class Task:
    def __init__(self, task_id, title, priority="low"):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.done = False
        self.tags = []
        self.notes = ""

    def complete(self):
        self.done = True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "done": self.done,
            "tags": self.tags,
            "notes": self.notes,
            "type": self.__class__.__name__,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        task = cls(data["id"], data["title"], data.get("priority", "low"))
        task.done = data.get("done", False)
        task.tags = data.get("tags", [])
        task.notes = data.get("notes", "")
        return task

    # def __str__(self):
    #     status = "Done" if self.done else "Not Done"
    #     return f"[{self.id}] {self.title} | Priority: {self.priority} | {status}"
    def __str__(self):
        status = "✅" if self.done else "❌"
        return f"{status} [{self.id}] {self.title} | Priority: {self.priority}"


class Task1:
    pass
