#option node
#takes user input and decides next node when there are categorical, non-numerically derived options
from node import Node

class OptionNode(Node):
    def __init__(self, label, nextNodes):
        Node.__init__(self, label, nextNodes)
    
    def getNextNode(self, response):
        if response in self.nextNodes:
            return self.nextNodes[response]
        raise InvalidResponseError("This is an invalid response")