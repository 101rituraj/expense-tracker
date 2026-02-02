"""a program where a user can add an expense (Category, Amount, Date), view a summary of spending by category
and see the remaining balance"""

maximum_limit = 1000

expense_list = []


def adding_expense_to_list(category, amount, date):
    new_expense = {
    "category" : category,
    "amount" : amount,
    "date" : date,
    }
    expense_list.append(new_expense)

def broke_message(amount):
    global maximum_limit
    maximum_limit -= amount
    if maximum_limit <= 0 :
        print("Sorry, You are BROKE")
        print(f"Your Total Balance is : {maximum_limit}")

continue_adding = True
while continue_adding:
    user_category = input("What is the category ? : ").lower()
    user_amount = float(input("What is the Amount ? : "))
    user_date = input("What is the Date ? : ")
    adding_expense_to_list(category = user_category, amount = user_amount, date = user_date)
    print(expense_list)
    broke_message(amount = user_amount)