import SudokuGrid
import numpy as np


def backtrackingLCV(sudoku):
    # Cherche le prochain vide:
    r,c = NextEmpty(sudoku.grid)
    if r == -1: # Le sudoku est terminé
        return True
    else:

        # Pour chacune des valeurs possibles, soit de 1 a 9:
        li = []
        for val in range(1,10):
            # ...Si la valeur 'val' est possible pour la case a la position
            # (r, c):
            if sudoku.grid[r][c].binCondition[val-1]:
                # ...Donner cette valeur a la grille
                sudoku.defineValue(r, c, val)
               
                # Faire le total des possibilites pour les autres cases si la
                # valeur de la case actuelle est 'val':
                total_poss = grid_poss_sum_value(sudoku.grid)
                li.append([total_poss,val])

                sudoku.defineValue(r,c, 0)
        # Quand on a passe au travers des valeurs possibles pour la case
        # actuelle, soit de 1 a 9, on donne la valeur pour laquelle il y a le
        # plus de possibilites pour les autres cases (la ou la somme est la
        # plus grande). Mettre en ordre du plus grand nombre de possibilites.
        li.sort()
        for i in range(len(li)):
            sudoku.defineValue(r, c, li[len(li)-i-1][1])
        # Si le backtracking est fini, on a fini
            if backtrackingLCV(sudoku):
                return True

        # Si non on remet la valeur a 0 (plutot qu'a la valeur 'val' trouve
        # precedemment).
            sudoku.defineValue(r,c,0)
        return False


def backtrackingDegreeHeuristic(sudoku):
    # Cherche le prochain vide:
    r,c = NextEmpty(sudoku.grid)
    if r == -1: # Le sudoku est terminé
        return True
    else:
        # Pour chacune des valeurs possibles, soit de 1 a 9:
        li = []
        for val in range(1,10):
            # ...Si la valeur 'val' est possible pour la case a la position
            # (r, c):
            if sudoku.grid[r][c].binCondition[val-1]:
                # ...Donner cette valeur a la grille
                sudoku.defineValue(r, c, val)
               
                # Faire le total des possibilites pour les autres cases si la
                # valeur de la case actuelle est 'val':
                total_poss = grid_poss_sum_value(sudoku.grid)
                li.append([total_poss,val])

                sudoku.defineValue(r,c, 0)
        # Quand on a passe au travers des valeurs possibles pour la case
        # actuelle, soit de 1 a 9, on donne la valeur pour laquelle il y a le
        # moins de possibilites pour les autres cases (la ou la somme est la
        # plus petite). Mettre en ordre du plus petit nombre de possibilites.
        li.sort()
        for i in range(len(li)):
            sudoku.defineValue(r, c, li[i][1])
            # Si le backtracking est fini, on a fini
            if backtrackingLCV(sudoku):
                return True
            # Si non on remet la valeur a 0 (plutot qu'a la valeur 'val' trouve
            # precedemment).
            sudoku.defineValue(r,c,0)
        return False


def NextEmptyLCV(grid):
    gridPoss = gridNumPossibility(grid)
    if gridPoss.any() != np.zeros((9,9)).any():
        for row in range(9):
            for col in range(9):
                # Return the first empty value:
                if  gridPoss[row, col] != 0:
                    return row, col
    return NextEmpty(grid) # Si il y a encore des cases vides mais sans solution


def grid_poss_sum_value(grid):
    return np.sum(gridNumPossibility(grid))


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


# Resolution with the Least constraining value algorithm
g = SudokuGrid.SudokuGrid()
g.printGridTerminal()
backtrackingLCV(g)
g.printGridTerminal()

# Resolution with the Degree heuristic algorithm
g = SudokuGrid.SudokuGrid()
g.printGridTerminal()
backtrackingDegreeHeuristic(g)
g.printGridTerminal()
