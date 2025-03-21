# Q. 음이 아닌 정수들로 이루어진 배열이 있다.
# 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers,
# 타겟 넘버 target_number이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    def dfs(index, current_sum):
        # 배열 끝까지 탐색했을 때
        if index == len(array):
            return 1 if current_sum == target else 0

        # 현재 숫자를 더하는 경우와 빼는 경우를 모두 탐색
        return (dfs(index + 1, current_sum + array[index])
                + dfs(index + 1, current_sum - array[index]))

    return dfs(0, 0)


# 테스트 실행
numbers = [1, 1, 1, 1, 1]
target_number = 3
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!