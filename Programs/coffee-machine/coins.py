import resources
import drinks

coin_types = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}


def process_coins():
    total = 0
    for coin_type in coin_types:
        value = int(input(f"How many {coin_type}s?: "))
        total += (value * coin_types[coin_type])
    return total


def calc_money(money, drink_type):
    drink_money = drinks.types[drink_type]["money"]
    if money < drink_money:
        print("Sorry that's not enough money. Money refunded")
        return False
    change = money - drink_money
    resources.values["money"]["value"] += drink_money
    print(f"Here is ${change} in change.")
    return True

