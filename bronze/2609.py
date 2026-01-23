# 최대공약수와 최소공배수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	145077	84211	68590	57.777%
# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 예제 입력 1 
# 24 18
# 예제 출력 1 
# 6
# 72

import sys
input = sys.stdin.readline
import math

def solution(n,m):
    print(math.gcd(n,m))
    print(int(n*m / math.gcd(n,m)))
    

n, m = map(int, input().split())
solution(n,m)