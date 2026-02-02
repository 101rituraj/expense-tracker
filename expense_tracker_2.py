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
    global  maximum_limit
    maximum_limit -= amount
    if maximum_limit <= 0 :
        print("Sorry, You are BROKE")
        print(f"Your Total Balance is : {maximum_limit}")
        return True
    return False

def expense_summary(category_value):
    length_of_expense_list = len(expense_list)
    total = 0
    for i in range(0, length_of_expense_list):
        if expense_list[i]["category"] == category_value:
            print(f"Category : {expense_list[i]["category"]}")
            print(f"Amount : {expense_list[i]["amount"]}")
            print(f"Date : {expense_list[i]["date"]}")
            total += expense_list[i]["amount"]
            print(f"Your total expense on {expense_list[i]["category"]} is : {expense_list[i]["amount"]}")
            print("\n")
    print(f"Your grand total on Category 'Food' is : {total}")

continue_adding = True
while continue_adding:
    user_category = input("What is the category ? : ").lower()
    user_amount = float(input("What is the Amount ? : "))
    user_date = input("What is the Date ? : ")
    adding_expense_to_list(category = user_category, amount = user_amount, date = user_date)
    print(expense_list)
    if broke_message(amount= user_amount):
        continue_adding = False
        user_input = input("You can check the expense history of a particular Category by writing the Category's name : ")
        print("\n")
        expense_summary(category_value = user_input)

