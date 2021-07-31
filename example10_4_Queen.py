'''4クイーン問題（4 Queen）
4×4 のボード上に，4つのチェスのクイーンのコマを置く．
4つのクイーンが互いに取られないように配置することはできるか?
'''
from z3 import *

X = [[Int("x_%s_%s" % (i, j)) for j in range(4)]for i in range(4)]

s = Solver()
s.add([And(0 <= X[i][j], X[i][j] <= 1) for i in range(4) for j in range(4)])
s.add([Sum([X[i][j]for i in range(4)]) == 1 for j in range(4)])
s.add([Sum([X[i][j]for j in range(4)]) == 1 for i in range(4)])
for a in range(-2, 3):
    diag = []
    for i in range(4):
        if (0 <= i+a) & (i+a <= 3):
            diag.append(X[i+a][i])
    s.add(Sum(diag) <= 1)

for a in range(-2, 3):
    diag = []
    for i in range(4):
        if (0 <= i+a) & (i+a <= 3):
            diag.append(X[i+a][3-i])
    s.add(Sum(diag) <= 1)

print(s.check())
m = s.model()
for i in range(4):
    tmp = []
    for j in range(4):
        tmp.append(m[X[i][j]])
    print(tmp)
