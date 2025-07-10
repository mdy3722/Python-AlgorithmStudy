class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
    
    # 1. 루트와 맨 끝 위치 변경
    # 2. 바꾼 루트를 자식과 비교
    # 3. 내가 자식보다는 클때까지 혹은 바닥을 찍을 때까지 반복
    # 4. 마지막으로 1번의 루트 노드를 반환
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1] # 루트와 맨 마지막
        prev_max = self.items.pop()    # 마지막 아이 반환

        cur_index = 1
        

        while cur_index <= len(self.items) - 1:    # 맨 끝 인덱스 도달 전까지만 반복
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1

            max_index = cur_index
                  # 왼쪽 자식이 범위 내부에 있는지             # 부모와 비교  
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index
           
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break
            
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]

            cur_index = max_index

        return prev_max
        
        
        return 8  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]