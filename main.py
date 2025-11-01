# Dictionary where all the expenses will be stored
all_expenses = {}

# Dictionary where all the removed expenses will be stored
removed_expenses = {}

# Function to add an expense
def add():
    while True: 
        try:
            expense_to_add = input('\nEnter your expense: ').title()
            expense_amount = int(input('Enter the amount: '))

            if expense_to_add == '0':
                print('\nAdding expenses was stopped!')
                break

            else:
                all_expenses[expense_to_add] = expense_amount
                print(f'\nExpense: [{expense_to_add}] was added successfully')
        
        except ValueError:
            print('\nPlease enter a valid number.')

# Function to remove and expense
def remove():
    while True:
    
        expense_to_remove = input('\nEnter the expense you want to remove: ').title()

        if expense_to_remove in all_expenses:
            # Expense to remove is removed from the dictionary using .pop()
            removed_expense = all_expenses.pop(expense_to_remove) 
            # It is added to removed_expenses dictionary
            removed_expenses[expense_to_remove] = removed_expense
            # Removed expense is printed
            print(f'\nExpense: [{expense_to_remove}] was removed successfully!')

        elif expense_to_remove == '0':
            print('\nRemoving expenses was stopped!')
            break

        else:
            print('\nExpense does not exist!')

# Function to modify any expense
def modify_expense():
    while True:

        expense_to_modify = input('\nEnter the expense you want to modify: ').title()

        if expense_to_modify in all_expenses:
            try:
                new_amount = int(input('Enter new amount: '))
                # New amount is changed as a value of the expense
                all_expenses[expense_to_modify] = new_amount
                print(f'\nModified expense: {expense_to_modify} - ${new_amount}')

            except ValueError:
                print('\nPlease enter a valid number!')

        elif expense_to_modify == 0:
            print('\nModifying was stopped!')
            break

        else:
            print('\nExpense does not exist!')

# Function to view all expenses
def view():
    # All the keys of the dict are converted to list items
    expense_key = list(all_expenses.keys()) 
    # All the values of the dict are converted to list items
    expense_value = list(all_expenses.values())

    if not all_expenses:
        print('\nNo expenses to show!')

    else:
        print('\nALL EXPENSES:\n')
        # Both key and value lists are printed using zip 
        for i, (expense, amount) in enumerate(zip(expense_key, expense_value),start=1):
            print(f'{i}. {expense} - ${amount}')

# Function to Find total
def sum_of_all_expenses():
    # All the values of the dict are converted to list items and total is calculated using sum keyword
    sum_of_all = sum(list(all_expenses.values()))
    print(f'\nTotal of all expenses: {sum_of_all}')

# Function to view removed expenses
def view_removed_expenses():
    # All the keys of removed dict are converted to list items
    removed_expense_key = list(removed_expenses.keys())
    # All the values of removed dict are converted to list itesm
    removed_expense_value = list(removed_expenses.values())

    if not removed_expenses:
        print('\nNo expenses to show!')

    else:
        print('\nALL REMOVED EXPENSES:\n')
        # Both key and value lists are printed using zip
        for i, (expense, amount) in enumerate(zip(removed_expense_key, removed_expense_value),start=1):
            print(f'{i}: {expense} - ${amount}')

# Function to view the expense with highest amount
def view_highest_amount():

    if not all_expenses:
        print('\nNo expenses to show!')
    # Highest amount is found using max key word
    highest_key = max(all_expenses, key=all_expenses.get)
    highest_amount = all_expenses[highest_key]
    print(f'\nHighest Expense: {highest_key} - ${highest_amount} ')

# Function to view the expense with lowerst amount
def view_lowest_amount():

    if not all_expenses:
        print('\nNo expenses to show!')
        
    lowest_key = min(all_expenses, key=all_expenses.get)
    lowest_amount = all_expenses[lowest_key]
    print(f'\nLowest Expense: {lowest_key} - ${lowest_amount} ')

# Function to clear all the expenses
def clear_all_expenses():

    all_expenses.clear()
    print('\nAll expenses cleared successfully!')

# Function to save all the expenses
def save_all_expenses():
    # Both keys and values are converted to two separate lists
    expense_key = list(all_expenses.keys())
    expense_value = list(all_expenses.values())

    with open('expenses.txt','w')as f:

        if not all_expenses:
            f.write('\nNo expenses to show!')
        # Both key and values list are written side by side using zip
        for i, (expense, amount) in enumerate(zip(expense_key, expense_value),start=1):
            f.write(f'{i}. {expense} - ${amount}')
    print('\nAll expenses are saved in a file name \'expenses.txt\' in your directory.')
    
# Dictionary to store all functions
all_func = {
    'add_expense': add,
    'modify_expense': modify_expense,
    'remove_expense': remove,
    'view_all_expenses': view,
    'view_removed_expenses': view_removed_expenses,
    'view_highest_expense': view_highest_amount,
    'view_lowest_expense': view_lowest_amount,
    'total_of_all_expenses': sum_of_all_expenses,
    'save_all_expenses': save_all_expenses,
    'clear_all_expenses': clear_all_expenses
}

# Function for intro
def intro():
    print("\n" + "="*40)
    print("        💰 EXPENSE TRACKER 💰")
    print("="*40)
    print("        Track • Manage • Analyze")
    print("="*40)
    
    print('\n',"-"*38)

# Function for insturction manual
def instruction_manual():
    print('''
          EXPENSE TRACKER GUIDE:

1. ADD EXPENSE - Enter expense name and amount
2. MODIFY EXPENSE - Modify the name and amount
3. REMOVE EXPENSE - Delete expenses by name  
4. VIEW ALL EXPENSES - See current expenses
5. VIEW REMOVED EXPENSES - See deleted expenses
6. VIEW HIGHEST EXPENSE - Find largest spending
7. VIEW LOWEST EXPENSE - Find smallest spending
8. TOTAL OF ALL EXPENSES - Calculate total spent
9. SAVE ALL EXPENSES - Export to file
10. CLEAR ALL EXPENSES - Reset everything

TIP: Enter '0' to exit any function
''')

# Main function to run the whole shit
def start():

    intro()

    print('\n1. Start')
    print('2. Insturction Manual')

    while True:
        try:

            user_input = int(input('\nEnter your choice (1-2): '))

            if user_input == 1:
                # All keys of the dict are converted in list items
                all_methods = list(all_func.keys())
                print('\nAll the functions are following:')
                for i, j in enumerate(all_methods,start=1):
                    print(f'\n{i}: {j.replace('_',' ').title()}')

                while True:
                    user_choice = int(input('\nEnter your choice: (1-10): '))

                    if user_choice == 0:
                        print('\nExpense tracker was stopped!')
                        break

                    elif 1 <= user_choice <= len(all_methods):
                        # User choice is directed towards the method and method is stored in selected_method
                        # -1 is used because index is behind then the actual number
                        selected_method = all_methods[user_choice - 1]
                        # selected_method is used to call the function in a dictionary
                        # Note: If parenthesis are not used it will not be called it will be stored
                        all_func[selected_method]()
            # Handling all possilbe outputs
                    else:
                        print('\nPlease enter (1-10) / 0.')

            elif user_input == 2:
                instruction_manual()

            elif user_input == 0:
                print('\nTraking was stopped!')
                break

            else:
                print('\nPlease enter (0/1/2)!')

        except ValueError:
            print('\nPlease enter a valid number!')

if __name__ == '__main__':
    start()

# ____________________________________________________________________________________________________
# Created by: Izram Khan
# Date created: 1-Nov-2025
# AI usage: 5%
# All credit goes to: 95% Izram Khand and 5% Deepseek
