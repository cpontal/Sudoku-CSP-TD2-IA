import SudokuGrid


def resNaive(g):
    nbIteration = 100
    iter = 0
    while iter < nbIteration:
        change = False
        for line in range(len(g.grid)):
            for col in range(len(g.grid[0])):
                index = -1
                nbSoluce = 0
                if g.grid[line][col].value == 0:
                    for resProblem in range(len(g.grid[line][col].binCondition
                                                )):
                        if g.grid[line][col].binCondition[resProblem] is True:
                            index = resProblem
                            nbSoluce = nbSoluce + 1
                    if nbSoluce == 1:
                        print("l:", line, " col:", col, " val:", index+1)
                        change = True
                        g.defineValue(line, col, index+1)
        if change is True:
            break
        iter = iter + 1
    g.printGridTerminal()


g = SudokuGrid.SudokuGrid()
g.printGridTerminal()
resNaive(g)
