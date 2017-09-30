import re

print("Expenses calculator:\n\n")
print("1. Enter balance.\n")
print("2. Enter expenditure.\n")
print("3. View ledger.\n")
print("\n")

choice = input("Enter your choice: ")

if choice == '1':
    balance_choice = input("How long you plan to have this balance?(daily,weekly,monthly): ")
    if balance_choice =='daily':
        daily_balance = input("Enter your choice: ")
    elif balance_choice =='weekly':
        weekly_choice = input("Enter your choice: ")
    elif balance_choice =='monthly':
        monthly_choice = input("Enter your choice: ")

elif choice == '2':
    expenditure = []
    take_expenditure = []
    amount = []
    title = []
    take_expenditure = input("please input according to 'value' follows with title. ex '50 on flower:  '")
    matching = re.match('(\w+\s\w+\s\w+)',take_expenditure)
    new_take_list = matching.groups()
    material = new_take_list(0)
    amount = amount.append()
    material_tile = new_take_list(2)
    title = title.append()
    print(amount)
    print(title)
