# Maze Solver

A Python demonstration of recursive backtracking. The solver starts in the top-left corner and tries to reach the bottom-right corner by moving down or right through open cells. It prints the route as zero-based `(row, column)` coordinates.

## Run

```sh
python3 Maze_solver.py
```

The included maze uses `0` for open cells and `1` for walls. To try a different layout, edit `MAZE` in the script and keep the grid square. A blocked start, a blocked destination, or a maze with no down-or-right route produces no solution. The script uses the Python standard library.
