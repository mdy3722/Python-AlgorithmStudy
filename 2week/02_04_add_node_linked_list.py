class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        index_minus_1_node = self.get_node(index - 1)   # 근데 index가 0이라면 get_node의 -1...?
        # 0번째 인덱스에 새로운 노드를 넣으려면 헤드를 새로 지정,,, 헤드 넥스트는 옛날 헤드로,,,
        next_node = index_minus_1_node.next
        index_minus_1_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)

        prev_node.next = index_node.next

#head노드에서 어떻게 가지? cur변수를 이용해라
linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(0).data) # -> 5를 들고 있는 노드를 반환해야 합니다!

linked_list.print_all()