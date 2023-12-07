class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
        
    def size(self):
        return len(self.items)
    
    def full(self):
        return len(self.items) == self.limit
    
    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target)
        else:
            return -1

