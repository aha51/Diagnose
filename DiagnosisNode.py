#diagnosis node

from node import Node

class DiagnosisNode(Node):
    def __init__(self, label):
        Node.__init__(self, label, [])
        
    