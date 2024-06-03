import resources
import drinks
import coins

should_continue = True

def check_user_prompt(user_prompt):
    global should_continue
    if user_prompt == "report":
        resources.report()
        return False
    elif user_prompt == "off":
        should_continue = False
        return False
    else:
        return True


resources.fill(300, 200, 100, 0)

while should_continue:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if check_user_prompt(user_prompt):
        drink_name = user_prompt
        if drinks.resources_needed(drink_name):
            print("Please insert coins")
            money = coins.process_coins()
            if coins.calc_money(money, drink_name):
                drinks.make(drink_name)

