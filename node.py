#class node
#has string and function for getting next node
from InvalidResponseError import InvalidResponseError
class Node:
    def __init__(self, label, nextNodes):
        self.nextNodes = nextNodes
        self.label = label

    def getNextNode(self, response):
        if response in self.nextNodes:
            return self.nextNodes[response]
        raise InvalidResponseError("This is an invalid response")
    
    def isDiagnosisNode(self):
        return len(self.nextNodes) == 0
    
    def getPrompt(self):
        return self.label