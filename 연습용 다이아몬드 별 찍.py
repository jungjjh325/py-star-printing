"""
T = 3
  *
 ***
*****
 ***
  *

2 1 2
1 3 1
0 5 0
1 3 1
2 1 2
"""
T = int(input())

for i in range(T):
    print(" " * (T - i - 1) + "*" * (2 * i + 1))
for j in range(T - 2, -1, -1):
    print(" " * (T - j - 1) + "*" * (2 * j + 1))

"""
1
2 * 1 + 1 = 3
1 * 1 + 1 = 1
"""