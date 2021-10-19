from utilitaire import *
import cProfile
import re

def calculateConfigValue_naiveVersion(config) :    
    """
        Calcule la valeur de la configuration 'config' de manière naive
        :param:
        config : list Liste formé du plateau de jeu (liste) et du symbole du joueur qui doit joueur [board, player]
        return : int Valeur de la configuration
    """
    successors = list(getSuccessors(config))
    values = list()
    
    if len(successors) == 0:
        return 0
    
    for successor in successors :
        value = calculateConfigValue_naiveVersion(successor)
        values.append( value )
        
    if 0 in values:
        return 1
    elif allPositive(values):
        return -(max(values)+1)
    else :
        return -(  max(extractNegativeValues(values))  -1 )
    


if __name__ == "__main__":
    board = list()
    nbLines=input()
    nbColumns=input()

    for i in range(int(nbLines)):
        line = list(input())
        assert len(line) == (int(nbColumns))
        board.append(line)
        
    """print("Plateau \n")
    for i in board:
        print(str(board.index(i)) + " " +str(i) + " \n")
     """
    
    print(str(calculateConfigValue_naiveVersion([board, whitePawnSymbol])))
cProfile.run('re.compile("config")')