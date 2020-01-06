#value node
#takes user numerical input and decides which is the next node
from node import Node

class ValueNode(Node):
    
    #nextNodes takes a dict with bounds that the program will use
    def __init__(self, label, nextNodes):
        self.__init__(self, label, nextNodes)
    
    def getNextNode(self, response):
        keys = nextNodes.keys()
        for i in keys:
            if response > keys[i] & response < keys[i + 1]:
                return nextNodes[keys[i]]