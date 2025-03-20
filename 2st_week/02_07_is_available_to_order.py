# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때,
# 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# #배열 안에 들어가 있는 요소를 찾는 가장 효율적인 방법은 이진탐색이다.
# # O(NlogN) + O(M) * O(logN)
# def is_available_to_order(menus, orders):
#     menus.sort() #정렬을 하기 위해선 O(NlogN)
#     for order in orders :
#         if not is_target_existed(order, menus): # O(logN)
#             # target, 즉, 메뉴(array)안에 order가 존재하지 않으면 바로 False반환
#             return False
#     return True

######################## 집합자료형을 이용하면 좀 더 효율적으로 개선이 가능할 것 같다.
# 엄청나게 긴 배열이 있을때 [ 1,2,3,4,5,1,2,.......,999999] 이중에서 중복되지 않는 것들만 반환해주는게
# set자료형이다

# O(N) + O(M) * O(1) = O(N+M) 위 방법보다 시간복잡도 면에서 훨씬 효율적
def is_available_to_order(menus, orders):
    menus_set = set(menus) # set에 담을때 시간 복잡도 O(N)
    for order in orders: # 순회할때 O(M)
        if order not in menus_set: #if문 O(1)
            return False
    return True

def is_target_existed(target, array):
    cur_min = 0
    cur_max = len(array) -1
    cur_guess = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2

    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)