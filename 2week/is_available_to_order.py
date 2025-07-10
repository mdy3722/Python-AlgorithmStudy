shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

"""내가 짠 코드 -> 이진탐색"""
"""
def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()   # -> O(NlogN)
    for i in range(len(shop_orders)):
      if find_is_available(menus, orders[i]):
         continue
      else:
         return False
    
    return True
"""

"""딩코님 코드 -> SET 활용"""
# 리스트보다 set이 탐색이 빠름름
def is_available_to_order(menus, orders):
    menus_set = set(menus)   # 정렬 + 중복 제거 O(N)
    for order in orders:    # O(M)
       if order not in menus_set:   # O(1)
          return False
    return True

def find_is_available(menus, order):
    index_min = 0
    index_max = len(menus) - 1
    current_guess = (index_max + index_min) // 2
    while index_min <= index_max:  
      if order == menus[current_guess]:
         return True
      elif order < menus[current_guess]:
         index_max = current_guess - 1
      else:
         index_min = current_guess + 1
      current_guess = (index_max + index_min) // 2

    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)