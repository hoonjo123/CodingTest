# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 버블 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array) -i -1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]

# 시간복잡도는 O(N*N)
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))