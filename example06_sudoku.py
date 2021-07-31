'''数独（sudoku）
3×3のブロックに区切られた 9×9の正方形の枠内に1〜9までの数字を入れる。
'''
from z3 import *

problem = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 3, 0, 0, 0, 6, 7, 0],
    [5, 0, 0, 4, 0, 2, 0, 0, 8],
    [8, 0, 0, 0, 6, 0, 0, 0, 1],
    [2, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 5, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 6, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 5, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]
# problem = [
#     [2, 0, 6, 0, 0, 8, 0, 0, 1],
#     [0, 0, 0, 0, 0, 3, 7, 0, 8],
#     [5, 0, 0, 6, 0, 0, 0, 0, 9],
#     [8, 0, 0, 0, 4, 0, 0, 3, 0],
#     [0, 0, 0, 0, 0, 0, 0, 9, 4],
#     [0, 0, 9, 0, 0, 0, 2, 0, 0],
#     [0, 0, 3, 7, 0, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0, 6, 0, 0, 0],
#     [1, 0, 0, 0, 8, 0, 0, 5, 0]
# ]
X = [[Int("x_%s_%s" % (i, j))for j in range(9)] for i in range(9)]

s = Solver()
s.add([And(1 <= X[i][j], X[i][j] <= 9) for i in range(9) for j in range(9)])
for i in range(9):
    for j in range(9):
        if problem[i][j] != 0:
            s.add(X[i][j] == problem[i][j])
s.add([Distinct([X[i][j] for i in range(9)]) for j in range(9)])
s.add([Distinct([X[i][j] for j in range(9)]) for i in range(9)])
s.add([Distinct([X[i+3*a][j+3*b] for i in range(3)
      for j in range(3)]) for a in range(3) for b in range(3)])

print(s.check())

m = s.model()
for i in range(9):
    tmp = []
    for j in range(9):
        tmp.append(m[X[i][j]])
    print(tmp)
