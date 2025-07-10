# 1. 좌석은 한줄, 왼부터 1번~N번
# 2. 자기 입장권에 표시되어 있는 좌석에 앉는다.
# 3. 단 자신의 바로 왼쪽, 오른쪽 좌석으로는 자리를 옮길 수 있다.
# 4. vip 회원 - 반드시 자기 좌석에 앉는다. 옆좌석으로 옮길 수 없다.
# 5. 총 좌석 수, vip 회원 번호 주어짐
# 6. 좌석에 앉는 서로 다른 방법의 가짓수 반환
# [1 2 3 4 5 6 7 8 9]
# vip가 4면 -> 4를 기준으로 왼쪽 3은 그대로, 혹은 왼쪽 한칸
# 4를 기준으로 오른쪽인 5는 그대로, 혹은 오른쪽으로 한칸
# 7을 기준으로 6은 그대로, 혹은 왼쪽 / 8은 그대로 혹은 오른쪽
# 결국 vip 인덱스를 기준으로 왼쪽과 오른쪽의 위치를 지정해주고, 만약 줄의 첫, 혹은 마지막 인덱스인지도 고려
'''
123 56 89
1. 숫자를 써보면서 발견해봐라
[1,2] -> [2,1] [1,2] => 2
[1,2,3] -> [1,2,3] [2,1,3] [1,3,2] => 3
[1,2,3,4] -> [1,2,3,4] [2,1,3,4] [1,2,4,3] [1,3,2,4] [2,1,4,3] => 5
[1,2,3,4,5] -> [1,2,3,4,5] [2,1,3,4,5] [1,2,4,3,5] [1,2,3,5,4] [2,1,4,3,5] [2,1,3,5,4] [1,3,2,4,5] [1,3,2,5,4] => 8

2 3 5 8 => 음... 피보나치? 1 1 2 3 5 8...
왤까?

2. 점화식
좌석이 n개
1 2 3 ... n-2 n-1 n
n번째 티켓을 가진 사람이 앉을 수 있는 방법?
1. n번째 좌석에 앉거나
-> 좌석은 n-1개가 남아있고, 사람도 n-1번째 티켓까지 가진 사람이 있는 상황.

2. n-1 번째 좌석에 앉거나
n-1번째 티켓을 가진 사람은 반드시 n번째 좌석에 앉아야만 한다.
-> 좌석은 n-2개가 남아있고, 사람도 n-2번째 티켓까지 가진 사람이 있는 상황

f(n) = n명의 사람들을 좌석에 배치하는 방법
f(n) = f(n-1) + f(n-2)

결론 [1,2,3,4,5,6,7,8,9]
4와 7은 고정 -> [1,2,3] [5,6] [8,9]
f(3) x f(2) x f(2)
'''

memo = {
  1 : 1,
  2 : 2
}

# 피보나치와 다른 점 => f(2)가 1이 아님. [1,2] -> [1,2] [2,1]라서 2임

def fib(n, memo):
  if n in memo:
    return memo[n]
  
  nth_fib = fib(n-1, memo) + fib(n-2, memo)
  memo[n] = nth_fib

  return nth_fib


seat_count = 9
vip_seat_array = [4, 7]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
  all_ways = 1
  current_index = 0

  for fixed_seat in fixed_seat_array:
    fixed_seat_index = fixed_seat - 1
    count_of_ways = fib(fixed_seat_index - current_index, memo)
    all_ways *= count_of_ways
    current_index = fixed_seat_index + 1

  if current_index < seat_count:
    all_ways *= fib(seat_count - current_index, memo)

  return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))