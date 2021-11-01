import resolutionMRVamelio
import SudokuGrid
import numpy as np
import time

##Test sur sudoku specifique
sudokuBacktracking = SudokuGrid.SudokuGrid(18)
sudokuBacktrackingMRV = SudokuGrid.SudokuGrid(18)
sudokuBacktracking.printGridTerminal()
sudokuBacktrackingt1 = time.time()
resolutionMRVamelio.backtracking(sudokuBacktracking)
print("Le temps mis par le backtracking est : {} s" .format(time.time()-sudokuBacktrackingt1))
sudokuBacktrackingMRVt1 = time.time()
resolutionMRVamelio.backtrackingMRV(sudokuBacktrackingMRV)
print("Le temps mis par le backtrackingMRV est : {} s" .format(time.time()-sudokuBacktrackingMRVt1))
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

print("Le temps mis par le backtracking pour l'ensemble des sudokus est : {} s" .format(time.time()-tempsTotalBacktrackingMRV))