# Q. 다음과 같이 문자열이 입력되었을 때,
# 회문이라면 True 아니라면 False 를 반환하시오.


input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i -1]:
            return False
    return True


print(is_palindrome(input))

def is_palinedrome_recursive(string):
    if len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))