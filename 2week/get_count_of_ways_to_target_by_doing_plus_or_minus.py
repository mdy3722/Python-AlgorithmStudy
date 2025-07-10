"""도저히 못풀겠던 문제!!"""
numbers = [1, 1, 1, 1, 1]
target_number = 3

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N-1의 길이의 배열에서 마지막 요소를 더하거나 뺀 경우의 수를 추가하면 된다.
# 포인트 -> 재귀함수

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

  # 모든 경우의 수
    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
      if current_index == len(array):
        all_ways.append(current_sum)
        return

      get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
      get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index]) 

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    print("all_ways is", all_ways)

    target_count = 0

    for way in all_ways:
       if target == way:
          target_count += 1

    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!