class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(5)
next_node = Node(3)
node.next = next_node

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head         # 맨앞

        while cur.next is not None:
            cur = cur.next      # 현재 칸에서 다음 칸으로 이동하는 행동

        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()