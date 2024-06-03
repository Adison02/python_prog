values = {
    "water": {
        "value": 0,
        "unit": "ml",
    },
    "milk": {
        "value": 0,
        "unit": "ml",
    },
    "coffee": {
        "value": 0,
        "unit": "g",
    },
    "money": {
        "value": 0,
        "unit": "$",
    }
}


def fill(water, milk, coffee, money):
    fill_values = [water, milk, coffee, money]
    
    i = 0
    for resource in values:
        values[resource]["value"] = fill_values[i]
        i += 1
        

def report():
    for resource in values:
        name = resource.capitalize()
        value = values[resource]["value"]
        unit = values[resource]["unit"]
        print(f"{name}: {value}{unit}")
