from pykkar import *
from time import *
create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

def left():
    for i in range(3):
        right()

        
def parem():
    for i in range(3):
        sleep(1)
        left()
parem()
