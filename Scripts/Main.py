#import Order
from Connect import *

def ToHome():
    h = open("C:\\DB\\Cafe\\Scripts\\Home.txt")
    print(h.read())
    
ToHome()