

class BackTrackingAlgorithm:
    
    #Constructor
    def __init__(self, queens,printer):
        self.__queens = queens
        self.__numberSolutions = 0
        self.__printer=printer
        self.__run()
    #Run the process
    def __run(self):
        places = [-1] * self.__queens
        self.__insertQueen(places, 0)
        self.__printer.printNumberSolutions(self.__numberSolutions)
    # back tracking for resolve the problem
    def __insertQueen(self, places, attackRow):
        # Stop if all rows are used
        if attackRow == self.__queens:
            self.__numberSolutions += 1
            self.__printer.run(places,self.__numberSolutions)
        else:
            # Iterate all Columns, trying to insert a queen
            for column in range(self.__queens):
                # discard invalid columns
                if self.__validatePlace(places, attackRow, column):
                    places[attackRow] = column
                    self.__insertQueen(places, attackRow + 1)

    # Here we check if there is an attack of the anothers queens
    def __validatePlace(self, places, usedRows, column):
        for i in range(usedRows):
            if places[i] == column or \
                places[i] - i == column - usedRows or \
                places[i] + i == column + usedRows:
                return False
        return True
