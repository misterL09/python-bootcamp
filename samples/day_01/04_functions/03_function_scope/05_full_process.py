def get_expenses():
    food = float(input("Food expense: "))
    transpo = float(input("Transport expense: "))
    return food + transpo

def get_budget():
    return float(input("Enter your budget: "))

def check_budget(total, budget):
    if total > budget:
        return "Over budget!"
    return "Within budget."

total = get_expenses()
budget = get_budget()
print("Status:", check_budget(total, budget))


