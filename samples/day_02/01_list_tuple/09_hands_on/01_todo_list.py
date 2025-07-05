tasks = []

def create(tasks: list[str], task: str):
	"""Add a new task at the end of the tasks"""

def read(tasks: list[str], index: int) -> str:
	"""Return the task in the index given"""

def update(tasks: list[str], index: int, new_task: str):
	"""Change the value in the index to the new task"""

def delete(tasks: list[str], index: int):
	"""Remove the task in the given index"""

# Test

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
