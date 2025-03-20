# Q. 60에서 0까지 숫자를 출력하시오. (재귀)

def count_down(number):
    if number < 0:
        return
    print(number)
    count_down(number - 1)

number = int(input())
count_down(number)