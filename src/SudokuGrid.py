
from random import randrange
import os
import Square

class SudokuGrid:
    def __init__(self):
        self.grid = [] # matrice d'entier
        self.loadGrid()
        # self.loadEasyGrid()

    def defineValue(self, line, column, value):
        if self.grid[line][column].value == 0:
            if self.grid[line][column].binCondition[value-1] == True:
                self.grid[line][column].value = value
                for i in self.grid[line][column].binCondition:
                    self.grid[line][column].binCondition[i] = False
                self.updateConstraint(line, column)
            else:
                print("Erreur method defineValue : la valeur de respecte pas la contrainte")
                return 1
        else:
            print("Erreur method defineValue : la case a déjà une valeur")
            return 1

    def initCheckAllConstraint(self):
        for i in range(9):
            self.checkConstraintLine(i)
            self.checkConstraintcollumn(i)
        
        for i in range(3):
            for j in range(3):
                self.checkConstraintBloc(i*3, j*3)
    
    def updateConstraint(self, line, column):
        self.checkConstraintBloc(line, column)
        self.checkConstraintLine(line)
        self.checkConstraintcollumn(column)

    def checkConstraintcollumn(self, n):
        for elem in self.grid:
            if elem[n].value > 0:
                for tab in self.grid:
                    if tab[n].value == 0:
                        tab[n].binCondition[elem[n].value-1] = False
        return
    
    def checkConstraintLine(self, n):
        for elem in self.grid[n]:
            if elem.value > 0:
                for tab in self.grid[n]:
                    if tab.value == 0:
                        tab.binCondition[elem.value-1] = False
        return
    
    def checkConstraintBloc(self, lineNumber, columnNumber):
        square = 3
        groupNumberLine = lineNumber//square
        groupNumberColumn = columnNumber//square
        tabGroup = []
        for i in range(square*groupNumberLine, square + square*groupNumberLine):
            for j in range(square*groupNumberColumn, square + square*groupNumberColumn):
                tabGroup.append(self.grid[i][j])

        for i in range(square*square):
            if tabGroup[i].value > 0:
                for j in range(square*square):
                    if tabGroup[j].value == 0:
                        tabGroup[j].binCondition[tabGroup[i].value-1] = False
        return

    def printGridTerminal(self):
        print("╔═══════════╦═══════════╦═══════════╗")
        for i, row in enumerate(self.grid):
            print(("║" + " {} ¦ {} ¦ {} ║"*3).format(*[x.value if x.value != 0 else " " for x in row]))
            if i == 8:
                print("╚═══════════╩═══════════╩═══════════╝")
            elif i % 3 == 2:
                print("╠═══════════╬═══════════╬═══════════╣")
            else:
                print("║---+---+---║---+---+---║---+---+---║")
    
    def loadGrid(self):
        lineNumber = (randrange(50) * 10) + 1
        f = open("src\grid.txt", "r")
        for i, line in enumerate(f):
            if ((i >= lineNumber) & (i< lineNumber+9)):

                self.grid.append(list(map(Square.Square, map(int, line.rstrip('\n')))))
            elif i > lineNumber+9:
                break
        f.close()
        self.initCheckAllConstraint()
        # self.grid.append(list(map(int, "003020600")))
        # self.grid.append(list(map(int, "900305001")))
        # self.grid.append(list(map(int, "001806400")))
        # self.grid.append(list(map(int, "008102900")))
        # self.grid.append(list(map(int, "700000008")))
        # self.grid.append(list(map(int, "006708200")))
        # self.grid.append(list(map(int, "002609500")))
        # self.grid.append(list(map(int, "800203009")))
        # self.grid.append(list(map(int, "005010300")))

    def loadEasyGrid(self):
        self.grid.append(list(map(Square.Square, map(int, "509800010"))))
        self.grid.append(list(map(Square.Square, map(int, "067340209"))))
        self.grid.append(list(map(Square.Square, map(int, "002916507"))))
        self.grid.append(list(map(Square.Square, map(int, "415693028"))))
        self.grid.append(list(map(Square.Square, map(int, "906700403"))))
        self.grid.append(list(map(Square.Square, map(int, "073402091"))))
        self.grid.append(list(map(Square.Square, map(int, "201009060"))))
        self.grid.append(list(map(Square.Square, map(int, "708060100"))))
        self.grid.append(list(map(Square.Square, map(int, "004130000"))))
        self.initCheckAllConstraint()

# g = SudokuGrid()
# g.loadGrid()
# g.printGridTerminal()


# print(g.grid[8][8].value)
# print(g.grid[8][8].binCondition)
# g.checkConstraintcollumn(8)
# print(g.grid[8][8].value)
# print(g.grid[8][8].binCondition)
# g.checkConstraintLine(8)
# print(g.grid[8][8].value)
# print(g.grid[8][8].binCondition)
# g.checkConstraintBloc(8,8)
# print(g.grid[8][8].value)
# print(g.grid[8][8].binCondition)
# g.defineValue(8,8,8)
# g.printGridTerminal()