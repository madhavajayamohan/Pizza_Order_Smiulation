# Global variables/CONSTANTS (if needed)
STARTER_MENU = {"Garlic Knots": 10,
                "Jalapeno Poppers": 21,
                "French Fries": 10,
                "Potato Wedges": 10}

PIZZA_MENU = {"Cheese Pizza": 45,
              "Pepperoni Pizza": 60,
              "Vegetarian Pizza": 60,
              "BBQ Chicken Pizza": 60,
              "Aubergine Pizza": 60}

DESSERT_MENU = {"Nutella Calzone": 14,
                "Cookie Ice Cream Pie": 16,
                "Brownie Ice Cream Pie": 16,
                "Assorted Cakes": 19}
# All menus based off of actual Escape from New York Pizzeria
# All these dictionaries are different menus, and the key for each menu
# is the food item, while the value is the price of that item in AED

VAT = 1.05  # Value Added Tax, divided by 100, plus 1. Just multiply to
# total cost to get the final cost

STARTER_TIME = 10
PIZZA_TIME = 60
DESSERT_TIME = 20
# These variables show the amount of time in minutes to prepare each of the
# three different food types in the pizzeria: Starters, Pizza, and Dessert


# Functions
"""
Function: print_menu
Prints one of the following global variables:
    - STARTER_MENU
    - PIZZA_MENU
    - DESSERT_MENU

@param: A Dictionary; one of the global variables
@param: A string; which tells us for which menu was passed on 
        to print_menu
@retrun: Nothing
"""


def print_menu(menu, menu_type):
    print("\n" + menu_type + " Menu")

    for key in menu:
        print("\t" + str(key) + "        " + str(menu[key]) + " AED")


"""
Function: add_item_to_order
Asks the user which item they want from the menu

@param: A Dictionary; one of the global variables
@param: A string; which tells us for which menu was passed on 
        to print_menu
@return: A tuple that contains three elements.
        - The first element is the item ordered
        - The second element is the price of the item ordered
        - The third element is the time it takes to prepare the item ordered

        If the user does not order an item, all three values in the returned
        tuple will be 0
"""


def add_item_to_order(menu, menu_type):  # Parameter menu_type is used so that
    # this method can be used for all three
    # scenarios
    while True:
        print_menu(menu, menu_type)
        choose_item = "YES" == input("\nWould you like to order a " + menu_type + " (YES/NO): ").upper()
        # This is a common type of boolean definition I use throughout program
        # If the value is yes, no matter what case user eneters it in, I make it
        # uppercase and compare if it's equal to "YES". If it is, then
        # Choose_item is True. Enter anything other than yes, and choose_item is
        # False

        if choose_item:
            item = input("\nWhich " + menu_type + " would you like?: ")

            if not item in menu:
                print(
                    "Sorry, that " + menu_type + " is not in the menu. \nPlease remember to type in the " + menu_type +
                    " exactly the way \nyou see it on the menu")
                continue
                # If user input does not match any key within the dictionary
                # above message is printed, and then loop is made to start again

            print("Your item has been ordered")
            if menu_type == "Starter":
                return (item, menu[item], STARTER_TIME)
            elif menu_type == "Pizza":
                return (item, menu[item], PIZZA_TIME)

            return (item, menu[item], DESSERT_TIME)

            # Tuple is returned. The if statement is used to find out which menu
            # food item user asked for. This is one of the uses of parameter
            # menu_type
        else:
            return (0, 0, 0)
            # In the case the user does not want any food items from the menu,
            # This tuple is returned


"""
Function: update_order
Specifically, updates the list order and price_list after add_item_to_order
is called.

@param: A tuple, the tuple which add_item_to_order returns
@param: A list, the list order
@param: A list, the list price_list
@return: Nothing
"""


def update_order(tuple, order, price_list):
    if tuple[0] != 0:
        order.append(tuple[0])
        price_list.append(tuple[1])
    # Updates order and price_list if the inital value of the tuple is 0.


"""
Function: bill_receipt
Prints out the reciept of the user, which contains all the items the user
has ordered, the number of each the user has ordered, the amount of money
user spends for each item, and the total amount of money user has spent.

The function also combines all repetitions of one item in order, and the
prices of those items in price_list, into one single element in 
receipt_items and receipt_item_prices

@param: A list, the list order
@param: A list, the list price_list
@param: An integer, the variable total_cost
@return: Nothing
"""


