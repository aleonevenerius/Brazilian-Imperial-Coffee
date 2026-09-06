import Connect

# Variables about client and order
try:
    order = int(input("What is your order?: "))
    client_name = input("What is your name?:")
except ValueError:
    print("There is not that order.")
else:
    pass