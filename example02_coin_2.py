'''コイン問題２
以下のユーロ硬貨を持っているとする(総和は148セントになる)。
20セント硬貨 4枚
10セント硬貨 4枚
5セント硬貨 4枚
2セント硬貨 4枚
合計がちょうど93セントになる組合せはあるだろうか?
各3枚の場合はどうか？
'''
from z3 import *

coin__2cent = Int("coin__2cent")
coin__5cent = Int("coin__5cent")
coin_10cent = Int("coin_10cent")
coin_20cent = Int("coin_20cent")

s = Solver()
s.add(And(0 <= coin__2cent, coin__2cent <= 4))
s.add(And(0 <= coin__5cent, coin__5cent <= 4))
s.add(And(0 <= coin_10cent, coin_10cent <= 4))
# s.add(And(0 <= coin_20cent, coin_20cent <= 4))
s.add(0 <= coin_20cent, coin_20cent <= 4)
s.add(2*coin__2cent + 5*coin__5cent + 10*coin_10cent + 20*coin_20cent == 93)

print(s.check())
if s.check() == sat:
    print(s.model())

s = Solver()
s.add(And(0 <= coin__2cent, coin__2cent <= 3))
s.add(And(0 <= coin__5cent, coin__5cent <= 3))
s.add(And(0 <= coin_10cent, coin_10cent <= 3))
s.add(And(0 <= coin_20cent, coin_20cent <= 3))
s.add(2*coin__2cent + 5*coin__5cent + 10*coin_10cent + 20*coin_20cent == 93)

print(s.check())
if s.check() == sat:
    print(s.model())
