from lists import Lists


class Stack(Lists):

    def __init__(self, elements):
        super().__init__(elements)

    def push(self, element):
        Lists.handle_insert(self, 0, element)
        return self.elements

    def pop(self):
        if len(self.elements) == 0:
            raise Exception("Stack is empty")
        return Lists.handle_pop(self)

    def peek(self):
        if len(self.elements) == 0:
            raise Exception("Stack is empty")
        return self.elements[0]


s = Stack('1, 2, 3, 4')
print(s.peek())
print(s.pop())
print(s.pop())
print(s.push('apple'))
