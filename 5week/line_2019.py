'''
Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다. 
이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 
게임이 끝나는데 걸리는 최소 시간을 구하시오.
조건은 다음과 같다.
코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 
이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 
즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게
임이 끝난다
c = 11 # 코니의 처음 위치
b = 2 # 브라운의 처음 위치
'''
# 시간     0   1   2    3     4 => 시간은 규칙적으로 값이 증가하니까 "배열"을 자료구조로.
# 코니    11  12  14   17    21
# 브라운   2  1    0
#                 2    => 이런 식으로 브라운의 위치가 시간마다 마구 잡이로 바뀜(불규칙). 이 경우에는 임의의 키값을 추가하기 쉬운 자료구조, 즉 딕셔너리를 사용해라.
#                 2    
#             3   2
#                 4
#                 6
#             4
# 경우의수가 너무 많다. 그리고 경우의수를 다 봐야한다. => BFS, DFS로 풀어야된다.
# "경우가 너무 많고, 수학적으로 풀 수 없을 거 같다" => BFS, DFS

# [{}, {}, {}, ..] : 각 시간마다 어느 위치에 있었는지를 저장하기 위해서 배열 안에 딕셔너리로!
# [0]초에 위치할 수 있었던 곳들
# [1]초에 위치할 수 있었던 곳들
# [2]초에 위치할 수 있었던 곳들

from collections import deque

c = 11
b = 2

def catch_me(cony_loc, brown_loc):
  time = 0
  queue = deque() # BFS를 사용하기 위함, 모든 경우의수를 확인하기 위해 BFS 사용
  queue.append((brown_loc, 0))   # 큐에 담길 것은 불규칙한 브라운의 위치와, 시간 (구해야 하는 것이 최소 시간이므로)

  # 10이라는 위치에 도달한 시간이 1초, 30초, 1000초면
  # visited[10] = {1: true, 30: true, 1000: ture}
  # ex) visited[3] : 3의 위치에 도달한 시간들의 모음집, dictionary = {5:treu, 9:true}
  visited = [{} for _ in range(200001)]  # [{}, {}, {}, .... 20만개]

  while cony_loc <= 200000:   # 탈출 조건 : 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
    cony_loc += time   # 1초일 때 1만큼, 2초일 때 2만큼, 3초일 때 3만큼 증가니까...

    if time in visited[cony_loc]:    # 현재의 시간은 코니의 시간과 동일하죠
      return time
    
    for i in range(0, len(queue)):    # while queue:를 안쓰고 for문을 왜 썼을까요? 시간별 비교를 맞추기 위해. 브라운과 코니의 시간이 엇갈리지 않게. 시간 비교 안전성을 위해 queue를 0서부터..
      current_position, current_time = queue.popleft()   # 초기: brown_loc, 0
      
      new_time = current_time + 1
      
      new_position = current_position - 1    # 브라운이 이동할 위치 = new_position
      if 0 <= new_position <= 200000:        # 해당 범위 내에서만 이동 가능
        visited[new_position][new_time] = True
        queue.append((new_position, new_time))
    
      new_position = current_position + 1
      if 0 <= new_position <= 200000:
        visited[new_position][new_time] = True
        queue.append((new_position, new_time))

      new_position = current_position * 2
      if 0 <= new_position <= 200000:
        visited[new_position][new_time] = True
        queue.append((new_position, new_time))
    
    
    time += 1


  return

print(catch_me(c, b)) # 5가 나와야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))
