# 영재의 시험
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	2247	1761	1311	78.222%
# 문제
# 컴퓨터공학과 학생인 영재는 이번 학기에 알고리즘 수업을 수강한다.

# 평소에 자신의 실력을 맹신한 영재는 시험 전날까지 공부를 하지 않았다.

# 당연하게도 문제를 하나도 풀지 못하였지만 다행히도 문제가 5지 선다의 객관식 10문제였다.

# 찍기에도 자신 있던 영재는 3개의 연속된 문제의 답은 같지 않게 한다는 자신의 비법을 이용하여 모든 문제를 찍었다.

# 이때 영재의 점수가 5점 이상일 경우의 수를 구하여라.

# 문제의 점수는 1문제당 1점씩이다.

# 입력
# 시험의 정답이 첫 줄에 주어진다.

# 출력
# 영재의 점수가 5점 이상일 경우의 수를 출력하여라.

# 예제 입력 1 
# 1 2 3 4 5 1 2 3 4 5
# 예제 출력 1 
# 261622

cnt = 0
answer = list(map(int, input().split()))

def dfs(idx, score, prev1, prev2):
    global cnt

    if idx == 10:
        if score >= 5:
            cnt += 1
        return 

    for pick in range(1,6):
        if pick == prev1 == prev2:
            continue

        new_score = score + (1 if pick == answer[idx] else 0)

        dfs(idx+1, new_score, pick, prev1)


def solution():
    dfs(0, 0, 0, 0)
    print(cnt)

solution()

