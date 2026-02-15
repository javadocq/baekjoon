# 구간 합 구하기 5
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	105834	49579	36460	44.725%
# 문제
# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7
# 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

# 출력
# 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

# 예제 입력 1 
# 4 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 2 2 3 4
# 3 4 3 4
# 1 1 4 4
# 예제 출력 1 
# 27
# 6
# 64
# 예제 입력 2 
# 2 4
# 1 2
# 3 4
# 1 1 1 1
# 1 2 1 2
# 2 1 2 1
# 2 2 2 2
# 예제 출력 2 
# 1
# 2
# 3
# 4

import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    two_array = []
    DP = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(n):
        temp_array = list(map(int, input().split()))
        two_array.append(temp_array)

    for i in range(1, n+1):
        for j in range(1, n+1):
            DP[i][j] = two_array[i-1][j-1] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())

        if x1 == x2 and y1 == y2:
            print(two_array[x2-1][y2-1])
            continue
        
        print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])
        
solution() 

# 1 2 3 4
# 2 5 7 10 
# 4 8 12

# DP[i][j] = two_array[i][j] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]
# sum(two_array[x1:x2][y1:y2]) == DP[x2][y2] - DP[x1-1][y2] - DP[x1][y-2]