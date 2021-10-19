from utilitaire import *
import cProfile
import re



memorizedConfigs = {}
    
def calculateConfigValue_dynamiqueVersion(config) :
    """
        Calcule la valeur de la configuration 'config' de maniere dynamique
        :param:
        config : list Liste formé du plateau de jeu (liste) et du symbole du joueur qui doit joueur [board, player]
        return : int Valeur de la configuration
    """
    currentConfigValue = 0
    successorsValues = list()
    
    # On convertie la configuration en chaine de caractere
    strBoard = ""
    for line in config[0]:
        strBoard += ''.join(line) 
    strPlayer = config[1]
    strConfig = strBoard+strPlayer
    
    # On verifie qu'on a pas déjà calculé la valeur de la configuration actuelle
    if strConfig in memorizedConfigs:
        return memorizedConfigs[strConfig]
    
    successors = list( getSuccessors(config) )
    
    # Si on n'a pas de coup possible, alors le joueur actuel a perdu
    if len(successors) == 0:
        return 0
    
    for successor in successors :
        successorValue = calculateConfigValue_dynamiqueVersion( successor )
        successorsValues.append( successorValue )
        
    if 0 in successorsValues:
        currentConfigValue = 1
    elif allPositive(successorsValues):
        currentConfigValue =  -( max(successorsValues)+1 )
    else :
        currentConfigValue = -(  max(extractNegativeValues(successorsValues))-1 )
    
    # On mémorise la configuration actuelle avec sa valeur    
    memorizedConfigs[strConfig] = currentConfigValue
    
    return currentConfigValue


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
    "print(str(calculateConfigValue_dynamiqueVersion([board, whitePawnSymbol])))"
    cProfile.run('print(str(calculateConfigValue_dynamiqueVersion([board, whitePawnSymbol])))')
