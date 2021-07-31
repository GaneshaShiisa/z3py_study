'''ビンパッキング問題（Bin packing）
4人で8個の荷物を運ぶとする． 各荷物の重さは
3.3kg, 6.1kg, 5.8kg, 4.1kg, 5.0kg, 2.1kg, 6.0kg, 6.4kg
である (合計は 38.8kg)．
各自の運ぶ荷物の重さの合計が 11kg 以下になるように荷物を割り当てることはできるか?
'''
from z3 import *

loads = [3.3, 6.1, 5.8, 4.1, 5.0, 2.1, 6.0, 6.4]
X = [[Int("x_%s_%s" % (i, j)) for j in range(len(loads))] for i in range(4)]

s = Solver()
s.add([And(0 <= X[i][j], X[i][j] <= 1)
      for i in range(4) for j in range(len(loads))])
# 各荷物は、誰か1人が運ぶ
s.add([Sum([X[i][j] for i in range(4)]) == 1 for j in range(len(loads))])
# 各自の運ぶ荷物の重さの合計は11kg以下
s.add([Sum([loads[j]*ToReal(X[i][j])
      for j in range(len(loads))]) < 11 for i in range(4)])

print(s.check())

m = s.model()
for i in range(4):
    sum = 0
    for j in range(len(loads)):
        sum += loads[j]*m[X[i][j]].as_long()
    print("*", i, sum)