def bill_receipt(order, price_list, cost):
    receipt_items = []
    receipt_item_prices = []
    # These two respective lists are created so as to have a better printed view
    # Of the user's order. Using this, I can combine multiple occurences of the
    # same item. For example, a user can order two Grlic knots. INstead of having
    # garlic knots appear two seperate times on the receipt, which would happen if
    # I just looped and printed out the items in order, I can combine all those
    # multiple occurences and make them one single object such as
    # 2 x Garlic Knots in recepit_items

    items_already_done = []
    # This list is to avoid repeition; explained lated in code

    print("\nYour Receipt: ")

    for item in order:
        num_of_item = order.count(item)
        # This tells me the amount of occurences of the food item in the order

        if not item in items_already_done:
            receipt_items.append(str(num_of_item) + " x " + item)
            receipt_item_prices.append(price_list[order.index(item)] * num_of_item)
            # price_list[order.index(item)] = price of the respective item the
            # for loop is looking at. I then multiply this price by the number of
            # of items in the receipt, to get the total cost for the sum of items

            items_already_done.append(item)
            # items_already_done is used to avoid repetition. If there are
            # multiple occurences of the same item, then in the loop for item in
            # order, after the first occurence, then the same item will appear
            # again. This causes repetition of the same information. In the example
            # of the user buying only two garlic knots, what would happen without
            # items_already done is the following code:

            """
            Your receipt:
            2 x Garlic Knots                      20 AED
            2 x Galric Knots                      20 AED
            ___________________________________________
            Total................................20 AED
            """

            # Because of the second occurence, 2 x Garlic Knots is printed again
            # Thus, using items_already_done, I can append food items that are
            # already in recipt_items and receipt_item_prices. Then, with the
            # if statement onf line 155, I can avoid repetition, because it won't
            # run if the food item is already in items_already_done, and thus
            # the information si already in the receipt lists.

    for i in range(len(receipt_items)):
        print(receipt_items[i] + "..................." + str(receipt_item_prices[i]) + " AED")
    # I use a regular for loop instead of a for loop that loops through the item
    # for the simplicity of writing. Each sum of goods in receipt_items corresponds
    # to the price of the sum of goods in receipts_price_list. By using i, I can
    # just i for both rather thand elving into the terriorory of the index function

    print("______________________________________________________")
    print("Total............................................" + str(round(total_cost * VAT, 2)) + " AED")
    # This is the only place I multiply the total price of the order by VAT
    # Technically, the total_cost variable never becomes the total price of the order,
    # but it doesn't really matter as this is the only function where price is printed
    # Notice how I round it to 2 decimal points, which is how price is rounded


"""
Function: remove_item
This function removes one single item from the order of the user, and makes
the corresponding changes in price_list, order_finish_time and total_cost

@param: A list, order
@param: A list, price_list
@param: An integer, order_finish_time
@param: An integer, total_cost
@return: Nothing
"""


def remove_item(order, price_list, order_finish_time, total_cost):
    while True:
        item = input("\nWhich item would you like to remove?: ")

        if not item in order:
            remove_confirmed = "YES" == input(
                "The item you asked to remove is not in your order. Do you still want to remove an item? (YES/NO): ").upper()
            # Notice that I ask additional confirmation. I assume an actual website
            # Would amke sure the user orders as much as posisble and would try
            # to provoke second thoughts.

            if remove_confirmed:
                print("\nPlease remember to input your response with proper punctuation.")
            else:
                print("\nYour item has not been removed")
                break

        else:
            total_cost -= price_list[order.index(item)]
            # Subtacts price of item, from total_cost. The price of each item in
            # price_list and the item in order   each correspond, so the index
            # of the item is the same as the price in price_list

            price_list.remove(price_list[order.index(item)])
            # Then I remove that item afterwards, because I need price_list[order.index(item)]
            # to change total_cost

            order.remove(item)
            # Then I remove item for order her because I need item in order for
            # the last two variables

            if item in STARTER_MENU:
                order_finish_time -= STARTER_TIME
            elif item in PIZZA_MENU:
                order_finish_time -= PIZZA_TIME
            else:
                order_finish_time -= DESSERT_TIME

            # This set of if statements looks at which dictionary the item is from
            # so as to find out how much time it would take to prepare that item,
            # and to subtract that amount from order_finish_time

            print("\nYour item has been removed")
            break


# --------------------------------------------
# MAIN CODE BELOW
# --------------------------------------------
order_finish_time = 0  # This shows how much time it takes to prepare the whole order
order = []  # A list with all the food items the user ordered
price_list = []  # A list with the prices of all the food items the user ordered
# Each price corresponds to the food item in order
total_cost = 0  # This is the total cost of the order the user has made

print("Welcome to the New York Pizzeria")

