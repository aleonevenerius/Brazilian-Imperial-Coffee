import time

#                           The main function of the system
# It creates the system's logo
def ToLogo():
    h = open("C:\\DB\\Cafe\\Scripts\\Logo.txt")
    print(h.read())
    
# It creates the system's home options
def ToOptions():
    o =  open("C:\\DB\\Cafe\\Scripts\\Options.txt")
    print(o.read())

def ToTime():
    icons = ["|", "/", "-", "\\", "|"]
    i = 0
    while i < 5:
        print(f"\rLoading {icons[i%len(icons)]}", end="", flush=True)
        i += 1
        time.sleep(0.1)

    print("\nDone!")
    time.sleep(1)
    
# It create order
def ToCreateOrder(cursor, connecting):
    while True:
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
            break
    ToTime()
    
# It changes the cirumstances of order
def ToChangeCircumstances(cursor, connecting):
    while True:
        try:
            client_order_code = int(input('Order code: '))
        except ValueError:
            print("Incorrect value. Please, try again.")
        else:
            client_order_code = str(client_order_code)
            cursor.execute(
            """
            UPDATE db_order
            SET order_circumstance = 'Done'
            WHERE code_order = %s
            """, (client_order_code,))
            connecting.commit()
            print("Done!")
            break
    ToTime()
    
# It consults the orders
def ToConsultOrder(cursor):
    number_order = input("What's the number of order?\n> ")
    cursor.execute('SELECT * FROM db_order WHERE code_order = '+ number_order)
    print(cursor.fetchall())
    ToTime()
    
# It checks the products
def ToConsultProducts(cursor, connecting):
    j = 0
    while True:
        try:
            category_product = input("What is the category of product?\n> ")
            cursor.execute("SELECT * FROM db_products WHERE category = '"+category_product+"'")
        except:
            print("Incorrect value. Please, try again.")
        else:
            products = cursor.fetchall()
            size = len(products)
            print(size)
            while True:
                if j == (size-1):
                    break
                else:
                    print(products[j][0:3])
                    j += 1
            break
    ToTime()
    
# It registers a product
def ToRegisterProduct(cursor, connecting):
    while True:
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
            break
    ToTime()
    
def ToDeleteOrder(cursor, connecting):
    while True:
        try:
            code_order_client = int(input("Order code: "))
        except ValueError:
            print("Incorrect value. Try again, please.")
        else:
            code_order_client = str(code_order_client)
            cursor.execute(
            """
            DELETE FROM db_order
            WHERE code_order = %s;
            """, (code_order_client))
            connecting.commit()
            print("Done!")
            break
    ToTime()

# The next choose afterwards the "Initial home"
def ToChoose(cursor, connecting):
    while True:
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
                    ToChangeCircumstances(cursor, connecting)
                    ToOptions()
                case 3:
                    ToConsultOrder(cursor)
                    ToOptions()
                case 4:
                    ToConsultProducts(cursor, connecting)
                    ToOptions()
                case 5:
                    ToRegisterProduct(cursor, connecting)
                    ToOptions()
                case 6:
                    ToDeleteOrder(cursor, connecting)
                case 7:
                    break
'''
def Test(cursor, connecting):
    cursor.execute("SELECT * FROM db_order")    
    db = cursor.fetchall()
    print(type(db)) # list
    print(len(db)) # 15 tuples into one list
    print(db[0][0:4]) 
'''