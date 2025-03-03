"""
T = 5
    1
   121
  12321
 1234321
123454321


"""
T = int(input())

# 빈칸 생서
for i in range(1, T + 1):
    print(" " * (T - i), end='')

    # 왼쪽 숫자 생성
    for j in range(1, i + 1):
        print(j, end='')

    # 오른쪽 숫자 생성
    for j in range(i - 1, 0, -1):
        print(j, end='')

    # 줄바꿈
    print()

"""
왼쪽 숫자
1, i + 1
1부터 시작, i가 1씩 증가
i = 1, T + 1
1부터 시작, 5칸을 생성

ex)
1, 2, 3 --- 증가 5까지
첫 째줄 0 + 1 = 1
둘 째줄 1 + 1 = 2
계속 증가 5까지 왼쪽 기준이니까 1~4까지 출력
처음 첫 째줄은 121 여기서부터 시작이다
이후에 123 1234 출력
"""