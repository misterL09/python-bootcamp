tasks = []

def create(tasks, task):
	"""Add a new task at the end of the tasks"""

def read(tasks, index) -> str:
	"""Return the task in the index given"""

def update(tasks, index, new_task):
	"""Change the value in the index to the new task"""

def delete(tasks, index):
	"""Remove the task in the given index"""

"""
Test code is written below

If the statement on the right of `assert` is True, nothing happens
If the statement on the left of `assert` is False, it raises an error

So if the code doesn't raise an error, then the functions are implemented well
"""

create(tasks, "Buy milk")
create(tasks, "Do homework")
create(tasks, "Sleep")

assert "Buy milk" in tasks
assert read(tasks, 1) == "Do homework"

update(tasks, 0, "Buy coffee")
assert "Buy milk" not in tasks
assert "Buy coffee" in tasks

delete(tasks, 2)
assert "Sleep" not in tasks
assert len(tasks) == 2
