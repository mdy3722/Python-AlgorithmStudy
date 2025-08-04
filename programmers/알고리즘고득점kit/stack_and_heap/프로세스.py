# 나의 풀이 <- 이것도 도움 받은 풀이
# 시간 복잡도 -> O(N^2)
from collections import deque

def solution(priorities, location):
    queue = deque((idx, p) for idx, p in enumerate(priorities))
    # (3,2) (0,2) (1,1) / (2,3) 
    order = 0
    
    while queue:
        curr = queue.popleft()
        if any(curr[1] < q[1] for q in queue):
            queue.append(curr)
        else:
            order += 1
            if curr[0] == location :
                return order

# 개선된 풀이
# priorities = [2, 1, 3, 2]
# sorted_priorities = [3, 2, 2, 1]
# sorted_priorities는 앞에서부터 차례로 출력될 우선순위 순서
# 출력된 프로세스 수가 0이면 → 0번째 우선순위(=3) 출력될 차례
# 출력된 프로세스 수가 1이면 → 1번째 우선순위(=2) 출력될 차례
# 즉, order가 곧 정렬된 우선순위 배열의 인덱스가 됨....
from collections import deque

def solution(priorities, location):
    queue = deque((idx, p) for idx, p in enumerate(priorities))
    sorted_priorities = sorted(priorities, reverse=True)   # 항상 제일 앞이 우선순위. any 연산 필요 없이 최댓값과 비교하면 됨. O(nlogn)
    order = 0   # 출력된 개수 = 정렬된 우선순위의 현재 위치

    while queue:  # O(n)
        idx, priority = queue.popleft()
        if priority < sorted_priorities[order]:
            queue.append((idx, priority))  # 더 큰 거 남아 있으니까 뒤로 보냄
        else:
            order += 1
            if idx == location:
                return order
