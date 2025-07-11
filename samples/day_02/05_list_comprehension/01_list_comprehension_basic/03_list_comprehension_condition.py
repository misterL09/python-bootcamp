tasks = {
    'register': 'high',
    'test': 'medium',
    'refactor': 'low',
}

# Manual
priority_tasks = []
for task, prio in tasks.items():
    if prio != 'low':
        priority_tasks.append(task)

print(priority_tasks)

# List comprehension
priority_tasks = [task for task, prio in tasks.items() if prio != 'low']
print(priority_tasks)
