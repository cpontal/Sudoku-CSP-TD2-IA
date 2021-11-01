import SudokuGrid
import numpy as np


def backtrackingAC3(g):
    #Cherche le prochain vide:
    r,c = NextEmpty(g.grid)
    if r == -1: #Le sudoku est terminé
        return True
    else:
        for i in range(len(g.grid[r][c].binCondition)):
            if g.grid[r][c].binCondition[i] == True:
                val = i+1
                if checkConsistensy(g, r, c, val):
                    g.defineValue(r, c, val)
                    
                    if backtrackingAC3(g):
                        return True
                    g.defineValue(r,c,0)
        return False

def NextEmpty(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col].value == 0:
                return row, col
    return -1,-1

def checkConsistensy(g, row, col, val):
    if ((g.grid[row][col].binCondition[val-1]) & (sum(g.grid[row][col].binCondition) == 1)):
        return True

    for tab in g.grid:
        if tab[col].value == 0:
            nbTrue = sum(tab[col].binCondition)
            if ((tab[col].binCondition[val-1]) & (nbTrue == 1)):
                return False
                

    for elem in g.grid[row]:
        if elem.value == 0:
            nbTrue = sum(elem.binCondition)
            if ((elem.binCondition[val-1]) & (nbTrue == 1)):
                return False
    
    square = 3
    groupNumberLine = row//square
    groupNumberColumn = col//square
    tabGroup = []
    for i in range(square*groupNumberLine, square + square*groupNumberLine):
        for j in range(square*groupNumberColumn, square + square*groupNumberColumn):
            tabGroup.append(g.grid[i][j])

    for i in range(square*square):
        if tabGroup[i].value == 0:
            nbTrue = sum(tabGroup[i].binCondition)
            if ((tabGroup[i].binCondition[val-1]) & (nbTrue == 1)):
                return False

    return True


g = SudokuGrid.SudokuGrid()
g.printGridTerminal()

print(backtrackingAC3(g))
g.printGridTerminal()