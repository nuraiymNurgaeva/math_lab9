
import math
from sympy import *
from bisect import bisect
def mr(num):
    return round(num, 6)
def get_x0(x, l, m):
    if m == 1:
        for i in l:
            if i > x:
                return l.index(i), i
    else:
        for i in l[::-1]:
            if i < x:
                return l[::-1].index(i), i
x1 = []
y1 = [1,
      1.4,
      1.9]
s = 0
for i in range(2):
    x1.append(mr(s))
    s += 0.2
table = [x1, y1]
k = 1
while abs(table[-1][0]) > 0.01:
    dy = []
    for i in range(len(table[-1]) - k):
        dy.append(mr(table[-1][i + 1] - table[-1][i]))
    k = 1
    while len(dy) != len(table[-1]):
        dy.append("_")
        k += 1
    table.append(dy)
head = ['x', 'y']
head.extend([f"dy{i}" for i in range(1, len(table) - 1)])
row_format = '{:<15}' * len(head)
print(row_format.format(*head))
row_format = '{:<15}' * len(table)
for t in zip(*table):
    print(row_format.format(*t))

for t in table:
    while "_" in t:
        t.remove("_")

method = int(input("Первая или вторая формула Ньютона? 1/2 "))
if method == 1:
    x1 = float(input("Введите х: "))
    x, y, dy, dy2, dy3, q = symbols("x, y, dy, dy2, dy3, q")
    sym = [x, y, dy, dy2, dy3]
    f1 = y + q * dy

    for i in range(2, 4):
        qq = q
        for j in range(2, i + 1):
            qq *= q - j + 1
        f1 += ((qq) / math.factorial(i)) * sym[i + 1]
    pprint(f1)
else:
    x1 = float(input("Введите х: "))
    x, y, dy, dy2, dy3, q = symbols("x, y, dy, dy2, dy3, q")
    sym = [x, y, dy, dy2, dy3]
    f1 = y + q * dy
    for i in range(2, 4):
        qq = q
        for j in range(2, i + 1):
            qq *= q + j - 1
        f1 += ((qq) / math.factorial(i)) * sym[i + 1]
    pprint(f1)

ind, x0 = get_x0(x1, table[0], method)
print("x0 = ", x0)
q1 = (x1 - x0) / 0.005
print("q = ", mr(q1))
f = lambdify([y, dy, dy2, dy3, q], f1)
if method == 1:
    print(f"y({x0}) = ", mr(f(table[1][ind], table[2][ind], table[3][ind], table[4][ind], q1)))
else:
    if ind == 0:
        ind = -1
    else:
        ind = -1*ind
    print(f"y({x0}) = ", mr(f(table[1][ind], table[2][ind], table[3][ind], table[4][ind],q1)))