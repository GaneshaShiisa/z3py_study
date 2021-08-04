from z3 import *

x = Int("x")
y = Int("y")

p = [Int("p%s" % i) for i in range(5)]

hannin = Function('Hannin', IntSort(), BoolSort())
chiteki = Function('Chiteki', IntSort(), BoolSort())
ranbo = Function('Ranbo', IntSort(), BoolSort())
henjin = Function('Henjin', IntSort(), BoolSort())
aribai = Function('Aribai', IntSort(), IntSort(), BoolSort())

premise_01 = [
    Or([hannin(p[i])for i in range(5)]) == True]
premise_02 = [chiteki(p[0]) == True]
premise_03 = [chiteki(p[1]) == True]
premise_04 = [ranbo(p[3]) == True]
premise_05 = [ranbo(p[4]) == True]
premise_06 = [ForAll(x, And(chiteki(x), ranbo(x)) == True)]
premise_07_1 = [Exists(x, And(chiteki(x), henjin(x)) == True)]
premise_07_2 = [ForAll(x, Implies(Not(chiteki(x)), Not(henjin(x))) == True)]
premise_08 = [aribai(p[3], p[0]) == True]
premise_09 = [aribai(p[1], p[4]) == True]
premise_10 = [aribai(p[0], p[2]) == True]
premise_11 = [ForAll(x, Implies(hannin(x), henjin(x)) == True)]
premise_12 = [ForAll([x, y], Implies(
    And(Not(hannin(x)), aribai(x, y)), Not(hannin(y))) == True)]
premise_13 = [ForAll(x, Implies(Not(ranbo(x)), Not(hannin(x))) == True)]
premise_14 = [hannin(p[3]) == False]

premise_15 = []
# premise_15 = [p[1] == p[4]]

premise = premise_01+premise_02+premise_03+premise_04+premise_05+premise_06+premise_07_1 + \
    premise_07_2+premise_08+premise_09+premise_10 + \
    premise_11+premise_12+premise_13+premise_14+premise_15

s = Solver()
s.add(premise)

print(s.check())

# 犯人でない人の確認
print("犯人でない人の確認")
for i in range(5):
    s = Solver()
    s.add(Not(Implies(And(premise), hannin(p[i]) == False)))
    print(i, s.check())

# 犯人の確認
print("犯人の確認")
for i in range(5):
    s = Solver()
    s.add(Not(Implies(And(premise), hannin(p[i]) == True)))
    print(i, s.check())
