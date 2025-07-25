#스택 버전
top_heights = [6, 9, 5, 7, 4]
'''
인덱스
0 1 2 3 4
v v v v

0 1 2 3 4
v v v

...
3210 => 4개
210 => 3개
10 => 2개
0 => 1개

for i in range(4, 0, -1): -> 4321
  for j in range(i - 1, -1, -1):  # i=4면 3210
'''

def get_receiver_top_orders(heights):
    result = [0] * len(heights)    # 0으로 초기화한 이유? 아무 신호도 받지 못하면 0을 반환해야 하므로
    
    while heights:    # 해당 스택이 비어있지 않다면 계속 반복해라
        height = heights.pop()
        
        for i in range(len(heights)-1, -1, -1):
            if heights[i] >= height:
                result[len(heights)] = i+1
                break
        
    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))