#option node
#takes user input and decides next node
from node import Node

class OptionNode(Node):
    def __init__(self, label, nextNodes):
        Node.__init__(self, label, nextNodes)
        