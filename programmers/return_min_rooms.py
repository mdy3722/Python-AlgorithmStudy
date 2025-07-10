'''
호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

제한사항
1 ≤ book_time의 길이 ≤ 1,000
book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다
[대실 시작 시각, 대실 종료 시각] 형태입니다.
시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.
예약 시각이 자정을 넘어가는 경우는 없습니다.
시작 시각은 항상 종료 시각보다 빠릅니다.

[전략]
가장 빨리 퇴실해서 청소까지 끝난 놈을 먼저 찾아야 한다.
최소 힙을 이용해 항상 제일 빨리 비는 방이 맨 앞으로..
'''

book_time = [
    ["15:00", "15:30"],
    ["15:10", "15:40"],
    ["15:50", "16:00"]
]

# "HH:MM" 형태의 문자열을 분 단위로 변환하는 법
def to_minutes(time_str):
  h, m = map(int, time_str.split(":"))
  return h * 60 + m

import heapq

def solution(book_time):
  books = []
  for start, end in book_time:
    start_minutes = to_minutes(start)
    end_minutes = to_minutes(end) + 10
    books.append((start_minutes, end_minutes))

  books.sort(key=lambda x: x[0])    # 시작 시간 기준 정렬

  room_heap = []    # 각 방의 종료 시간

  for start, end in books:
    if room_heap and room_heap[0] <= start:     # 힙이 비어있는지도 체크
      heapq.heappop(room_heap)          # 방 재사용
    heapq.heappush(room_heap, end)      # 최소 힙, push = 새 방 예약

  return len(room_heap)

solution(book_time)
