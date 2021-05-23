# put your python code here
available_coffee = 120
available_cups = 9
available_milk = 540
available_water = 400
money = 550

espresso_cost = 4
latte_cost = 7
cappuccino_cost = 6

espresso_water = 250
espresso_coffee = 16

latte_water = 350
latte_milk = 75
latte_coffee = 20

cappuccino_water = 200
cappuccino_milk = 100
cappuccino_coffee = 12


def machine():
    global available_coffee
    global available_cups
    global available_milk
    global available_water
    global money

    global espresso_cost
    global latte_cost
    global cappuccino_cost

    global espresso_water
    global espresso_coffee

    global latte_water
    global latte_milk
    global latte_coffee

    global cappuccino_water
    global cappuccino_milk
    global cappuccino_coffee

    if available_water < 200:
        print("Sorry, not enough water")
        machine()
    elif available_milk < 75:
        print("Sorry, not enough milk")
        machine()
    elif available_coffee < 12:
        print("Sorry, not enough coffee")
        machine()
    else:
        user_options = input(
            "Write action (buy, fill, take, remaining, exit): \n")
        if user_options == "buy":
            buy()
        elif user_options == "fill":
            fill()
        elif user_options == "take":
            take()
        elif user_options == "remaining":
            remaining()
            machine()
        elif user_options == "exit":
            sys.exit()


def buy():
    global available_coffee
    global available_cups
    global available_milk
    global available_water
    global money

    global espresso_cost
    global latte_cost
    global cappuccino_cost

    global espresso_water
    global espresso_coffee

    global latte_water
    global latte_milk
    global latte_coffee

    global cappuccino_water
    global cappuccino_milk
    global cappuccino_coffee

    user = int(input(
        "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back: \n"))

    if user == 1:
        print("I have enough resources, making you a coffee!")
        available_water = available_water - espresso_water
        available_coffee = available_coffee - espresso_coffee
        available_cups -= 1
        money = money + espresso_cost
        print()
    elif user == 2:
        print("I have enough resources, making you a coffee!")
        available_water = available_water - latte_water
        available_coffee = available_coffee - latte_coffee
        available_milk = available_milk - latte_milk
        available_cups -= 1
        money = money + latte_cost
        print()
    elif user == 3:
        print("I have enough resources, making you a coffee!")
        available_water = available_water - cappuccino_water
        available_coffee = available_coffee - cappuccino_coffee
        available_milk = available_milk - cappuccino_milk
        available_cups -= 1
        money = money + cappuccino_cost
        print()
    elif user == "back":
        machine()
        print()

    machine()


def fill():
    global available_coffee
    global available_cups
    global available_milk
    global available_water
    global money

    global espresso_cost
    global latte_cost
    global cappuccino_cost

    global espresso_water
    global espresso_coffee

    global latte_water
    global latte_milk
    global latte_coffee

    global cappuccino_water
    global cappuccino_milk
    global cappuccino_coffee

    user_water = int(
        input("Write how many ml of water do you want to add: \n"))
    user_milk = int(input("Write how many ml of milk do you want to add: \n"))
    user_coffee = int(
        input("Write how many grams of coffee beans do you want to add: \n"))
    user_cups = int(
        input("Write how many disposable cups of coffee do you want to add: \n"))
    available_water += user_water
    available_milk += user_milk
    available_coffee += user_coffee
    available_cups += user_cups
    print()
    machine()


def take():
    global available_coffee
    global available_cups
    global available_milk
    global available_water
    global money

    global espresso_cost
    global latte_cost
    global cappuccino_cost

    global espresso_water
    global espresso_coffee

    global latte_water
    global latte_milk
    global latte_coffee

    global cappuccino_water
    global cappuccino_milk
    global cappuccino_coffee

    print(f"I gave you ${money}")
    money -= money
    print()

    machine()


def remaining():
    global available_coffee
    global available_cups
    global available_milk
    global available_water
    global money

    global espresso_cost
    global latte_cost
    global cappuccino_cost

    global espresso_water
    global espresso_coffee

    global latte_water
    global latte_milk
    global latte_coffee

    global cappuccino_water
    global cappuccino_milk
    global cappuccino_coffee

    print()
    print("The coffee machine has: ")
    print(f"{available_water} of water")
    print(f"{available_milk} of milk")
    print(f"{available_coffee} of coffee beans")
    print(f"{available_cups} of disposable cups")
    print(f"{money} of money")
    print()
    machine()


machine()
