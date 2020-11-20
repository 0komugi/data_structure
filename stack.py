
Class Stack(object):
  # 创建栈
  def __init__(self,limit=10):
    self.stack = []
    self.limit = limit
    
  # 进栈
  def push(self,data):
    if len(self.stack) >= self.limit:
      raise IndexError("超出栈的容量！")
    self.stack.append(data)
    
    # 出栈
    def pop(self):
      if self.stack:
        return self.stack。pop()
      else:
        raise IndexError("这是一个空栈！")

    
