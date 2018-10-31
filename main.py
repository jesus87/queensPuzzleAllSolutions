#Author: Jesus Garcia Flores
# Eight Queens Puzzle Find All Solutions
#   The solution was made it using BackTracking Algorithm
#   Storage was made it using SQLAlchemy
#Resources: 
# BackTracking Algortihm:  https://www.ecured.cu/Vuelta_atr%C3%A1s_(backtracking)
# BackTracking Algortihm :  https://en.wikipedia.org/wiki/Backtracking
# SqlAlchemy, How to Create and Insert data in postgress with sqlalchemy https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
#Dependencies:
#   Dependencies for this project were added on requierements.txt
#############################################################################


import container as container
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False
def askOptPrint():
    inputFromBoard = input('Would you like to print results? Y|N: ')
    try:
        
        _value=str(inputFromBoard)
        _value= _value.upper()
        if _value == "Y":
            return True
        if _value == "N":
            return False
        askOptPrint();
        
    except ValueError:
         print('Please type Y|N')    
         askOptPrint()

if __name__ == "__main__":
    inputFromBoard = input('Please Type the Numbers of Board/Queens: ')
    numberOfQueens,ok=intTryParse(inputFromBoard)
    if ok:
        print('We are working on ', numberOfQueens, ' Queens')
        toPrint = askOptPrint()
        _container= container.Container(numberOfQueens,toPrint)
        _container.run()
    else:
        print('Please type a correct Int Number')    

