# Importing libraries
import psycopg2
import Functions

# The password to acess the PostgreSQL
password = input("Password: ")

# The First Steps
try:
    connecting = psycopg2.connect(database = "cafe_db", host = "localhost", user = "postgres", password = password, port = "5432")
    
except:
    print("That isn't the password.")

else:
    cursor = connecting.cursor()
    #Functions.Test(cursor, connecting)
    
    # Calling functions from library Functions
    Functions.ToLogo()
    Functions.ToOptions()
    Functions.ToChoose(cursor, connecting)