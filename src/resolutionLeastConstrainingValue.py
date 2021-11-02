import SudokuGrid
import numpy as np


def backtrackingLCV(grid):
    #Cherche le prochain vide:
    r,c = NextEmptyLCV(grid)
    if r == -1: #Le sudoku est terminé
        return True
    else:
        total_poss = 0
        highest_total_poss = 0
        val_with_highest = -1

        # Pour chacune des valeurs possibles, soit de 1 a 9:
        for val in range(1,10):
            # ...Si la valeur 'val' est possible pour la case a la position
            # (r, c):
            if isPossible(grid, r, c, val):
                # ...Donner cette valeur a une grille copie
                grid[r][c].value = val

                # Faire le total des possibilites pour les autres cases si la
                # valeur de la case actuelle est 'val':
                total_poss = grid_poss_sum_value(grid)

                # Garder le plus grand total de possibilites et la valeur de
                # cette case dans ce cas:
                if total_poss >= highest_total_poss:
                    highest_total_poss = total_poss
                    val_with_highest = val
        # Quand on a passe au travers des valeurs possibles pour la case
        # actuelle, soit de 1 a 9, on donne la valeur pour laquelle il y a le
        # plus de possibilites pour les autres cases (la ou la somme est la
        # plus grande).
        grid[r][c].value = val_with_highest

        # Si le backtracking est fini, on a fini
        if backtrackingLCV(grid):
            return True

        # Si non on remet la valeur a 0 (plutot qu'a la valeur 'val' trouve
        # precedemment) et on quitte la fonction, on refait la boucle
        # principale de l'algorithme.
        grid[r][c].value = 0
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


def grid_poss_highest_value(grid):  # Not used
    gridPoss = gridNumPossibility(grid)
    if gridPoss.any() != np.zeros((9,9)).any():
        max_poss_x, max_poss_y = np.unravel_index(gridPoss.argmax(), gridPoss.shape)
        max_possibilite = gridPoss[max_poss_x, max_poss_y]
        return max_poss_x, max_poss_y, max_possibilite
    return -1, -1, -1


def grid_poss_sum_value(grid):
    total_possibilites = 0
    gridPoss = gridNumPossibility(grid)
    for row in range(9):
        for col in range(9):
            total_possibilites += gridPoss[row, col]
    return total_possibilites


def gridNumPossibility(grid): #Retourne le nombre de possibilité (en valeur) pour chaque case
    gridNum = np.zeros((9,9))
    for row in range(9):
        for col in range(9):
            if grid[row][col].value == 0:
                for val in range(1,10):
                    if isPossible(grid, row, col, val):
                        gridNum[row][col] += 1
    return gridNum


def NextEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col].value == 0:
                return row, col
    return -1,-1


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


def least_constraining_value(grid):
    iteration = 10000
    for x in range(iteration):
        # La fonction 'backtrackingLCV' va back track tant que le tableau n'est
        # pas rempli au complet. Remplis au complet veut dire rempli avec des
        # valeurs de 1 a 9, ou -1 quand je passe par la case mais qu'il n'y a
        # aucune valeur possible (que la fonction 'isPossible' retourne faux).
        backtrackingLCV(grid)

        # Une fois que le tableau est rempli de valeurs de 1 a 9 ou de -1
        # (quand la fonction 'isPossible' retourne faux), on repasse a travers
        # le tableau et on remet tous les -1 a 0 puis on refait une tournee. Le
        # nombre de tournees qu'on fait est le nombre d'iterations ici dans
        # cette fonction.
        for row in range(9):
            for col in range(9):
                if grid[row][col].value == -1:
                    grid[row][col].value = 0


g = SudokuGrid.SudokuGrid()
g.printGridTerminal()

least_constraining_value(g.grid)

print(gridNumPossibility(g.grid))
g.printGridTerminal()
