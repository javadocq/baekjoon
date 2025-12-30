# 행렬 곱셈
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	24140	16454	14350	69.280%
# 문제
# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 행렬 A의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다. 이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

# 예제 입력 1 
# 3 2
# 1 2
# 3 4
# 5 6
# 2 3
# -1 -2 0
# 0 0 3
# 예제 출력 1 
# -1 -2 6
# -3 -6 12
# -5 -10 18

def solution():
    n, m = map(int, input().split())
    nm_list = [list(map(int, input().split())) for _ in range(n)] # n x m 행렬

    m, k = map(int, input().split())
    mk_list = [list(map(int, input().split())) for _ in range(m)] # m x k 행렬

    nk_list = [] # n x k 행렬

    for i in range(n):
        for j in range(k):
            temp = 0
            for q in range(m):
                temp += nm_list[i][q] * mk_list[q][j]

            nk_list.append(temp)
        
    for i, j in enumerate(nk_list):
        if i != 0:
            if i % k == 0:
                print()
            
            print(j, end=" ")
        else:
            print(j, end=" ")

solution()

    
