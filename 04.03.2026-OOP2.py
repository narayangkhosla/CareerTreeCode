# Inheritance - lets a child class inherit attributes and methods from the parent class.
# IS-A relationship
# Task --> Urgent task, recurring task, project task etc.
from datetime import datetime, timedelta

from colorama import init


class Task:
    def __init__(self, title, priority="low"):
        self.title = title
        self.priority = priority
        self.done = False
        self.tags = []

    def complete(self):
        self.done = True
        return self

    def describe(self):
        return f"Task: {self.title} [{self.priority}]"

    def __str__(self):
        numbers = {"low": 1, "medium": 2, "high": 3}
        status = "Yes" if self.done else "No"
        return f"[{status}] {numbers} {self.title}"

    def __repr__(self):
        return f"Task({self.title!r}, {self.priority!r})"


class UrgentTask(Task):  # urgent inherits from task
    """ "An urgent task with a deadline and escalation"""

    def __init__(self, title, deadline_hours=24):
        super().__init__(title, priority="high")
        self.deadline = datetime.now() + timedelta(hours=deadline_hours)
        self.escalated = False

    def hours_remaining(self):
        delta = self.deadline - datetime.now()
        return max(0, delta.total_seconds() / 3600)

    def escalate(self):
        self.escalated = True
        print(f"ESCALATED: {self.title}")

    def __str__(self):
        base = super().__str__()  # reuse parent's string
        hrs = self.hours_remaining()
        escalated_str = "Cool" if self.escalated else "Hot"
        return f"{base} ({hrs:.1f}h left) {escalated_str}"


class RecurringTask(Task):
    """A task that repeats on a schedule"""

    FREQ_DAYS = {"daily": 1, "weekly": 7, "monthly": 30}

    def __init__(self, title, frequency="weekly", priority="low"):
        super().__init__(title, priority)
        self.frequency = frequency
        self.last_completed = None

    def complete(self):  # overriding parent's complete()
        self.done = True
        self.last_completed = datetime.now()
        return self

    def next_due(self):
        if self.last_completed is None:
            return "Not yet done"
        days = self.FREQ_DAYS.get(self.frequency, 7)
        return self.last_completed + timedelta(days=days)

    def __str__(self):
        base = super().__str__()
        return f"{base} [{self.frequency}]"


t = Task("Write report", "medium")
ut = UrgentTask("Fix Production bug", deadline_hours=2)
rt = RecurringTask("Team Standby", "weekly")

# print(t)  # __str__
# print(ut)
print(rt)
# super() - calling the parent's class method
# method overriding - same method exists both in parents + child class
#
# POLYMORPHISM - many forms
tasks = [
    Task("Buy Groceries", "low"),
    UrgentTask("Deploy Hot fix", deadline_hours=1),
    RecurringTask("Daily Standup", "daily"),
]
# we can str() on each - each class handles it differently
# for task in tasks:
#     print(task)
# for task in tasks:
#     task.complete()
for task in tasks:
    print(task.describe())
