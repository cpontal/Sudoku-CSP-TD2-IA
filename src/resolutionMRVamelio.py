import SudokuGrid
import numpy as np

#Fonction de backtracking idiot
def backtracking(g):
    #Cherche le prochain vide:
    r,c = NextEmpty(g.grid)
    if r == -1: #Le sudoku est terminé
        return True
    else:
        for val in range(1,10):
            if g.grid[r][c].binCondition[val-1]:
                g.defineValue(r,c,val)
                if backtracking(g):
                    return True
                g.defineValue(r,c,0)
        return False

def backtrackingMRV(g):
    #Cherche le prochain vide:
    r,c = NextEmptyMRV(g.grid)
    if r == -1: #Le sudoku est terminé
        return True
    else:
        for val in range(1,10):
            if g.grid[r][c].binCondition[val-1]:
                g.defineValue(r,c,val)
                if backtrackingMRV(g):
                    return True
                g.defineValue(r,c,0)
        return False  

def NextEmptyMRV(grid):
    gridPoss = gridNumPossibility(grid)
    if gridPoss.any() != np.zeros((9,9)).any():
        min = np.min(gridPoss[np.nonzero(gridPoss)])
        for row in range(9):
            for col in range(9):
                if  gridPoss[row, col] == min:
                    return row, col
    return NextEmpty(grid) # Si il y a encore des cases vides mais sans solution

def gridNumPossibility(grid): #Retourne le nombre de possibilité (en valeur) pour chaque case
    gridNum = np.zeros((9,9))
    for row in range(9):
        for col in range(9):
                gridNum[row,col] = sum(grid[row][col].binCondition)
    return gridNum

def NextEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col].value == 0:
                return row, col
    return -1,-1    
#def isPossible(grid, row, col, val):
    
    # Meme num sur la ligne
    for x in range(9):
        if grid[row][x].value == val:
            return False

    # Meme num sur la colonne
    for x in range(9):
        if grid[x][col].value == val:
            return False
    
    # Meme num sur la sous matrice
    subRow = row - row % 3
    subCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + subRow][j + subCol].value == val:
                return False
    
    # Le chiffre est possible
    return True



g = SudokuGrid.SudokuGrid()
g.printGridTerminal()

backtracking(g)
g.printGridTerminal()
