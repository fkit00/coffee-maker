# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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

off = False
dollar = 0
espresso = MENU['espresso']
latte = MENU['latte']
cappuccino = MENU['cappuccino']

def check(a):
    if a["ingredients"]["water"] > resources["water"]:
        print('there is not enough water')
        return False

    if a["ingredients"]["coffee"] > resources["coffee"]:
        print('there is not enough coffee')
        return False
    if espresso:
        return True
    if a["ingredients"]["milk"] > resources["milk"]:
        print('there is not enough milk ')
        return False

def cash(a):
    pennies = int(input('please insert pennies ')) * 0.01
    nickles = int(input('please insert nickles ')) * 0.05
    dimes = int(input('please insert dimes ')) * 0.10
    qaurters = int(input('please insert quarters ')) * 0.25
    total = pennies+nickles+dimes+qaurters

    if a['cost'] == total:
        print('Fantastic! Perfect change')
        return True
    if a['cost'] < total:
        change = total - a['cost']
        print(f"Here is your change ${change}")

        return True
    else:
        print("You don't have enough money")
        return False


def make(a):
    new_water = resources["water"] - a["ingredients"]["water"]
    resources["water"]=new_water
    new_coffee =resources["coffee"] - a["ingredients"]["coffee"]
    resources["coffee"]=new_coffee
    if a != espresso:
       new_milk = resources["milk"] - a["ingredients"]["milk"]
       resources["milk"]=new_milk


while not off:
    start = input("What would you like (espresso/latte/cappuccino): ").lower()
    if start == 'report':
        for n in resources:
            print(f"{n}:{resources[n]}")
        print(f"Money:${dollar}")
    if start == 'off':
        off = True
    if start == 'espresso':
        if check(espresso):
            print(f"This drink costs {espresso['cost']}")
            if cash(espresso):
                make(espresso)
                dollar += espresso['cost']
                print('here is your espresso')
    if start == 'latte':
        if check(latte):
            print(f"This drink costs {latte['cost']}")
            if cash(latte):
                make(latte)
                dollar += latte['cost']
                print('here is your latte')
    if start == 'cappuccino':
        if check(cappuccino):
            print(f"This drink costs {cappuccino['cost']}")
            if cash(cappuccino):
                make(cappuccino)
                dollar += cappuccino['cost']
                print('here is your cappuccino!')