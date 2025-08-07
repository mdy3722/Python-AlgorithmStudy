# 내 풀이
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    
    return answer


# 과거의 주식 가격을 살피는 것은 어떤지? 
# 가격이 떨어지는 지점에서 과거 가격들과 비교하자!
# 가격이 떨어졌을 때 과거로 거슬러 올라가면서...
# 스택 - 나중에 추가한 놈이 먼저 나옴. 가까운 과거의 가격을 먼 과거의 가격보다 먼저 접근할 수 있다는 말
# 따라서 이 문제는 스택이 딱이다.
"""
prices = [100, 300, 500, 400, 200]
stack = [0, 1] # 인덱스
top = 2
result[2] = 3 - 2 = 1
stack[top] 300 < 400    stack = [0, 1]
top = 3
result[3] = 4 - 3 = 1
top = 1
result[1] = 4 - 1 =3
stack = [0] -> stack = [0, 4]
len(prices) - i - 1
"""
# 시간 복잡도 - O(2N)
def solution(prices):
    result = [-1] * len(prices)   # -1 : 아직 가격 떨어지지 않는 구간은 못구했다.
    stack = []
    for cur in range(len(prices)):
        while stack and prices[stack[-1]] > prices[cur]:   # 스택이 있다면 -> 값 비교
            pas = stack.pop()    # 가격이 게속 떨어지면 pop을 계속 => for 안에 while이 있다고 O(N^2)이 아니라는 뜻!
            result[pas] = cur - pas
        stack.append(cur)   # 가격이 계속 오르면 계속 append
    
    for i in stack:
        result[i] = len(prices) - i - 1

    return result

# 큐 버전
from collections import deque

def get_price_not_fall_periods(prices):
    result = []
    prices_queue = deque(prices)

    while prices_queue:
        period = 0
        current_price = prices_queue.popleft()
        for next_price in prices_queue:
            if current_price <= next_price:
                period += 1
            else:
                period += 1
                break
        result.append(period)
    
    return result