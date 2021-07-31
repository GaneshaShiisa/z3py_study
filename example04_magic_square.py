'''魔方陣（magic square）
1から9の数字を 3×3 に配置し， 各行，各列，各対角線の和がいずれも15になるようにせよ．
'''
from z3 import *

X = [[Int("x_%s_%s" % (i, j)) for j in range(3)] for i in range(3)]

s = Solver()
s.add([And(1 <= X[i][j], X[i][j] <= 9) for i in range(3) for j in range(3)])
s.add([Distinct([X[i][j] for i in range(3) for j in range(3)])])
s.add([Sum([X[i][j] for i in range(3)]) == 15 for j in range(3)])
s.add([Sum([X[i][j] for j in range(3)]) == 15 for i in range(3)])
s.add([Sum([X[i][i] for i in range(3)]) == 15])
s.add([Sum([X[i][2-i] for i in range(3)]) == 15])

print(s.check())

m = s.model()
for i in range(3):
    row = []
    for j in range(3):
        row.append(m[X[i][j]])
    print(row)

for a in range(10):
    print(a)
    m = s.model()
    s.add([Not(And([X[i][j] == m[X[i][j]] for i in range(3) for j in range(3)]))])
    if s.check() == sat:
        print(s.model())
    else:
        break
