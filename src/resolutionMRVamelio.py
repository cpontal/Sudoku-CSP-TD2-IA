import SudokuGrid
import numpy as np
import time


# Fonction de backtracking
def backtracking(sudoku, nbIte=1):
    # Cherche le prochain vide:
    r, c = NextEmpty(sudoku.grid)
    if r == -1:     # Le sudoku est terminé
        # print("Le nombre d'appel de la fonction
        # backtracking est : {}".format(nbIte))
        return True
    else:
        for val in range(1, 10):
            if sudoku.grid[r][c].binCondition[val - 1]:
                sudoku.defineValue(r, c, val)
                if backtracking(sudoku, nbIte + 1):
                    return True
                sudoku.defineValue(r, c, 0)
        return False


def backtrackingMRV(sudoku, nbIte=1):
    # Cherche le prochain vide:
    r, c = NextEmptyMRV(sudoku.grid)
    if r == -1:     # Le sudoku est terminé
        # print("Le nombre d'appel de la fonction
        # backtrackingMRV est : {}".format(nbIte))
        return True
    else:
        for val in range(1, 10):
            if sudoku.grid[r][c].binCondition[val - 1]:
                sudoku.defineValue(r, c, val)
                if backtrackingMRV(sudoku, nbIte + 1):
                    return True
                sudoku.defineValue(r, c, 0)
        return False


def NextEmptyMRV(grid):
    gridPoss = gridNumPossibility(grid)
    if gridPoss.any() != np.zeros((9, 9)).any():
        min = np.min(gridPoss[np.nonzero(gridPoss)])
        for row in range(9):
            for col in range(9):
                if gridPoss[row, col] == min:
                    return row, col

    # Si il y a encore des cases vides mais sans solution
    return NextEmpty(grid)


# Retourne le nombre de possibilité (en valeur) pour chaque case
def gridNumPossibility(grid):
    gridNum = np.zeros((9, 9))
    for row in range(9):
        for col in range(9):
            if grid[row][col].value == 0:
                gridNum[row, col] = sum(grid[row][col].binCondition)
    return gridNum


def NextEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col].value == 0:
                return row, col
    return -1, -1


"""
sudo1 = SudokuGrid.SudokuGrid(18)
sudo2 = SudokuGrid.SudokuGrid(18)
sudo1.printGridTerminal()
sudo1t1 = time.time()
backtracking(sudo1)
print("Le temps mis par le backtracking est : {} s"
    .format(time.time()-sudo1t1))
sudo2t1 = time.time()
backtrackingMRV(sudo2)
print("Le temps mis par le backtrackingMRV est : {} s"
    .format(time.time()-sudo2t1))
sudo1.printGridTerminal()
"""
