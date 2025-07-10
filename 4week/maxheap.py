class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1   # 예를들어 배열 길이 3이면 마지막 요소의 인덱스가 2니까
        
        while cur_index != 1:    # 1인 경우에는 root node이므로 더 비교할 게 없음.
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break 
        
        return

'''
  3
 4 2
9
1. 배열 맨 뒤에 원소 추가
2. 부모와 비교해서 자기가 높으면 바꿈
3. 2의 과정을 부모가 더 크거나 루트 노드에 달했을때까지 반복
'''
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!