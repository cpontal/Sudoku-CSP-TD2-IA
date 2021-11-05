import resolutionMRVamelio
import resolutionLeastConstrainingValue_DegreeHeuristic
import resolutionAC3
import SudokuGrid
import numpy as np
import time
import random


### Test sur sudoku specifique ###

#Initialisation des sudokus
n = random.randint(1,50)
sudokuBacktracking = SudokuGrid.SudokuGrid(n)
sudokuBacktrackingMRV = SudokuGrid.SudokuGrid(n)
sudokuBacktrackingAC3 = SudokuGrid.SudokuGrid(n)
sudokuBacktrackingLCV = SudokuGrid.SudokuGrid(n)
sudokuBacktrackingDH = SudokuGrid.SudokuGrid(n)

# Affichage du sudoku initial
sudokuBacktracking.printGridTerminal()

# Résolution et affichage du temps pour chauqe méthode
print()
print("##############################")
print("Résolution pour un même sudoku")
print()

######## BACKTRACKING ##########
sudokuBacktrackingt1 = time.time()
resolutionMRVamelio.backtracking(sudokuBacktracking)
print("Le temps mis par le backtracking est: {} s" .format(
    time.time()-sudokuBacktrackingt1))

######## MRV ##########
sudokuBacktrackingMRVt1 = time.time()
resolutionMRVamelio.backtrackingMRV(sudokuBacktrackingMRV)
print("Le temps mis par le backtrackingMRV est: {} s" .format(
    time.time()-sudokuBacktrackingMRVt1))

######## AC3 ##########
sudokuBacktrackingAC3t1 = time.time()
resolutionAC3.backtrackingAC3(sudokuBacktrackingAC3)
print("Le temps mis par le backtrackingAC3 est: {} s" .format(
    time.time()-sudokuBacktrackingAC3t1))

######## LCV ##########
sudokuBacktrackingLCVt1 = time.time()
resolutionLeastConstrainingValue_DegreeHeuristic.backtrackingLCV(
    sudokuBacktrackingLCV)
print("Le temps mis par le backtrackingLCV est: {} s" .format(
    time.time()-sudokuBacktrackingLCVt1))

######## DH ##########
sudokuBacktrackingDHt1 = time.time()
resolutionLeastConstrainingValue_DegreeHeuristic.backtrackingDegreeHeuristic(
    sudokuBacktrackingDH)
print("Le temps mis par le backtrackingDH est: {} s" .format(
    time.time()-sudokuBacktrackingDHt1))

print()
print("##############################")
print()

# Affichage du sudoku final
sudokuBacktracking.printGridTerminal()

########################################
print()
print("##############################")

# Test sur l'enseble des sudokus
n = 50  # nombre de sudoku teste
print("Résolution de {} sudokus par les différents algorithmes".format(n))
print()

######## BACKTRACKING ##########
tempsTotalBacktracking = time.time()
for i in range(n):
    sudokuBacktracking = SudokuGrid.SudokuGrid(i)
    resolutionMRVamelio.backtracking(sudokuBacktracking)
print(
    "Le temps mis par le backtracking pour l'ensemble des sudokus est: {} s"
    .format((time.time()-tempsTotalBacktracking)/n))

######## MRV ##########
tempsTotalBacktrackingMRV = time.time()
for i in range(n):
    sudokuBacktrackingMRV = SudokuGrid.SudokuGrid(i)
    resolutionMRVamelio.backtrackingMRV(sudokuBacktrackingMRV)
print(
    "Le temps mis par le backtrackingMRV pour l'ensemble des sudokus est: {} s"
    .format((time.time()-tempsTotalBacktrackingMRV)/n))

######## AC3 ##########
tempsTotalBacktrackingAC3 = time.time()
for i in range(n):
    sudokuBacktrackingAC3 = SudokuGrid.SudokuGrid(i)
    resolutionAC3.backtrackingAC3(sudokuBacktrackingAC3)
print(
    "Le temps mis par le backtrackingAC3 pour l'ensemble des sudokus est: {} s"
    .format((time.time()-tempsTotalBacktrackingAC3)/n))

######## LCV ##########
tempsTotalBacktrackingLCV = time.time()
for i in range(n):
    sudokuBacktrackingLCV = SudokuGrid.SudokuGrid(i)
    resolutionLeastConstrainingValue_DegreeHeuristic.backtrackingLCV(
        sudokuBacktrackingLCV)
print(
    "Le temps mis par le backtrackingLCV pour l'ensemble des sudokus est: {} s"
    .format((time.time()-tempsTotalBacktrackingLCV)/n))

######## DH ##########
tempsTotalBacktrackingDH = time.time()
for i in range(n):
    sudokuBacktrackingDH = SudokuGrid.SudokuGrid(i)
    resolutionLeastConstrainingValue_DegreeHeuristic\
        .backtrackingDegreeHeuristic(sudokuBacktrackingDH)
print(
    "Le temps mis par le backtrackingDH pour l'ensemble des sudokus est: {} s"
    .format((time.time()-tempsTotalBacktrackingDH)/n))
