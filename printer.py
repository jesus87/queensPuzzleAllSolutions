
class Printer:
    #   Constructor
    def __init__(self,queens,storage,toPrint):
        self.__storage=storage
        self.__queens= queens
        self.__currentSolution=""
        self.__shortSolution=""
        self.__print=toPrint
    # run the process
    def run(self,places,number):
        self.__currentSolution=""
        self.__printMovs(places,number)
        self.__shortMovs(places,number)
        self.__storage.insert(self.__queens,0,number,self.__shortSolution,self.__currentSolution)
    #here print the solution
    def __printMovs(self,places,number):
        
        for row in range(self.__queens):
            toDataBase = ""
            for column in range(self.__queens):
                if places[row] == column:
                    toDataBase += "1 "
                else:
                    toDataBase += "0 "
            self.__currentSolution+=toDataBase+"\n" 
        if self.__print:
            print ("Solution #"+str(number))
            print (self.__currentSolution)
        
    #here print the short solution (positions)
    def __shortMovs(self, places,number):
        line = ""
        for i in range(self.__queens):
            line += str(places[i]) + " "
        self.__shortSolution=line
        if self.__print:
            print ("Short Solution #"+str(number))
            print(self.__shortSolution)
            print("\n")
    #print the number of solutions
    def printNumberSolutions(self,numberSolutions):
        self.__storage.updateNumberSolutions(numberSolutions)
        if self.__print:
            print("The Numbers of Solutions for ",self.__queens," Queens is: ", numberSolutions)
          