
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def get_stack(self):
        return self.items


s = Stack()
s.push('1')
s.push('2')
s.push('3')
print(s.get_stack())
print('peek element:', s.peek())
s.pop()
print(s.get_stack())