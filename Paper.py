# Markhus Dammar
# 3/10/2020
# This is the paper company 'driver' prog

from SQ import Stack
import time

qty = Stack()
price = Stack()
total_qty = 0


def menu():
    print("""
    PAPER COMPANY -- MAIN MENU:
    1. Add to Inventory
    2. Sell Paper
    3. Show Profits
    4. Show Total Inventory
    5. Exit()
    """)


menu()
choice = int(input("Which would you like to do? >>> "))

if choice == 1:
    qty_input = int(input("How many boxes of paper would you like to order? >>> "))  # takes user input for amt ordered
    print(f"{qty_input} boxes will be ordered.")
    total_qty = total_qty + qty_input
    qty.push(qty_input)
    price_input = int(input("What is the price per box of paper? >>> $"))
    price.push(price_input)
    time.sleep(1)
    total_price = qty_input * price_input
    print(f"""\nORDER CONFIRMED:
             {qty_input} boxes of paper @ ${price_input} per box.
             This totals to ${total_price}.""")
    time.sleep(5)
    menu()
    choice = int(input("Which would you like to do? >>> "))

if choice == 2:
    print(f"We have {total_qty} boxes of paper in stock.")
    box_sold = int(input("How many boxes of paper are we going to sell? >>> "))
    recommended = price_input + (price_input * .1)
    dealer = float(input(f"""How much will we sell each box for?
    We need to make a 10% profit. The last order was ${price_input} per box.
    I recommend selling each box for ${recommended}
        >>> $"""))
    profit = total_price - (dealer * box_sold)
    gross_cost = dealer * box_sold
    print(f"""Okay, so we're selling {box_sold} boxes at ${dealer} per box.
    This equates to ${gross_cost} altogether, with a ${profit} profit.""")
    total_qty = total_qty - box_sold
    time.sleep(5)
    menu()
    choice = int(input("Which would you like to do? >>> "))

if choice == 3:
    print(f"""PROFITS
          Currently, we have made ${profit}""")
    time.sleep(5)
    menu()
    choice = int(input("Which would you like to do? >>> "))

if choice == 4:
    print(f"""INVENTORY
            We have a total of {total_qty} boxes of paper in stock.""")
    time.sleep(5)
    menu()
    choice = int(input("Which would you like to do? >>> "))

if choice == 5:
    print("Goodbye, user. Remember to clock out, because we won't pay you for overtime")
    time.sleep(5)
    exit()
#while choice < 1 or choice > 5:
   # menu()


