from sqlalchemy import create_engine


class Storage:
    #Constructor
    def __init__(self,readYaml):
        self.__dbString="postgres://"+readYaml.user+":"+readYaml.password+"@"+readYaml.host+":"+readYaml.port+"/"+readYaml.dbName
        self.__db=create_engine(self.__dbString)
        self.__createTable()
        self.__deleteTable()
     #if table does not exist , we create it
    def __createTable(self):
        self.__db.execute("CREATE TABLE IF NOT EXISTS solution (queens integer, solutions integer, numbersolution integer,shortsolution text,solution text,runedat timestamp with time zone DEFAULT now())")  
    #clean table solution
    def __deleteTable(self):
        self.__db.execute("delete from solution")
    #insert the values on postgress
    def insert(self,queens,solutions,idsolution,shortSolution,solution):
    
        self.__db.execute("INSERT INTO solution (queens, solutions,numbersolution, shortsolution,solution) VALUES ("+str(queens)
        +","+str(solutions)+","+str(idsolution)+", '"+str(shortSolution)+"','"+str(solution)+"')")
     #update the number of solutions founded
    def updateNumberSolutions(self,nSolutions):
        self.__db.execute("UPDATE  solution set solutions= "
        +str(nSolutions))