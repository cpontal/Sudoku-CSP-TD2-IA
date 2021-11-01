import SudokuGrid
import numpy as np

#Fonction de backtracking idiot
def backtracking(sudoku, nbIte = 1):
    #Cherche le prochain vide:
    r,c = NextEmpty(sudoku.grid)
    if r == -1: #Le sudoku est terminé
        print(nbIte)
        return True
    else:
        for val in range(1,10):
            if sudoku.grid[r][c].binCondition[val-1]:
                sudoku.defineValue(r,c,val)
                if backtracking(sudoku, nbIte + 1):
                    return True
                sudoku.defineValue(r,c,0)
        return False

def backtrackingMRV(sudoku, nbIte = 1):
    #Cherche le prochain vide:
    r,c = NextEmptyMRV(sudoku.grid)
    if r == -1: #Le sudoku est terminé
        print(nbIte)
        return True
    else:
        for val in range(1,10):
            if sudoku.grid[r][c].binCondition[val-1]:
                sudoku.defineValue(r,c,val)
                if backtrackingMRV(sudoku, nbIte + 1):
                    return True
                sudoku.defineValue(r,c,0)
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
            if grid[row][col].value == 0:
                gridNum[row,col] = sum(grid[row][col].binCondition)
    return gridNum

def NextEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col].value == 0:
                return row, col
    return -1,-1 


sudo1 = SudokuGrid.SudokuGrid(9)
sudo2 = SudokuGrid.SudokuGrid(9)
sudo1.printGridTerminal()
backtracking(sudo1)
backtrackingMRV(sudo2)
sudo1.printGridTerminal()
