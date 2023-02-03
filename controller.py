"""
The controller handles the menu and handing off to the order actions handler
"""
from order_actions import run_action


def run(database):
    """
    Run the thing
    :param database: The database
    :return: bool - Determines whether the application should exit, return True to exit
    """

    print("""
QA Cafe Order System

1) Enter Order
2) Order Info
3) All Orders
4) Update Order
5) Delete Order
6) Delete All Orders
7) Exit
""")

    valid_choices = list(range(1, 7+1))

    choice = input("Please enter a choice above: ")

    try:
        choice = int(choice)
    except ValueError:
        print("That is not a valid option")
        return False

    if choice not in valid_choices:
        print("That is not a valid option")
        return False

    return run_action(choice, database)
