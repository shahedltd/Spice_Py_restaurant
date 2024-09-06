import datetime


def greet_based_on_time():
    current_time = datetime.datetime.now().time()

    if current_time >= datetime.time(18, 0) or current_time < datetime.time(6, 0):
        print("Hello sir, Welcome to Spice Py restaurant ❤️\nHave a nice night sir! 😊🌙")
    else:
        print("Good Morning sir ☀️☁️!\nWelcome to Spice Py restaurant")


def order_food():
    total_bill = 0
    total_order = []

    menu = """
    APPETIZERS:
    1. Garlic Bread - $4.99
    2. Caesar Salad - $6.99
    3. Mozzarella Sticks - $7.99
    MAIN COURSES:
    4. Grilled Chicken Alfredo - $12.99
    5. BBQ Beef Burger with Fries - $11.99
    6. Margherita Pizza - $10.99
    DESSERTS:
    7. Chocolate Lava Cake - $6.50
    8. New York Cheesecake - $5.50
    9. Ice Cream Sundae - $4.99
    DRINKS:
    10. Soft Drinks - $2.99
    11. Coffee/Tea - $2.50
    12. Fresh Juice - $3.50
    """

    price_list = {
        1: ("Garlic Bread", 4.99),
        2: ("Caesar Salad", 6.99),
        3: ("Mozzarella Sticks", 7.99),
        4: ("Grilled Chicken Alfredo", 12.99),
        5: ("BBQ Beef Burger with Fries", 11.99),
        6: ("Margherita Pizza", 10.99),
        7: ("Chocolate Lava Cake", 6.50),
        8: ("New York Cheesecake", 5.50),
        9: ("Ice Cream Sundae", 4.99),
        10: ("Soft Drinks", 2.99),
        11: ("Coffee/Tea", 2.50),
        12: ("Fresh Juice", 3.50)
    }

    name = input("Please enter your name sir, if you don't want to enter your name you can skip it!\n: ").capitalize()

    while True:
        print(f"{name} sir, the food menu of our restaurant is shown below:")
        print(menu)

        try:
            restaurant_menu = int(input(f"{name} sir please order by selecting the corresponding number: "))
            if restaurant_menu in price_list:
                item_name, item_price = price_list[restaurant_menu]
                total_order.append(f"{item_name} - ${item_price}")
                total_bill += item_price
                print(f"You have ordered: {item_name}")
                print(f"Current Total: ${total_bill:.2f}")
            else:
                print("Invalid selection, please choose a valid menu option.")
        except ValueError:
            print("Please enter a valid menu number.")

        order_again = input(f"{name}, do you want to order again? 'Y/N'\n: ").upper()
        if order_again != 'Y':
            break

    print(f"\n{name}, your total order is:")
    for order in total_order:
        print(order)
    print(f"Total Bill: ${total_bill:.2f}\nSir if you like our service and food then come again to our restaurant! 😊")
    return total_bill

greet_based_on_time()
order_food()
