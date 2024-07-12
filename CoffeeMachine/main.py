MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


run_machine = True
current_water = resources['water']
current_milk = resources['milk']
current_coffee = resources['coffee']
current_money = 0

def transaction_status(total, drink_cost):
    if total > drink_cost:
        print(f"Here is your change: {round(total - drink_cost, 2)}")
        return True
    elif total == drink_cost:
        return True
    else:
        return False
def run_report():
    print(f'Water: {resources['water']}ml')
    print(f'Milk: {resources['milk']}ml')
    print(f'Coffee: {resources['coffee']}g')
    print(f'Money: ${current_money}')

def gather_money():
    total = 0.0
    total += int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total

def process_transaction(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True

while run_machine:
    choice = input('What would you like? (espresso/latte/cappuccino):').lower()

    if choice == "off":
        run_machine = False
    elif choice == "report":
        run_report()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            print("Please insert coins")
            total_inserted = gather_money()
            if transaction_status(total_inserted, drink["cost"]):
                current_money += drink["cost"]
                process_transaction(drink["ingredients"])
                print(f"Enjoy your {choice}!")





# TODO: Show everytime action is completed. (coffee dispensed, transaction complete, etc.
#TODO PROCESS COINS
#TODO CHECK IF ENOUGH MONEY WAS INSERTED, IF NOT, PRINT "SORRY THATS NOTE NOUGH MONEY/ MOENY REFUNDED.
#   IF ENOUGH ENTERED, COST GETS ADDED TO MACHINE PROFIT
#   IF TOO MUCH MONEY, REFUND CHANGE. "HERE IS XXX DOLLARS IN CHANGE. ROUNDED TO .2
#TODO MAKE COFFEE - DEDUCT INGREDIENTS FROM RESOURCES
#   print('Here is your latte. Enjoy!')
