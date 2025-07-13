# 서버가 증설되고 k시간 후 서버는 종료된다. 큐에 서버를 증설시키고 종료 시간이 되면 앞에서부터 popleft 처리를 한다.
'''
당신은 온라인 게임을 운영하고 있습니다. 
같은 시간대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가로 필요합니다. 
어느 시간대의 이용자가 m명 미만이라면, 서버 증설이 필요하지 않습니다. 
어느 시간대의 이용자가 n x m명 이상 (n + 1) x m명 미만이라면 최소 n대의 증설된 서버가 운영 중이어야 합니다. 
한 번 증설한 서버는 k시간 동안 운영하고 그 이후에는 반납합니다. 예를 들어, k = 5 일 때 10시에 증설한 서버는 10 ~ 15시에만 운영됩니다.

하루 동안 모든 게임 이용자가 게임을 하기 위해 서버를 최소 몇 번 증설해야 하는지 알고 싶습니다. 
같은 시간대에 서버를 x대 증설했다면 해당 시간대의 증설 횟수는 x회입니다.
'''

from collections import deque

def solution(players, m, k):
    total_count = 0
    running_server = deque()

    for i in range(len(players)):
        while running_server and running_server[0] <= i:
            running_server.popleft()

        required_count = players[i] // m
        running_count = len(running_server)

        if required_count > running_count:  
          add_count = required_count - running_count
          total_count += add_count
          for _ in range(add_count):
              running_server.append(i+k)


    return total_count


print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))   # 정답: 7
