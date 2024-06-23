from lists import Lists


class Stack(Lists):

    def __init__(self, elements):
        """
            Constructs all the necessary attributes for the stack object.
        Parameters:
            elements (str):  A string wiht comma-separeted values to be converted in list.
        """
        super().__init__(elements)

    def push(self, element):
        """
            Inserts an element at the top of the stack.
        Parameters:
            element (any) :The element to be inserted at the top of the stack.
        Returns:
            list: The updated list of stack elements.
        """
        Lists.handle_insert(self, 0, element)
        return self.elements

    def pop(self):
        """
            Removes and returns the element at the top of the stack.
         Raises:
            Exception: If the stack is empty.
         Returns:
             The element at the top of the stack.
         """
        if len(self.elements) == 0:
            raise Exception("Stack is empty")
        return Lists.handle_pop(self)

    def peek(self):
        """
            Returns the element at the top of the stack without removing it.
        Raises:
            Exception: If the stack is empty.
        Returns:
            The element at the top of the stack.
        """
        if len(self.elements) == 0:
            raise Exception("Stack is empty")
        return self.elements[0]

    def size(self):
        """
            Returns the number of elements in the stack.
        Returns:
            int: The number of elements in the stack.
        """
        return len(self.elements)
