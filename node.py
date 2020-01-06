#class node
#has string and function for getting next node
from InvalidResponseError import InvalidResponseError
from abc import ABC

class Node(ABC):
    def __init__(self, label, nextNodes):
        self.nextNodes = nextNodes
        self.label = label

    def getNextNode(self, response):
        pass
    
    def isDiagnosisNode(self):
        return len(self.nextNodes) == 0
    
    def getPrompt(self):
        return self.label