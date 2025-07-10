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

# 유지보수성을 위한 함수 추출
def get_single_linked_list_sum(linked_list):
    sum = 0

    cur = linked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next

    return sum


def get_linked_list_sum(linked_list_1, linked_list_2):
    # sum_1 = 0
    # sum_2 = 0
    #
    # cur_1 = linked_list_1.head
    # while cur_1 is not None:
    #     sum_1 = sum_1 * 10 + cur_1.data
    #     cur_1 = cur_1.next
    #
    # cur_2 = linked_list_2.head
    # while cur_2 is not None:
    #     sum_2 = sum_2 * 10 + cur_2.data
    #     cur_2 = cur_2.next
    sum_1 = get_single_linked_list_sum(linked_list_1)
    sum_2 = get_single_linked_list_sum(linked_list_2)

    return sum_1 + sum_2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))