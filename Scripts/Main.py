import psycopg2
p = input("Password: ")

connecting = psycopg2.connect(database = "cafe_db", host = "localhost", user = "postgres", password = p, port = "5432")
cursor = connecting.cursor()

def ToHome():
    h = open("C:\\DB\\Cafe\\Scripts\\Home.txt")
    print(h.read())

ToHome()

try:
    # Variables about client and order
    order = int(input("What is your order?: "))
    client_name = input("What is your name?:")

except ValueError:
    print("There is not that order.")

else:
    pass

# The main function of the system
def ToShowOrder():
    cursor.execute('SELECT * FROM db_order')
    print(cursor.fetchall())
def ToShowCafeProducts():
    cursor.execute('SELECT * FROM db_products')
    print(cursor.fetchall())
def ToCreateOrder():
    cursor.execute(
    """
    INSERT INTO db_order(order_circumstance, client_name, client_order)
    VALUES(%s, %s, %s)
    """,
    ('Making', client_name, order))
    connecting.commit()
    ToShowOrder()

ToCreateOrder()
