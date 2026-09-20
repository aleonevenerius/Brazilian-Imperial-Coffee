import time

#                           The main message
error_menssage = "There is an error. Please, try again"
incorrect_value = "Incorrect value. Please, try again."
ok = "Done!"
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
    print("Done!")
    time.sleep(1)
    
# It create order
def ToCreateOrder(cursor, connecting):
    while True:
        try:
            # Variables about client and order
            order = int(input("What is your order?: "))
        except:
            print(error_menssage)
        else:
            str(order)
            client_name = input("What is your name?:")
            try:
                cursor.execute(
                """
                INSERT INTO db_order(order_circumstance, client_name, client_order)
                VALUES(%s, %s, %s)
                """,('Making', client_name, order))
            except:
                print(error_menssage)
            else:
                connecting.commit()
                break
    ToTime()
    
# It changes the cirumstances of order
def ToChangeCircumstances(cursor, connecting):
    while True:
        try:
            client_order_code = input('Order code: ')
        except ValueError:
            print(incorrect_value)
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
def ToConsultOrder(cursor, connecting):
    def OneOrder(cursor, connecting):
        number_order = input("What's the number of order?\n> ")
        cursor.execute('SELECT * FROM db_order WHERE code_order = '+ number_order)
        order = cursor.fetchall()
        if order == []:
            print("There is no that order.")
        else:
            print(order[0][0:4])
            ToTime()
        
    def AllOrders(cursor, connecting):
        cursor.execute("SELECT * FROM db_order")
        all_orders = cursor.fetchall()
        size = len(all_orders)
        i = 0
        while True:
            if i == (size-1):
                break
            else:
                print(all_orders[i])
                i += 1
     
    while True:
        try:
            type_order = int(input("What do you wish?\n1 - Consult solely one order\n2 - Consult all orders\n3 - Exit\n> "))
        except ValueError:
            print("There is no this option. Please, try again.")
        else:
            if 1 == type_order:
                OneOrder(cursor, connecting)
            elif 2 == type_order:
                AllOrders(cursor, connecting)
            elif 3 == type_order:
                break
            else:
                print("There is no this option. Please, try again.")

# It checks the products
def ToConsultProducts(cursor, connecting):
    j = 0
    while True:
        try:
            category_product = input("What is the category of product?\n> ")
            cursor.execute("SELECT * FROM db_products WHERE category = '"+category_product+"'")
        except:
            print(incorrect_value)
        else:
            products = cursor.fetchall()
            size = len(products)
            while True:
                if j == (size-1):
                    break
                else:
                    try:
                        print(products[j][0:3])
                    except:
                        print("Error!")
                        j = size-1
                    else:
                        j += 1
            break

    
# It registers a product
def ToRegisterProduct(cursor, connecting):
    while True:
        name_product = input("What is the name of the new product?: ")
        category_product = input("What is the product's category? Coffee, Cake, Candy, Drink?\n> ")                
        try:
            price_product = float(input("What is the price of its?: "))
        except ValueError:
            print(incorrect_value)
        else:
            cursor.execute(
            """
            INSERT INTO db_products(name_products, category, price)
            VALUES(%s, %s, %s)
            """, (name_product, category_product, price_product))
            connecting.commit()
            print(ok)
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
            print(ok)
            break
    ToTime()

# The next choose afterwards the "Initial home"
def ToChoose(cursor, connecting):
    while True:
        try:
            choose = int(input("Which shall we select?\n> "))
        except ValueError:
            print(incorrect_value)
        else:
            match choose:
                case 1:
                    ToCreateOrder(cursor, connecting)
                    ToOptions()
                case 2:
                    ToChangeCircumstances(cursor, connecting)
                    ToOptions()
                case 3:
                    ToConsultOrder(cursor, connecting)
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