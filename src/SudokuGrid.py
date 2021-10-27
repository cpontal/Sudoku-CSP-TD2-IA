
from random import randrange
import os


class SudokuGrid:
    def __init__(self):
        self.grid = [] # matrice d'entier

    def printGridTerminal(self):
        print("╔═══════════╦═══════════╦═══════════╗")
        for i, row in enumerate(self.grid):
            print(("║" + " {} ¦ {} ¦ {} ║"*3).format(*[x if x != 0 else " " for x in row]))
            if i == 8:
                print("╚═══════════╩═══════════╩═══════════╝")
            elif i % 3 == 2:
                print("╠═══════════╬═══════════╬═══════════╣")
            else:
                print("║---+---+---║---+---+---║---+---+---║")





        # bar = '―――――――――――――――――――――――――\n'
        # '|'
        # for row in self.grid:
        #     for elem in row:
        #         print(elem)
        # bar = '―――――――――――――――――――――――――\n'
        # lnf = '|' +(' {:}'*3 + ' |')*3 + '\n'
        # bft = bar + (lnf*3+bar)*3
        # print(bft.format(*(el for rw in self.grid for el in rw)))
    
    def loadGrid(self):
        lineNumber = (randrange(50) * 10) + 1
        f = open("src\grid.txt", "r")
        for i, line in enumerate(f):
            if ((i >= lineNumber) & (i< lineNumber+9)):
                self.grid.append(list(map(int, line.rstrip('\n'))))
            elif i > lineNumber+9:
                break
        f.close()
        # self.grid.append(list(map(int, "003020600")))
        # self.grid.append(list(map(int, "900305001")))
        # self.grid.append(list(map(int, "001806400")))
        # self.grid.append(list(map(int, "008102900")))
        # self.grid.append(list(map(int, "700000008")))
        # self.grid.append(list(map(int, "006708200")))
        # self.grid.append(list(map(int, "002609500")))
        # self.grid.append(list(map(int, "800203009")))
        # self.grid.append(list(map(int, "005010300")))

g = SudokuGrid()
g.loadGrid()
g.printGridTerminal()






    