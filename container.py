
import backtrackingAlgorithm as algorithm
import printer as printer
import readYaml as yamlFile
import storage as dbStorage

class Container:
    #Constructor
    def __init__(self,queens,toPrint):
        self.__queens=queens
        self.__print=toPrint

    def run(self):
        #First let's read our config file, in this case a yaml file
        yaml= yamlFile.ReadYaml()
        #Initialization of storage class, passing the configuration
        storage=dbStorage.Storage(yaml)
        #Finally , print the solution
        myPrinter= printer.Printer(self.__queens,storage,self.__print)
        #Initialization of the Genetic algorithm for seeking the solution
        backtracking= algorithm.BackTrackingAlgorithm(self.__queens,myPrinter)


        


        
