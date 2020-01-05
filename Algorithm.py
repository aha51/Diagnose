#Algorithm class
from node import Node
from InvalidResponseError import InvalidResponseError

class Algorithm:
    def __init__(self, firstOptionNode):
        self.firstOptionNode = firstOptionNode
    
    def runAlgorithm(self):
        currentNode = self.firstOptionNode
        while not currentNode.isDiagnosisNode():
            try:
                userResponse = input(currentNode.getPrompt())
                currentNode = currentNode.getNextNode(userResponse)
            except InvalidResponseError:
                print("Sorry I didn't understand that...")
                
        print(currentNode.getPrompt()) 
    