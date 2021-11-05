import SudokuGrid
import numpy as np


# Fonction de backtracking idiot
def backtracking(grid, nbIte=1):
    # Cherche le prochain vide:
    r, c = NextEmpty(grid)
    if r == -1:     # Le sudoku est terminé
        print(nbIte)
        return True
    else:
        for val in range(1, 10):
            if isPossible(grid, r, c, val):
                grid[r][c].value = val

                if backtracking(grid, nbIte + 1):
                    return True
                grid[r][c].value = 0
        return False


def backtrackingMRV(grid, nbIte=1):
    # Cherche le prochain vide:
    r, c = NextEmptyMRV(grid)
    if r == -1:     # Le sudoku est terminé
        print(nbIte)
        return True
    else:
        for val in range(1, 10):
            if isPossible(grid, r, c, val):
                grid[r][c].value = val

                if backtrackingMRV(grid, nbIte + 1):
                    return True
                grid[r][c].value = 0

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
                for val in range(1, 10):
                    if isPossible(grid, row, col, val):
                        gridNum[row][col] += 1
    return gridNum


def NextEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col].value == 0:
                return row, col
    return -1, -1


def isPossible(grid, row, col, val):

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


sudo1 = SudokuGrid.SudokuGrid(9)
sudo2 = SudokuGrid.SudokuGrid(9)
sudo1.printGridTerminal()
backtracking(sudo1.grid)
backtrackingMRV(sudo2.grid)
sudo1.printGridTerminal()
