# 삼각형 만들기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	11183	4901	4015	44.676%
# 문제
# 세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.

# 입력
# 첫째 줄에 빨대의 개수 N이 주어진다. N은 3보다 크거나 같고, 1,000,000보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 빨대의 길이가 한 줄에 하나씩 주어진다. 빨대의 길이는 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 삼각형 세 변의 길이의 합의 최댓값을 출력한다. 만약 삼각형을 만들 수 없으면 -1을 출력한다.

# 예제 입력 1 
# 3
# 1
# 2
# 3
# 예제 출력 1 
# -1
# 예제 입력 2 
# 3
# 1
# 2
# 2
# 예제 출력 2 
# 5
# 예제 입력 3 
# 6
# 2
# 3
# 2
# 3
# 2
# 4
# 예제 출력 3 
# 10
# 예제 입력 4 
# 5
# 4
# 5
# 6
# 7
# 20
# 예제 출력 4 
# 18

import sys
input = sys.stdin.readline

def solution(triangle):
    triangle.sort(reverse=True)

    an = 0
    an1 = 1
    an2 = 2
    while True:
        if triangle[an] < triangle[an1] + triangle[an2]:
            print(triangle[an] + triangle[an1] + triangle[an2])
            return
        else:
            an += 1
            an1 += 1
            an2 += 1

            if an2 == len(triangle):
                print(-1)
                return 

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(int(input()))
solution(triangle)