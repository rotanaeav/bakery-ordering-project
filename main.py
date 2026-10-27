import sys


def order_items(sub_total):
    bakeries = [
        {"name": "Croissant", "price": 5.00},
        {"name": "Chocolate Muffin", "price": 2.50},
        {"name": "Bread", "price": 2.00},
        {"name": "Bagel", "price": 1.00},
        {"name": "Bun", "price": 1.50},
    ]
    # for b in bakeries:
    for b in range(len(bakeries)):
        print(f"{b + 1}. {bakeries[b]['name']:<24} {bakeries[b]['price']}$")
    try:
        select = int(input("Select an items: "))
        if select - 1 in range(len(bakeries)):
            sub_total += bakeries[select - 1]['price']
            # sub_total =bakeries[select-1]['price'] if 0 else +bakeries[select-1]['price']
            print("--------------------------------")
            print(bakeries[select - 1]['name'], "added successfully!!")
            print("Current Sub-Total : ", sub_total)
        else:
            print("Invalid choice! Please try again!")
    except:
        print("Invalid number! Please try again!")
    return sub_total


def view_total(sub_total):
    print("""
================================
[+]        Order Total       [+]
================================
    """)
    if sub_total == 0:
        print('[!] No items added!')
    else:
        print(f"Current Sub-Total: {sub_total}$")
    press_enter()


def payment(sub_total):
    cash = float(input('Enter your cash: '))
    print("""
================================
[+]          PAYMENT         [+]
================================
        """)
    if cash <=0:
        print('[!] Please enter a positive cash!')
        return False
    if cash < sub_total:
        print('You need ', sub_total - cash, "$ more!")
        return False
    if cash >= sub_total:
        print(f"{"Total:":<27}{sub_total:.2f}$")
        print(f"{'Cash:':<27}{cash:.2f}$")
        print("--------------------------------")
        print(f"{'Change:':<27}{cash - sub_total:.2f}$")
        print("[*] Payment Successful! ")
        return True


def checkout(sub_total):
    discount = 0.00
    print("""
================================
[+]         CHECKOUT         [+]
================================
    """)
    if sub_total == 0:
        print('[!] No items added!')
        print('[!] Please add items first!')
        return False

    print(f"{"Sub-Total:":<26}{sub_total:.2f}$")
    if sub_total >= 10:
        discount = sub_total * 10 / 100
        sub_total -= discount
    print(f"{"Discount:":<27}{discount:.2f}$")
    print("--------------------------------")
    print(f"{"Total:":<27}{sub_total:.2f}$")
    paid = payment(sub_total)
    press_enter()
    return paid


def press_enter():
    input("\n[~] Press enter to continue [~]")
    # os.system("clear")


sub_total = 0.00
is_running = True
while is_running:
    print("""
================================
[+] WELCOME TO BAKERY SYSTEM [+]
================================
1. Order Items
2. View Total
3. Checkout
4. Exit
================================
    """)
    try:
        opt = int(input("Enter your choice: "))
        match opt:
            case 1:
                sub_total = order_items(sub_total)
                press_enter()
            case 2:
                view_total(sub_total)

            case 3:
                if checkout(sub_total):
                    sub_total = 0.00

            case 4:
                print('Thank you ! Good Bye!')
                is_running = False
                # sys.exit()
            case _:
                print("Invalid choice! Please try again!")
    except ValueError:
        print("Invalid number! Please try again!")
