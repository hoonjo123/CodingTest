# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

number = int(input())


def find_prime_list_under_number(number):
    primes = []
    for i in range(2, number):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                is_prime = False
                break


        if is_prime:
            primes.append(i)
    return primes

print(find_prime_list_under_number(number))