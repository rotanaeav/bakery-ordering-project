import sys

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
opt = int(input("Enter your choice: " ))
match opt:
    case 1:
        print("Order Items")
    case 2:
        print("View Total")
    case 3:
        print("Checkout")
    case 4:
        sys.exit()
    case _ :
        print("Exit")

