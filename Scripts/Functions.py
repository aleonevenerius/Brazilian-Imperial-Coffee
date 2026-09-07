import psycopg2
#                           The main function of the system
# To create the system's initail home
def ToLogo():
    h = open("C:\\DB\\Cafe\\Scripts\\Logo.txt")
    print(h.read())
    
# To create the system's home options
def ToOptions():
    o =  open("C:\\DB\\Cafe\\Scripts\\Options.txt")
    print(o.read())

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
            
# The next choose afterwards the "Initial home"
def ToChoose():
    labour = True
    while labour:
        choose = int(input("Which shall we select?\n> "))
        match choose:
            case 1:
                print("Creating a new order...")
            case 2:
                print("Consulting")
            case 3:
                print("Consult product")
            case 4:
                print("Registering")
            case 5:
                labour = False
                print("Out...")