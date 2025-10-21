import random
from main import BSTNode
from user import *
#from ref import *

test_vals = [
        12, 23, 6, 98, 14
        ]

def test():
    node = BSTNode(0)
    for i in range(0, len(test_vals)):
        node.insert(test_vals[i])

test()
