import psycopg2

connecting = psycopg2.connect(database = "cafe_db", host = "localhost", user = "postgres", password = "7898", port = "5432")
cursor = connecting.cursor()

try:
    # Variables about client and order
    order = int(input("What is your order?: "))
    client_name = input("What is your name?:")

except ValueError:
    print("There is not that order.")

else:
    pass

def ToHome():
    h = open("C:\\DB\\Cafe\\Scripts\\Home.txt")
    print(h.read())

def ToShowOrder():
    cursor.execute('SELECT * FROM db_order')
    print(cursor.fetchall())
    
def ToShowCafeProducts():
    cursor.execute('SELECT * FROM db_products')
    print(cursor.fetchall())
    
def ToCreateOrder():
        #cursor.execute("INSERT INTO db_order(order_circumstance, client_name, client_order)")
        cursor.execute(f"VALUES('Making', '{client_name}', {order})")

ToHome()
ToCreateOrder()