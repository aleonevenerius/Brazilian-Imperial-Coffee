# Importing libraries
import psycopg2
from Functions import *
import Functions

# The password to acess the PostgreSQL
password = input("Password: ")
# The main variable which will control the main loop
labour = True

# The First Steps
try:
    connecting = psycopg2.connect(database = "cafe_db", host = "localhost", user = "postgres", password = password, port = "5432")

except:
    print("That isn't the password.")

else:
    cursor = connecting.cursor()
    ToLogo()
    ToOptions()
    ToChoose()