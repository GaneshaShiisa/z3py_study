'''ハノイの塔（Tower of Hanoi）
以下のルールに従って、すべての円盤を右端の杭に移動する。
○ 3本の杭と、中央に穴の開いた大きさの異なる複数の円盤から構成される。
○ 最初はすべての円盤が左端の杭に小さいものが上になるように順に積み重ねられている。
○ 円盤を一回に一枚ずつどれかの杭に移動させることができるが、小さな円盤の上に大きな円盤を乗せることはできない。

円盤は4枚
'''
from z3 import *
import itertools

disk_num = 4
peg = 3

# 存在する状態を列挙 (disk_4,disk_3,disk_2,disk_1) の形
states = itertools.product(range(peg), repeat=disk_num)
dict_state = {}
# 状態を辞書化
for i, state in enumerate(states):
    dict_state[i] = state


# 状態の逆引き辞書作成
def inverse_dict(d):
    return {v: k for k, v in d.items()}


inverse_dict_state = inverse_dict(dict_state)


# 制約定義
t_max = 16  # 移動させる回数
T = [Int("T%s" % i) for i in range(t_max)]
f = Function('f', IntSort(), IntSort(), BoolSort())

s = Solver()
s.add([And(0 <= T[i], T[i] <= len(dict_state)-1) for i in range(len(T))])


def check_state_change(before, after):
    # 状態遷移が可能かどうかチェックする
    changed_disk = None
    for x in range(len(before)):
        # 一度に１枚だけしか移動しない。
        if (before[x] - after[x]) != 0:
            if changed_disk != None:
                changed_disk = None
                break
            else:
                changed_disk = x

        else:
            if changed_disk != None:
                # 前状態において、一番上のDiskしか移動しない
                if (before[changed_disk] - before[x]) == 0:
                    changed_disk = None
                    break
                # 小さな円盤の上に大きな円盤を乗せることはできない
                if (after[changed_disk] - after[x]) == 0:
                    changed_disk = None
                    break

    if changed_disk != None:
        return True
    else:
        return False


for i in range(len(dict_state)):
    for j in range(len(dict_state)):
        if check_state_change(dict_state[i], dict_state[j]):
            s.add(f(i, j) == True)
        else:
            s.add(f(i, j) == False)

# 全ての遷移において、遷移可能な状態である。
for i in range(len(T)-1):
    s.add(f(T[i], T[i+1]))

# 初期状態と終了状態を指定する。
s.add(T[0] == inverse_dict_state[(0, 0, 0, 0)])
s.add(T[-1] == inverse_dict_state[(2, 2, 2, 2)])


# 結果
print(s.check())
if s.check() == sat:
    # print(s.model())
    m = s.model()
    for i in range(len(T)):
        print('T['+str(i)+']=' + str(dict_state[m[T[i]].as_long()]))
