# 부분합 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.5 초 (하단 참고)	128 MB	137401	39753	28110	27.170%
# 문제
# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

# 출력
# 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

# 예제 입력 1 
# 10 15
# 5 1 3 5 10 7 4 9 2 8
# 예제 출력 1 
# 2

import sys
input = sys.stdin.readline

def solution(n, s, numbers):
    if sum(numbers) < s:
        print(0)
        return

    answer = 100001

    left = 0
    right = 0

    current_sum = numbers[0]

    while left <= right:
        if current_sum >= s:
            answer = min(answer, right-left+1)
            current_sum -= numbers[left]
            left += 1

        else:
            right += 1
            if right == n:
                break
            current_sum += numbers[right]
    
    print(answer)

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

solution(n,s,numbers)