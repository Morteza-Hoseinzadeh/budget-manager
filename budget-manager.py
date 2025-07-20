import sys

budget = float(input('Enter your budget: '))
statuses = {'remaining': budget, 'expenses': []}

def budget_manager():
    global statuses

    status = ""

    while status != 'exit':
        status = input('Enter status (add/spent/get) or exit: ')

        if status == 'exit':
            print("Final status:", statuses)
            sys.exit()

        if status not in ["add", "spent", "get"]:
            print("Invalid status. Please enter 'add', 'spent', 'get', or 'exit'.")
            continue

        match status:
            case "add":
                spent = float(input('Enter amount to add: '))
                statuses['remaining'] += spent
                statuses['expenses'].append({
                    'amount': spent,
                    'category': input('Enter expense category: '),
                    "type": status
                })
                print(statuses)

            case "spent":
                spent = float(input('Enter amount to spent: '))
                statuses['remaining'] -= spent
                statuses['expenses'].append({
                    'amount': spent,
                    'category': input('Enter expense category: '),
                    "type": status
                })
                print(statuses)
            
            case "get":
                print(statuses)

        if statuses['remaining'] < 0:
            print("Budget exceeded!")

budget_manager()
