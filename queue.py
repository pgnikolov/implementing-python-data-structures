from lists import Lists


class Queue(Lists):

    def __init__(self, elements: str):
        """
            Constructs all the necessary attributes for the queue object.
        Parameters:
            elements (str): A string with comma-separated values to be converted into a list.
        """
        super().__init__(elements)

    def handle_enqueue(self, new_element):
        """
            Adds an element to the end of the queue.
        Parameters:
            new_element (any): The element to be added to the queue.
        Returns:
            list: The updated list of queue elements.
        """
        Lists.handle_append(self, new_element)
        return self.elements

    def handle_dequeue(self):
        """
            Remove and return the first element from the queue.
        Raises:
            IndexError: If the queue is empty.
        Returns:
            The dequeued element.
        """
        if not self.elements:
            raise IndexError("Dequeue from an empty queue.")
        return self.elements.pop(0)

    def handle_peek(self):
        """
            Return the first element in the queue without removing it.
        Raises:
            IndexError: If the queue is empty.
        Returns:
            The first element in the queue.
        """
        if not self.elements:
            raise IndexError("Peek from an empty queue.")
        return self.elements[0]

    def handle_size(self):
        """
            Return the number of elements in the queue.
        Returns:
            The size of the queue.
        """
        return len(self.elements)

    def handle_rotate(self, steps):
        """
            Rotate the elements of the queue by a specified number of steps.
        Args:
            steps (int): The number of steps to rotate. Positive steps rotate to the right,
                         negative steps rotate to the left.
        Returns:
            The rotated queue.
        """
        if not self.elements:
            return self.elements

        steps = steps % len(self.elements)
        if steps > 0:
            self.elements = self.elements[-steps:] + self.elements[:-steps]
        elif steps < 0:
            steps = abs(steps)
            self.elements = self.elements[steps:] + self.elements[:steps]

        return self.elements
