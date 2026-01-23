# FizzBuzz 스페셜 저지다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.5 초	1024 MB	21335	12908	11684	60.617%
# 문제
# FizzBuzz 문제는 
# $i = 1, 2, \cdots$ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

#  
# $i$가 
# $3$의 배수이면서 
# $5$의 배수이면 “FizzBuzz”를 출력합니다.
#  
# $i$가 
# $3$의 배수이지만 
# $5$의 배수가 아니면 “Fizz”를 출력합니다.
#  
# $i$가 
# $3$의 배수가 아니지만 
# $5$의 배수이면 “Buzz”를 출력합니다.
#  
# $i$가 
# $3$의 배수도 아니고 
# $5$의 배수도 아닌 경우 
# $i$를 그대로 출력합니다.
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?

# 입력
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다. 각 문자열의 길이는 
# $8$ 이하입니다. 입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.

# 출력
# 연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요.

# 예제 입력 1 
# Fizz
# Buzz
# 11
# 예제 출력 1 
# Fizz
# 예제 입력 2 
# 980803
# 980804
# FizzBuzz
# 예제 출력 2 
# 980806
# 힌트
# FizzBuzz 문제의 
# $i=1, \cdots, 20$에 대한 출력은 다음과 같습니다.

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz

import sys
input = sys.stdin.readline

def solution(first_sen, second_sen, third_sen):
    answer = [first_sen, second_sen, third_sen]
    for sen in answer:
        if sen != "Fizz" and sen != "Buzz" and sen != "FizzBuzz":
            temp = int(sen)
            if sen == first_sen:
                result = temp + 3
            elif sen == second_sen:
                result = temp + 2
            else:
                result = temp + 1

            if result % 3 == 0:
                if result % 5 == 0:
                    print("FizzBuzz")
                else:
                    print("Fizz")
            elif result % 5 == 0 :
                print("Buzz")
            else:
                print(int(result))
            
            break

    answer = 0

first_sen = input().strip()
second_sen = input().strip()
third_sen = input().strip()
solution(first_sen, second_sen, third_sen)