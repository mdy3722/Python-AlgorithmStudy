# "시간 경과"를 코드로 어떻게 표현하지?" → while, deque, 1초 단위 루프
# "상태를 유지해야 하는 대상이 있나?" → bridge 상태를 매번 갱신
# "조건에 따라 무언가를 넣거나 빼야 하는가?" → 무게 제한 → if로 분기
# "대기열처럼 순서를 지켜야 하는가?" → deque 활용
# 트럭도 보면 대기열에서 순서대로 줄 서있다가 앞에서부터 한 명씩 다리 건너는 거니까 큐!!!!


# 못풀었던 문제
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)   # 트럭이 줄 서서 대기 하는 걸 생각하면 큐로 처리해야겠다를 떠올려라. 꼭 그거 아니라도 pop(0)는 O(N)이 걸리지만 popleft()는 O(1)이니까 큐를 써라!!
    total_weight = 0
    
    while bridge: 
        time += 1
        finish = bridge.popleft()
        total_weight -= finish
        
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
    
    return time