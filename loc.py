#loss of conciousness algorithm
from OptionNode import OptionNode
from Algorithm import Algorithm
from DiagnosisNode import DiagnosisNode


def main():
    
    #diagnosis nodes
    concussion = DiagnosisNode("You have a concussion")
    seizure = DiagnosisNode("You've had a seizure")
    metabolic = DiagnosisNode("You have a metabolic derangement")
    intoxication = DiagnosisNode("You are intoxicated")
    idiopathic = DiagnosisNode("The cause is unknown")

    #questions as option nodes
    intoxicatedQ = OptionNode("Intoxicated?", {'yes': intoxication, 'no': idiopathic})
    metabolicQ = OptionNode("Metabolic derangement?", {'yes': metabolic, 'no': intoxicatedQ})
    confusionQ = OptionNode("Confusion?", {'yes': seizure, 'no': metabolicQ})
    traumaQ = OptionNode("Trauma?", {'yes': concussion, 'no': confusionQ})
    
    
    

    loc = Algorithm(traumaQ)
    loc.runAlgorithm()
    
if __name__ == "__main__":
    main()
