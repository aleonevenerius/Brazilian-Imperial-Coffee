#                           The main function of the system
# It creates the system's logo
def ToLogo():
    h = open("C:\\DB\\Cafe\\Scripts\\Logo.txt")
    print(h.read())
    
# It creates the system's home options
def ToOptions():
    o =  open("C:\\DB\\Cafe\\Scripts\\Options.txt")
    print(o.read())

# It create order
def ToCreateOrder(cursor, connecting):
    working = True
    while working:
        try:
            # Variables about client and order
            order = int(input("What is your order?: "))
            
        except ValueError:
            print("The order must be an int number!")
        else:
            client_name = input("What is your name?:")
            cursor.execute(
            """
            INSERT INTO db_order(order_circumstance, client_name, client_order)
            VALUES(%s, %s, %s)
            """,
            ('Making', client_name, order))
            connecting.commit()
            working = False

# It changes the cirumstances of order
def ToShiftCircumstances():
    print("Changing")

# It consults the orders
def ToConsultOrder(cursor):
    cursor.execute('SELECT * FROM db_order')
    print(cursor.fetchall())
    
# It checks the products
def ToConsultProducts(cursor):
    cursor.execute('SELECT * FROM db_products')
    print(cursor.fetchall())

# It registers a product
def ToRegisterProduct(cursor, connecting):
    labour = True
    while labour:
        name_product = input("What is the name of the new product?: ")
        category_product = input("What is the product's category? Coffee, Cake, Candy, Drink?\n> ")        
        try:
            price_product = float(input("What is the price of its?: "))
        except ValueError:
            print("This value isn't acceptable.")
        else:
            cursor.execute(
            """
            INSERT INTO db_products(name_products, category, price)
            VALUES(%s, %s, %s)
            """, (name_product, category_product, price_product))
            connecting.commit()
            print("It was created properly!")
            labour = False
        
# The next choose afterwards the "Initial home"
def ToChoose(cursor, connecting):
    labour = True
    while labour:
        try:
            choose = int(input("Which shall we select?\n> "))
        except ValueError:
            print("Incorrect value! Please, try again.")
        else:
            match choose:
                case 1:
                    ToCreateOrder(cursor, connecting)
                    ToOptions()
                case 2:
                    ToShiftCircumstances()
                    ToOptions()
                case 3:
                    ToConsultOrder(cursor)
                    ToOptions()
                case 4:
                    ToConsultProducts(cursor)
                    ToOptions()
                case 5:
                    ToRegisterProduct(cursor, connecting)
                    ToOptions()
                case 6:
                    print("Deleting...")
                case 7:
                    labour = False
                    print("Turning off.")