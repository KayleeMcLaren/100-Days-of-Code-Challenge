
from info import menu, resources

money_earned = 0.0
machine_on = True
enough_resources = True


def process_payment(num_of_quarters, num_of_dimes, num_of_nickels, num_of_pennies, order):
    """Function to calculate the total value of the coins used to pay, check whether that is enough to pay for the
    order, and calculate the change for the user"""
    global money_earned
    total = 0.0
    total += num_of_quarters * 0.25
    total += num_of_dimes * 0.10
    total += num_of_nickels * 0.05
    total += num_of_pennies * 0.01

    if total == menu[order]['cost']:
        money_earned += menu[order]['cost']
        print(f"Here is your {order}. Enjoy!")
    elif total > menu[order]['cost']:
        money_earned += menu[order]['cost']
        print(f"Here is ${round(total - menu[order]['cost'], 2)} change and your {order}. Enjoy!")
    else:
        print(f"Sorry that is not enough money. Money refunded.")


def check_resources(order):
    """Function to check if there are enough resources to fulfil the order. If so, it returns True. If not it prints out
    a message stating which resource there isn't enough of and returns False"""
    global enough_resources
    if order == 'espresso':
        if resources['water'] >= menu[order]['ingredients']['water']:
            if resources['coffee'] >= menu[order]['ingredients']['coffee']:
                return True
            else:
                print("Sorry! There is not enough coffee")
                enough_resources = False
                return False
        else:
            print("Sorry! There is not enough water")
            enough_resources = False
            return False

    if order == 'latte' or order == 'cappuccino':
        if resources['water'] >= menu[order]['ingredients']['water']:
            if resources['milk'] >= menu[order]['ingredients']['milk']:
                if resources['coffee'] >= menu[order]['ingredients']['coffee']:
                    return True
                else:
                    print("Sorry! There is not enough coffee")
                    enough_resources = False
                    return False
            else:
                print("Sorry! There is not enough milk")
                enough_resources = False
                return False

        else:
            print("Sorry! There is not enough water")
            enough_resources = False
            return False


def adjust_resources(order):
    """Function to adjust the amounts of each resource"""
    if order == 'espresso':
        resources['water'] = resources['water'] - 50
        resources['coffee'] = resources['coffee'] - 18

    elif order == 'latte':
        resources['water'] = resources['water'] - 200
        resources['milk'] = resources['milk'] - 150
        resources['coffee'] = resources['coffee'] - 24

    else:
        resources['water'] = resources['water'] - 250
        resources['milk'] = resources['milk'] - 100
        resources['coffee'] = resources['coffee'] - 24

def report():
    """Function to generate a report showing the amounts of resources and the money earned"""
    global money_earned
    formatted_money_earned = "{:.2f}".format(money_earned)
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"\nReport: \nWater: {water} \nMilk: {milk} \nCoffee: {coffee} \nMoney Earned: ${formatted_money_earned}"

"""Program starts here"""
while machine_on:
    while enough_resources:
        print("\nMenu: \nEspresso - $1.50 \nLatte - $2.50 \nCappuccino - $3.00")
        order = input("\nWhat would you like? (espresso, latte, or cappuccino): ").lower()
        if order == 'off':
            print("Turning machine off")
            machine_on = False
        elif order == 'report':
            print(report())
        else:
            if check_resources(order=order):
                print("Please insert coins")
                quarters = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickels = int(input("How many nickels: "))
                pennies = int(input("How many pennies: "))
                adjust_resources(order=order)
                process_payment(num_of_quarters=quarters, num_of_dimes=dimes, num_of_nickels=nickels,
                                num_of_pennies=pennies, order=order)
                                
