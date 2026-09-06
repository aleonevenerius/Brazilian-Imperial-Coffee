import psycopg2

connecting = psycopg2.connect(database = "cafe_db", host = "localhost", user = "postgres", password = "7898", port = "5432")
   
#print(connecting.info)
#print(connecting.status)

cursor = connecting.cursor()

def ToShowOrder():
    cursor.execute('SELECT * FROM db_order')
    print(cursor.fetchall())
    
def ToShowCafeProducts():
    cursor.execute('SELECT * FROM db_products')
    print(cursor.fetchall())
    
def ToCreateOrder():
    print("Creating...")