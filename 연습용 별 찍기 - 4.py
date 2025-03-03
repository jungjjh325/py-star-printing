"""
백준 문제가 아닌 연습용 코드

    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *

"""
T = int(input())

#위쪽 삼각형 별
for i in range(1, T + 1):
    print(" " * (T - i) + "*" * i)

#아래쪽 삼각형 별
for j in range(T - 1, 0, -1):
    print(" " * (T - j) + "*" * j)