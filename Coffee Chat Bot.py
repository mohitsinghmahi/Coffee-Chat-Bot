def coffeebot():
    print("Welcome to Mohit's Café!")

    size = get_size()

    drink_type = get_drink_type()
    milk_type = order_latte()
    print(f"Alright, that\'s a {size} {drink_type}!")
    name = input("Can I get your name?")
    print(f"Thanks, {name}, your order will be done shortly.")


def get_size():
    res = input(
        "What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
    if res == "a":
        return "Small"
    elif res == "b":
        return "Medium"
    elif res == "c":
        return "Large"
    else:
        print_message()
        return get_size()


def print_message():
    print('I am sorry, I did not understand your selection. Please enter the corresponding letter for your response.')


def get_drink_type():
    res = input(
        "What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
    if res == "a":
        return "Brewed Coffee"
    elif res == "b":
        return "Mocha"
    elif res == "c":
        return order_latte()
    else:
        print_message()
        return get_drink_type()


def order_latte():
    res = input(
        "What milk would you like for your latte? \n[a] 2% Milk \n[b] Non-Fat Milk \n[c] Soy Milk \n")
    if res == 'a':
        return "2% Milk"
    elif res == 'b':
        return "Non-Fat Milk"
    elif res == 'c':
        return "Soy Milk"
    else:
        print_message()
        return order_latte()


coffeebot()
