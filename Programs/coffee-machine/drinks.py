import resources

types = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "money": 1.50,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "money": 2.50,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "money": 3.00,
    }
}


def resources_needed(drink_name):
    requirements = True

    for resource_type in types[drink_name]:
        if resource_type == "money":
            break
        resource_value = types[drink_name][resource_type]
        if resource_value > resources.values[resource_type]["value"]:
            print(f"Sorry there is not enough {resource_type}.")
            requirements = False

    return requirements


def make(drink_name):
    for resource_type in types[drink_name]:
        if resource_type == "money":
            break
        resource_value = types[drink_name][resource_type]
        resources.values[resource_type]["value"] -= resource_value
    print(f"Here is your {drink_name}☕️. Enjoy!")
