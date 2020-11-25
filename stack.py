class Stack:

    # 创建栈
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    # 进栈
    def push(self, data):
        if len(self.stack) >= self.limit:
            raise IndexError("超出栈的容量！")
        self.stack.append(data)

    # 出栈
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("这是一个空栈！")

    # 返回栈的大小
    def size(self):
        return len(self.stack)

    # 判断栈是否为空
    def is_empty(self):
        return not bool(self.stack)

    # 查看栈顶元素
    def peek(self):
        if self.stack:
            return self.stack[-1]

if __name__ == '__main__':
    stack1 = Stack()

    for i in range(10):
        stack1.push(i)

    print(stack1.pop(),stack1.peek(),stack1.is_empty(),stack1.size())
