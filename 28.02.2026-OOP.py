# def greet(name, age, phone):
#     return f"Hello {name}"

# greet("Narayan", 56, 78978) # it requires one positional argument

# Class vs Object
# A class is the blueprint 
# An object is the actual thing built from the blueprint
# dunder/magic/special methods __function-name__
# attributes
from datetime import datetime
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says: Woof!"

dog1 = Dog("Bella", "Poodle")
dog2 = Dog("Timmo", "Labrador")

# print(dog1.bark())
# print(dog2.bark())
# print(dog2.name)
# print(dog1.breed)
# Encapsulation - bundle data + behavior - A capsule pill 
# Abstraction - Expose only what's needed, hide complexity - A TV remote
# Inheritance - A child inherits from parent's class - A dog inherits from Animal
# Polymorphism - Same interface, different behavior - All animals make sounds - Dog barks, Cat meows

# Why OOP vs procedural (functions)
# tasks = []
# def create_task(title, priority='low', done=False):
#     return {"title":title, "priority":priority, "done": done, "id":len(tasks)+1}

# def complete_task(task):
#     task['done'] = True

# def get_priority_label(task):
#     labels = {"low":1, "medium":2, "high":3}
#     return labels.get(task['priority'], 5)

# def display_task(task):
#     status = "Yes" if task['done'] else 'No'
#     print(f"[{status}]{get_priority_label(task)} {task['title']} {task['id]}")

# def add_task_to_list(title, priority=1):
#     task = create_task(title, priority)
#     tasks.append(task)
#     return task

# t1 = add_task_to_list('Buy Groceries', "high")
# t2 = add_task_to_list('Read Book', "high")

# complete_task(t1)
# display_task(t1)
# display_task(t2)
# Class variables vs instance variables
# Class Methods vs Instance methods
class Task:    
    _id_counter = 0 # class variables
    # constructor that runs when you create an object
    # self - how Python knows which object to read or write
    VALID_PRORITIES = ('low', 'medium', 'high')
    def __init__(self, title, priority='Low', due_date=None): # instance variables
        # if not title or not title.strip():
        #     raise ValueError ("Task title cannot be empty")
        # if priority not in self.VALID_PRORITIES:
        #     raise ValueError(f"Priority must be one of {self.VALID_PRORITIES}")
        self.title = title.strip()
        self.priority = priority
        self.done = False
        # self.notes = []
        self.created_at = datetime.now().isoformat()
        self.tags = []
        self.due_date = due_date
        Task._id_counter += 1
        self.id = Task._id_counter
        
    ############### instance method ####################
    def complete(self): 
        self.done = True
    
    def add_tag(self, tag):
        """Add a tag to the task"""
        tag = tag.strip().lower()
        if tag not in self.tags:
            self.tags.append(tag)
    
    def is_overdue(self):
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date and not self.done
    
    def __str__(self): #this will be called when you call print
        status = "Yes" if self.done else 'No'
        return f"[{status}]{self.priority_numbers("medium")} #{self.id}:{self.title}"
    ######### class methods ############
    @classmethod
    def reset_counter(cls):
        """Reset the ID counter"""
        cls._id_counter = 0

    @classmethod
    def from_dict(cls, data:dict):
        """Create a task from a dictionary. Perfect for loading from JSON"""
        task = cls(data['title'], data.get('priority', "low"))
        task.done = data.get('done', False)
        task.tags = data.get('tags', [])
        return task
    ######### static methods - utility based  ############
    @staticmethod
    def priority_numbers(priority:str) -> str:
        numbers = {"low":1, "medium":2, "high":3}
        return numbers.get(priority, 5)
    
    @staticmethod
    def is_valid_property(priority:str) -> bool:
        return priority in Task.VALID_PRORITIES

t = Task('Buy Groceries', "high")
t.add_tag('shopping')
t.complete()

data = {"title":"Wash Utensils", "Priority": "low", "tags":['house_work']}
t2 = Task.from_dict(data)
# print(t2)

# print(Task.is_valid_property('high')) # True
# print(Task.is_valid_property('urgent')) # False
# print(Task.priority_numbers('medium')) #2

# [No]2 #2:Wash Utensils
# True
# False
# 2


# Dunder Methods  __str__
class Task1:
    def __init__(self, title, priority='low'):
        self.title = title
        self.priority = priority
        self.done = False
        self.priority_order = {"low":1, "medium":2, "high":3}
    
    def __str__(self): # human readable - used by print() and f-strings
        numbers = {"low":1, "medium":2, "high":3}
        status = "Yes" if self.done else 'No'
        return f"[{status} = {numbers} {self.title}]"
    
    def __repr__(self): # developer readable, used for debugging
        return f"Task1(title={self.title!r}, priority={self.priority!r}, done={self.done})"
    
    def __eq__(self, other):
        """Two tasks are equal if they have the same title"""
        if not isinstance(other, Task1):
            return "This has not been implemented"
        # return NotImplemented - this tells Python that I am unsure how to handle this type (when it's not Task1 type). Try something else
        return self.title.lower() == other.title.lower() # True or False

    def __lt__(self, other):        
        if not isinstance(other, Task1):
            return NotImplemented                
        return self.priority_order[self.priority] > self.priority_order[other.priority]

t1 = Task1('Buy Groceries', "high")
t2 = Task1('Buy Groceries', "medium")
print(t1 == t2)