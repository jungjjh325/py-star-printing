"""
백준 문제가 아님 임의로 작성한 연습용 코드

*       i + 1
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

for i in range(T):
    print("*" * (i + 1))
for j in range(1, T):
    print("*" * (T - j))


