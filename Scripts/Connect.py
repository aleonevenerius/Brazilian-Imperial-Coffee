import psycopg2

connecting = psycopg2.connect(database = "cafe_db", host = "localhost", user = "postgres", password = "7898", port = "5432")
   
print(connecting.info)
print(connecting.status)
cursor = connecting.cursor()
cursor.execute('SELECT * FROM db_order')
print(cursor.fetchall())