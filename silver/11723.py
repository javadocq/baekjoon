# 집합 언어 제한
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1.5 초	4 MB (하단 참고)	157547	49509	36759	30.130%
# 문제
# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.
# 입력
# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# 출력
# check 연산이 주어질때마다, 결과를 출력한다.

# 예제 입력 1 
# 26
# add 1
# add 2
# check 1
# check 2
# check 3
# remove 2
# check 1
# check 2
# toggle 3
# check 1
# check 2
# check 3
# check 4
# all
# check 10
# check 20
# toggle 10
# remove 20
# check 10
# check 20
# empty
# check 1
# toggle 1
# check 1
# toggle 1
# check 1
# 예제 출력 1 
# 1
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 1
# 0

import sys
input = sys.stdin.readline

def solution(num):
    answer = set()
    
    for _ in range(num):
        data = input().split()
        if len(data) == 2:
            sentence = data[0]
            number = data[1]
        else:
            sentence = data[0]

        if sentence == "add":
            answer.add(int(number))
        elif sentence == "remove":
            if int(number) not in answer:
                continue
            answer.remove(int(number))
        elif sentence == "check":
            if int(number) in answer:
                print(1)
            else:
                print(0)
        elif sentence == "toggle":
            if int(number) in answer:
                answer.remove(int(number))
            else:
                answer.add(int(number))
        elif sentence == "all":
            answer = set(range(1,21))
        else:
            answer = set()

num = int(input())
solution(num)