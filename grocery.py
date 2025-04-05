import csv

grocery_list = {}
with open('grocery.csv', 'r') as file:
        list = csv.reader(file)

        for row in list:
            grocery_list[row[0]] = [row[1], row[2],row[3], row[4]]

def main():
    customer_list = {}
    account = ["admin","admin123"]
    while True:
        print("=" * 30)
        print("Grocery Store System Management")
        print("=" * 30)
        print("1. Guest")
        print("2. Admin")
        print("3. Exit")
        choose = int(input("Choose a number: "))    
        if choose == 1:
            name = input("Enter your name: ")
            money = float(input("Enter your budget: "))
            customer_list[name] = [money]
            menu()
        elif choose == 2:
            try:
                user = input("Enter admin username: ")
                password = input("Enter admin password: ")
                
                if user == account[0] and password == account[1]:
                    print("Login successful!")
                    admin_management()
                else:
                    print("Invalid password. Please try again!")
            except KeyError:
                print("invalid username input. Please try again!")
        elif choose == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please try again.")
            
            
def admin_management():
    while True:
        print("=" * 30)
        print("Grocery Store System Management")
        print("=" * 30)
        print("\n1. View Products")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Logout\n")
        print("-" * 30)
        
        option = input("Enter a number to choose: ")
        
        if option == "1":
            display_products(grocery_list)
        
        elif option == "2":
            number = input("Enter a number: ")
            name = input("Enter product name: ")
            quantity = input("Enter product quantity: ")
            price = input("Enter product price: ")
            stock = input("Enter product stock: ")
            add_item(number,name,quantity,price,stock)
        elif option == "3":
            remove_item()        
        elif option == "4":
            print("You are now logged out.")
            break
        else:
            print("Invalid choices")                                
def menu():    
    while True:
        print("=" * 30)
        print("Grocery Store System Management")
        print("=" * 30)
        print("\n1. View Products")
        print("2. Add Cart")
        print("3. Exit\n")
        print("-" * 30)
        
        option = input("Enter a number to choose: ")
        
        if option == "1":
            display_products(grocery_list)
        
        elif option == "2":
            add_cart()
        
        elif option == "3":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choices")
            
def display_products(grocery_list):
    print(f"Number        Product               Quantity                 Price               Stock")
    for item in grocery_list:
        gro = grocery_list[item]
        print(f"{item}             {gro[0]:<15}       {gro[1]:<10}              {gro[2]:<7}             {gro[3]:<5}")
        
def add_item(number,name,quantity,price,stock):
    grocery_list[number] = [name, quantity,price,stock]
    with open('grocery.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number, name, quantity, price, stock])

def add_cart():
    pass

def remove_item():
    pass

    
main()