while True:
    print("\nTable of Contents")
    print("\t1. View Starter Menu\n\t2. View Pizza Menu" +
          "\n\t3. View Desert Menu\n\t4. Done with Order\n")

    try:
        choice = int(input("Please choose an option. Choose view menu to order " +
                           "an item: "))
        if not type(choice) is int or choice < 1 or choice > 4:
            raise Exception("INVALID CHOICE")
            # the raises Exception() statemenet raises an exception, even when
            # code works. In this case, it raises an exception if the input is
            # not an integer, or if the choice is not between 1-4
    except:
        print("That choice is invalid. Please choose another choice.\n")
        continue  # After printing above line, loop restarts

    # The try and except is used to make sure user enters a valid choice

    if choice == 1:
        starter_tuple = add_item_to_order(STARTER_MENU, "Starter")
        # starter_tuple recieves tuple add_item_to_order returns

        update_order(starter_tuple, order, price_list)
        total_cost += starter_tuple[1]
        order_finish_time += starter_tuple[2]
        # Uses the tuple to update order, price_list, total_cost, and
        # order_finish time

    elif choice == 2:
        pizza_tuple = add_item_to_order(PIZZA_MENU, "Pizza")
        # pizza_tuple recieves tuple add_item_to_order returns

        update_order(pizza_tuple, order, price_list)
        total_cost += pizza_tuple[1]
        order_finish_time += pizza_tuple[2]
        # Uses the tuple to update order, price_list, total_cost, and
        # order_finish time

    elif choice == 3:
        dessert_tuple = add_item_to_order(DESSERT_MENU, "Dessert")
        # dessert_tuple recieves tuple add_item_to_order returns

        update_order(dessert_tuple, order, price_list)
        total_cost += dessert_tuple[1]
        order_finish_time += dessert_tuple[2]
        # Uses the tuple to update order, price_list, total_cost, and
        # order_finish time

    else:
        # I use len(order) because if the length of the order is 0, then that means
        # The user didn't order anything, and thus the user doesn't want anything
        # Thus, the code below should only run if there is something in list, or
        # if len(order) > 0

        if not len(order) == 0:
            bill_receipt(order, price_list, total_cost)
            print("\nThis is the receipt of your order.")
            # Prints receipt

            to_cancel = "YES" == input("Do you want to cancel you order? (YES/NO): ").upper()

            if to_cancel:
                order = []
                order_finish_time = 0
                price_list = []
                total_cost = 0

                print("Yor order has been cancelled.")
                # This is the option to cancel, which the user may want to do.
                # If they want to cancel, this if statement runs, and I make
                # order and price_list empty, and order_finish_time and total_cost
                # 0. Thus, as all data is erased, order is cancelled

                make_new_order = "YES" == input("Would you like to make a new order? (YES/NO): ").upper()

                if make_new_order:
                    continue

                # This is the prompt to make user want to make another order. If
                # they want to, the continue statement make the loop restart, and
                # thus they can restart their order as they please

            else:
                # If user likes order, then the following statements run, which
                # gives user options to add or remove any items

                to_remove_item = "YES" == input("\nWould you like to remove an item? (YES/NO): ").upper()

                if to_remove_item:
                    remove_item(order, price_list, order_finish_time, total_cost)
                    # Calls remove_item
                    continue_to_remove = True

                    while continue_to_remove:
                        bill_receipt(order, price_list, total_cost)

                        continue_to_remove = "YES" == input(
                            "\nThis is you new receipt. Would you like to remove another item? (YES/NO): ").upper()
                        # I first assume continue_to_remove is true. I then print
                        # the recipt again to show the user the new amount of
                        # goods, and the new price of the order. I then ask if they
                        # want to remove anything else

                        if continue_to_remove:
                            remove_item(order, price_list, order_finish_time, total_cost)
                            # If they do want to continue removing, I all remove_item
                            # again
                        else:
                            break
                            # Else, I break, and stop removing
                # The following statements remove any food_items that isn't wanted
                # by user

                to_add_item = "YES" == input("\nWould you like to add an item? (YES/NO): ").upper()

                if to_add_item:
                    continue

                # This asks if they want to add something. If they want to add
                # something, then they are redirected to start of loop, where
                # they an choose whatever they want
        break

if len(order) == 0:
    print("\nPlease come to Escape from New York Pizzeria again.")
else:
    print("\n")
    bill_receipt(order, price_list, total_cost)
    print("Your order will be ready in " + str(round(order_finish_time / 60, 2)) + " hours.")
    # This is here I use order_finish_time. I divide it by 60, and round it t to
    # 2 decimal places to give me the approximate amount of hours it takes to prepare the
    # order
    print("Please pay upon recieving the order.")
    print("\nThank you for dining at Escape from New York Pizzeria. Please come again another time.")

# Two different statements, depending on wether the user ordered soemthing or not
# I check if they ordered something or not using len(order) == 0