from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    # 初始化链表并创建头结点
    def __init__(self):
        self.head = Node()

    # 头插
    def head_insert(self, new_data):
        new_node = Node(new_data)
        if self.length() == 1:
            self.head.next = new_node
        else:
            new_node.next, self.head.next = self.head.next, new_node

    # 尾插
    def tail_insert(self, new_data):
        new_node = Node(new_data)
        if self.length() == 1:
            self.head.next = new_node
        else:
            self.get_node(self.length() - 1).next = new_node

    # 指定位置插入结点
    def insert(self, new_data, position):
        new_node = Node(new_data)
        if position >= self.length() or position < 0:
            raise IndexError('超出链表长度！')
        elif position == 0:
            print('不能在头结点处插入新结点！')
        else:
            t = self.get_node(position - 1)
            new_node.next, t.next = t.next, new_node

    # 删除指定位置结点
    def remove(self, position):
        if position >= self.length() or position < 0:
            raise IndexError('超出链表长度！')
        elif position == 0:
            print('不能删除头结点！')
        else:
            pre, t = self.get_node(position - 1), self.get_node(position)
            pre.next, t.next = t.next, None

    def length(self):
        # 返回包括头结点在内的链表长度
        t, n = self.head, 1
        while t.next:
            t = t.next
            n += 1

        return n

    # 获取某个位置的结点2
    def get_node(self, position: int):
        if position >= self.length() or position < 0:
            raise IndexError('超出链表长度！')
        else:
            t = self.head
            for i in range(position):
                t = t.next

            return t

    def print(self):
        t = self.head.next
        res = 'head'
        while t:
            res += (' --> ' + str(t.data))
            t = t.next

        print(res)

    def reverse(self):
        link_re = LinkedList()
        for j in range(1, self.length()):
            link_re.head_insert(self.get_node(j).data)

        return link_re

    def init_list(self, data_list: List):
        link_li = LinkedList()
        for i in range(len(data_list)):
            link_li.tail_insert(data_list[i])

        return link_li


if __name__ == '__main__':
    link1 = LinkedList()

    for i in range(10):
        link1.tail_insert(i+1)

    print(link1.get_node(link1.length()-1).data, link1.length())
    link1.remove(link1.length()-1)
    print(link1.get_node(link1.length()-1).data, link1.length())
    # print(link1.get_node(link1.length()).data)
    # print(link1.get_node(-1).data)

    reverse_link1 = link1.reverse()
    reverse_link1.print()
    link1.print()

    list_link = link1.init_list([2, 4, 5, 6, 7, 8])
    list_link.print()

