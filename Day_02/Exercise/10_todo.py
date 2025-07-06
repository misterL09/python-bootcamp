tasks =[]
def create(inner_tasks: list[str], task: str):
    inner_tasks.append(task)
def read(inner_tasks: list[str], inner_index: int) -> str:
    return inner_tasks[inner_index]
def update(inner_tasks: list[str], inner_index: int,new_task: str ):
    inner_tasks[inner_index]=new_task
def delete(inner_tasks: list[str], index: int):
    tasks.pop(index)

create(tasks,"nathan")
print(tasks)

print(read(tasks,0))

update(tasks,0,"ken")
print(tasks)

delete(tasks,0)
print(tasks)