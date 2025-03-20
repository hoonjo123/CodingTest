# Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다.
# 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    cur_min = 0
    cur_max = len(array) -1
    cur_guess =  len(array) //2

    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess +1
        elif array[cur_guess] > target:
            cur_max = cur_guess -1
        cur_guess = (cur_min + cur_max) //2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)