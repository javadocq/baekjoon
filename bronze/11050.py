# 이항 계수 1
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	92122	59786	51747	64.663%
# 문제
# 자연수 
# \(N\)과 정수 
# \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 
# \(N\)과 
# \(K\)가 주어진다. (1 ≤ 
# \(N\) ≤ 10, 0 ≤ 
# \(K\) ≤ 
# \(N\))

# 출력
 
# \(\binom{N}{K}\)를 출력한다.

# 예제 입력 1 
# 5 2
# 예제 출력 1 
# 10

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
dp = [None] * (N + 1)
dp[0] = 0
dp[1] = 1

def factorial(num):
    if dp[num] != None:
        return dp[num]
    
    if num == 1:
        return 1
    
    dp[num] = num * factorial(num-1)
    return dp[num]

def solution(N, K):
    upper = factorial(N)
    lower = factorial(N-K) * factorial(K)

    print(int(upper / lower))

if K == 0 or N == K:
    print(1)
else:
    solution(N, K)
