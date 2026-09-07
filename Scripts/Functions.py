import psycopg2
    
#                           The main function of the system
# To create the system's initail home
def ToInitialHome():
    h = open("C:\\DB\\Cafe\\Scripts\\HomeInitial.txt")
    print(h.read())

# To consult orders
def ToConsultOrder():
    cursor.execute('SELECT * FROM db_order')
    print(cursor.fetchall())
    
# To consult products
def ToConsultProducts():
    cursor.execute('SELECT * FROM db_products')
    print(cursor.fetchall())

# To create order
def ToCreateOrder():
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
            ToShowOrder()