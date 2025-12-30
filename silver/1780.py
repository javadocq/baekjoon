# 종이의 개수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	55014	34016	25589	60.980%
# 문제
# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

# 출력
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

# 예제 입력 1 
# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1
# 예제 출력 1 
# 10
# 12
# 11

def solution():
    number = int(input())
    square_list = []

    for _ in range(number):
        square_list.append(list(map(int, input().split())))
    
    zero = 0
    minus_one = 0
    plus_one = 0

    def cut(x, y, size):
        nonlocal zero, minus_one, plus_one

        num = square_list[x][y]
        same = True

        for i in range(x, x + size):
            for j in range(y, y + size):
                if square_list[i][j] != num:
                    same = False
                    break

            if not same:
                break
        if same:
            if num == 0:
                zero += 1
            elif num == -1:
                minus_one += 1
            else:
                plus_one += 1
        
            return
        
        size = size // 3
        cut(x, y, size)
        cut(x + size, y, size)
        cut(x + (2 * size), y, size)
        cut(x, y + size, size)
        cut(x + size, y + size, size)
        cut(x + (2 * size), y + size, size)
        cut(x, y + (2 * size), size)
        cut(x + size, y + (2 * size), size)
        cut(x + (2 * size), y + (2 * size), size)
    
    cut(0, 0, number)

    print(minus_one)
    print(zero)
    print(plus_one)
        
solution()