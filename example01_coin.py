'''コイン問題（制約充足問題）
1円硬貨，5円硬貨，10円硬貨を合計で15枚，それぞれを1枚以上持っている． 
金額の合計は90円である． それぞれの硬貨を何枚持っているか?
'''
from z3 import *

coin__1yen = Int("coin__1yen")
coin__5yen = Int("coin__5yen")
coin_10yen = Int("coin_10yen")

s = Solver()
s.add(coin__1yen >= 1)
s.add(coin__5yen >= 1)
s.add(coin_10yen >= 1)
s.add((coin__1yen + coin__5yen + coin_10yen) == 15)
s.add((coin__1yen + 5 * coin__5yen + 10 * coin_10yen) == 90)

print(s.check())
if s.check() == sat:
    print(s.model())
