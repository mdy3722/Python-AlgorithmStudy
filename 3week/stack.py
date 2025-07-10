class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
'''
1. 한곳에서만 자료 넣고 뺄 수 있다.
2. LIFO
링크드 리스트 예시 
3->4->5

스택은 가장 위를 기억해야 한다. 즉 마지막에 추가한 놈이 head가 되게

5->4->3
여기서 pop을 하면 5를 빼고 4->3 
'''
class Stack:
  def __init__(self):
    self.head = None

  def push(self, value):
    new_head = Node(value)    # [3]이 있고, [4]를 추가
    new_head.next = self.head  # 4 -> 3
    self.head = new_head   # head, 즉 맨 위는 방금 넣은 4가,,
  
  def pop(self):
    if self.is_empty():
      return "stack is Empty"
    
    delete_head = self.head
    self.head = self.head.next
    return delete_head

  def peek(self):
    return self.head.data
  
  def is_empty(self):
    return self.head is not None
  

stack = Stack()
stack.push(4)
print(stack.head.data)
stack.push(5)
stack.push(7)
print(stack.peek())

''''
tip - 스택을 class로 구현안해도 파이썬에서 list로 쓸 수 있음
stack = []            # 빈 스택 초기화
stack.append(4)       # 스택 push(4)
stack.append(3)       # 스택 push(3)
top = stack.pop()     # 스택 pop
print(top)            # 3!
'''