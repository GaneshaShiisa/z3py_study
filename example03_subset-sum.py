'''部分和問題（subset-sum）
集合 {2,3,5,8,13,21,34} の部分集合で， 和が50になるものはあるか?
'''
from z3 import *

X = [2, 3, 5, 8, 13, 21, 34]
a = [Bool("a%s" % i) for i in range(len(X))]

s = Solver()
s.add(Sum([X[i]*a[i] for i in range(len(X))]) == 50)

print(s.check())
if s.check() == sat:
    m = s.model()
    subset = []
    for i in range(len(X)):
        if m[a[i]] == True:
            subset.append(X[i])

print(subset)
