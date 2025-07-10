'''
청소기 방향 - 동서남북 중 하나
r : 북으로부터 떨어진 칸 개수
c : 서쪽으로부터 떨어진 칸 개수
지도의 각 칸은 (r,c)

1. 현재 위치 청소
2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례로 탐색
3. 왼쪽 방향 청소 x면 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행
4. 왼쪽 방향 청소할 공간이 없다면 그 방향으로 회전하고 2번으로,,
5. 네 방향 모두 청소 이미 완료 또는 벽인 경우, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로,,
6. 네 방향 모두 청소 완료, 벽, 뒤쪽 방향이 벽이라 후진도 못하면 작동을 멈춤
이미 청소된 칸을 또 청소하지 않으며 벽을 통과할 수 없다.

tip: 모두 탐색? BFS 또는 DFS구나
BFS에서 visited 기억나는가?
여기서는 청소한 칸을 기억하는 저장소가 필요요

바라보는 방향
d 0북 1동 2남 3서
      북(0)
 서(3)     동(1)
      남(2)

왼쪽: 북0->서3 동1->북0 남2->동1 서3->남2
if d==0:
  d==3
딩코님 코멘트 : (d + 3) % 4
def get_d_index_when_rotate_to_left(d):
  return (d + 3) % 4

후진은?
0->2
2->0
1->3
3->1

def get_d_index_when_go_back(d):
  return (d + 2) % 4

북 dr[0]=-1 dc[0]=0
동 dr[1]=0 dc[1]=1
서 dr[3]=0 dc[3]=-1
남 dr[2]=1 dc[2]=0

지도 - 빈칸 0 벽 1
청소기가 청소 하는 칸의 개수를 구하시오
'''

from collections import deque

def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4

def get_d_index_when_go_back(d):
    return (d + 2) % 4

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)    # 2차원 배열의 길이 = 행의 길이
    m = len(room_map[0]) # 2차원 배열의 첫번째 행의 길이 = 열의 길이
    count_of_departmets_cleaned = 1
    room_map[r][c] = 2
    queue = deque([[r, c, d]]) # BFS- 루트 노드를 큐에 넣는다.
    
    while queue:
        r,c,d = queue.popleft()
        temp_d = d

        for i in range(4): # 4번 반복 - 동서남북이니까
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_c < m and 0 <= new_r < n and room_map[new_r][new_c] == 0:
                count_of_departmets_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break
            elif i == 3:
                temp_d = get_d_index_when_go_back(d)
                new_r, new_c = r + dr[temp_d], c + dc[temp_d]
                queue.append([new_r, new_c, d])

                if room_map[new_r][new_c] == 1:
                    return count_of_departmets_cleaned


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))