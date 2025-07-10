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

    # def get_kth_node_from_last(self, k):
    #     # 구현해보세요!
    #     length = 1
    #     cur = self.head

    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    #     end_length = length - k
    #     cur = self.head
    #     for i in range(end_length):
    #         cur = cur.next
    #     return self.head

    """위 코드보다 개선된 코드"""
    """
    물론 위 코드와 아래 코드 모두 O(N)
    slow와 fast, 두 개의 포인트를 생각해보는 것은 어떨까?
    slow와 fast가 2만큼 떨어져있다고 하자.
    head
    slow          fast
          slow          fast 
                 slow          fast
    [6] -> [7] -> [8] -> [9] -> [10]

    fast가 끝에 도달하는 순간 slow의 위치가 끝에서부터 k번째이다라는 원리를 이용
    """
    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        slow = self.head
        fast = self.head

        for i in range(k):    # k만큼 fast가 먼저 앞서 가있어라
            fast = fast.next

        while fast is not None:   # fast가 마지막에 도달해야 하니까
            slow = slow.next
            fast = fast.next
        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!