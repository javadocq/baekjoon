# 과일 탕후루 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	1024 MB	20865	7709	6253	35.670%
# 문제
# 은하는 긴 막대에 
# $N$개의 과일이 꽂혀있는 과일 탕후루를 만들었습니다. 과일의 각 종류에는 
# $1$부터 
# $9$까지의 번호가 붙어있고, 앞쪽부터 차례로 
# $S_1, S_2, \cdots, S_N$번 과일이 꽂혀있습니다. 과일 탕후루를 다 만든 은하가 주문을 다시 확인해보니 과일을 두 종류 이하로 사용해달라는 요청이 있었습니다.

# 탕후루를 다시 만들 시간이 없었던 은하는, 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했습니다. 앞에서 
# $a$개, 뒤에서 
# $b$개의 과일을 빼면 
# $S_{a+1}, S_{a+2}, \cdots, S_{N-b-1}, S_{N-b}$번 과일, 총 
# $N-(a+b)$개가 꽂혀있는 탕후루가 됩니다. 
# $(0 \le a, b;$ 
# $a+b < N)$ 

# 이렇게 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하세요.

# 입력
# 첫 줄에 과일의 개수 
# $N$이 주어집니다. 
# $(1 \le N \le 200\,000)$ 

# 둘째 줄에 탕후루에 꽂힌 과일을 의미하는 
# $N$개의 정수 
# $S_1, \cdots, S_N$이 공백으로 구분되어 주어집니다. 
# $(1 \le S_i \le 9)$ 

# 출력
# 문제의 방법대로 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 첫째 줄에 출력하세요.

# 예제 입력 1 
# 5
# 5 1 1 2 1
# 예제 출력 1 
# 4
# 과일을 앞에서 
# $1$개, 뒤에서 
# $0$개의 과일을 빼면 남은 과일은 
# $1, 1, 2, 1$번 과일이 꽂혀있는 탕후루가 됩니다. 과일의 개수는 
# $4$개입니다.

# 예제 입력 2 
# 3
# 1 1 1
# 예제 출력 2 
# 3
# 탕후루가 이미 두 종류 이하의 과일로만 이루어져 있습니다.

# 예제 입력 3 
# 9
# 1 2 3 4 5 6 7 8 9
# 예제 출력 3 
# 2
# 과일을 앞에서 
# $3$개, 뒤에서 
# $4$개의 과일을 빼면 남은 과일은 
# $4, 5$번 과일이 꽂혀있는 탕후루가 됩니다. 과일의 개수는 
# $2$개입니다.

import sys
input = sys.stdin.readline

def solution():
    # 1. 입력부 예외 처리
    line1 = input().strip()
    if not line1: return
    n = int(line1)
    
    line2 = input().strip()
    if not line2: return
    fruit = list(map(int, line2.split()))

    # 2. 변수 초기화 (UnboundLocalError 방지)
    count = [0] * 10  # 과일 번호가 1~9이므로 리스트가 딕셔너리보다 빠름
    left = 0
    max_len = 0
    kind_count = 0

    # 3. 슬라이딩 윈도우 로직 (O(N))
    for right in range(n):
        r_fruit = fruit[right]
        
        # 새로운 종류의 과일이 들어온 경우
        if count[r_fruit] == 0:
            kind_count += 1
        count[r_fruit] += 1
            
        # 과일 종류가 2개를 초과하면 left를 이동시켜 종류를 줄임
        while kind_count > 2:
            l_fruit = fruit[left]
            count[l_fruit] -= 1
            if count[l_fruit] == 0:
                kind_count -= 1
            left += 1
            
        # 최대 길이 갱신
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            
    print(max_len)

if __name__ == "__main__":
    solution()