import resolutionMRVamelio
import resolutionAC3
import SudokuGrid
import numpy as np
import time

##Test sur sudoku specifique
sudokuBacktracking = SudokuGrid.SudokuGrid(18)
sudokuBacktrackingMRV = SudokuGrid.SudokuGrid(18)
sudokuBacktrackingAC3 = SudokuGrid.SudokuGrid(18)
sudokuBacktracking.printGridTerminal()
sudokuBacktrackingt1 = time.time()
resolutionMRVamelio.backtracking(sudokuBacktracking)
print("Le temps mis par le backtracking est : {} s" .format(time.time()-sudokuBacktrackingt1))
sudokuBacktrackingMRVt1 = time.time()
resolutionMRVamelio.backtrackingMRV(sudokuBacktrackingMRV)
print("Le temps mis par le backtrackingMRV est : {} s" .format(time.time()-sudokuBacktrackingMRVt1))
sudokuBacktrackingAC3t1 = time.time()
resolutionAC3.backtrackingAC3(sudokuBacktrackingAC3)
print("Le temps mis par le backtrackingAC3 est : {} s" .format(time.time()-sudokuBacktrackingAC3t1))
sudokuBacktracking.printGridTerminal()

##Test sur l'enseble des sudokus
tempsTotalBacktracking = time.time()
for i in range(1,10):
    print(i)
    sudokuBacktracking = SudokuGrid.SudokuGrid(i)
    resolutionMRVamelio.backtracking(sudokuBacktracking)
print("Le temps mis par le backtracking pour l'ensemble des sudokus est : {} s" .format(time.time()-tempsTotalBacktracking))

tempsTotalBacktrackingMRV = time.time()
for i in range(1,10):
    print(i)
    sudokuBacktrackingMRV = SudokuGrid.SudokuGrid(i)
    resolutionMRVamelio.backtrackingMRV(sudokuBacktrackingMRV)

print("Le temps mis par le backtrackingMRV pour l'ensemble des sudokus est : {} s" .format(time.time()-tempsTotalBacktrackingMRV))

tempsTotalBacktrackingAC3 = time.time()
for i in range(1,10):
    print(i)
    sudokuBacktrackingAC3 = SudokuGrid.SudokuGrid(i)
    resolutionAC3.backtrackingAC3(sudokuBacktrackingAC3)

print("Le temps mis par le backtrackingAC3 pour l'ensemble des sudokus est : {} s" .format(time.time()-tempsTotalBacktrackingAC3))