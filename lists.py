class Lists:

    def __init__(self, elements: str):
        self.elements = elements.split(", ")

    def handle_append(self, new_element):
        """
            Appends a new element to the end of the list.
        Args:
            new_element (str): The element to be appended.
        Returns:
            The updated list.
        """
        self.elements.append(new_element)
        return self.elements

    def handle_extend(self, new_elements):
        """
            Extend a list by appending elements.
        Args:
            new_elements (list): The elements to be extended.
        Returns:
            The updated list.
        """
        self.elements.extend(new_elements)
        return self.elements

    def handle_insert(self, index: int, new_element):
        """
            Insert a new element into the list at a specified index.
        Args:
            index (int): The index to be inserted.
            new_element (str): The element to be inserted.
        Raises:
            ValueError: If the input index is not an integer.
        Returns:
            updated list
        """
        try:
            self.elements.insert(index, new_element)
            return self.elements
        except ValueError:
            print("Invalid index. Please enter an integer.")

    def handle_remove(self, element):
        """
            Remove an element from the list.
        Args:
            element (str): The element to be removed.
        Raises:
            ValueError: If the value is not found in the list.
        Returns:
            updated list
        """
        try:
            self.elements.remove(element)
            return self.elements
        except ValueError:
            print("Value not found in the list.")

    def handle_pop(self, index=None):
        """
            Pop an element at a specified index or the last element if no index is provided.
        Args:
            index(int): The index to be popped.(optional)
        Raises:
            IndexError: If the index is out of range.
            ValueError: If the input index is not an integer.
        Returns:
            updated list
        """
        try:
            if not index:
                self.elements.pop()
            else:
                self.elements.pop(index)
            return self.elements
        except (ValueError, IndexError):
            print("Invalid index. Please enter an integer.")

    def handle_clear(self):
        """
            Clear all elements from the list.
        Argss:
            list to clear.
        Returns:
            Print msg
        """
        self.elements.clear()
        if not self.elements:
            print("Empty list.")

    def handle_index(self, element):
        """
            Find the index of a specified value in the list.
        Args:
            element (str): The element which index we want to be found.
        Raises:
            ValueError: If the value is not found in the list.
        Returns:
            index of value
        """
        try:
            index = self.elements.index(element)
            return f"The index of {element} is {index}."
        except ValueError:
            print("Value not found in the list.")

    def handle_count(self, element):
        """
            Count the occurrences of a specified value in the list.
        Args:
            element (str): The element which index we want to count.
        Returns:
            number of ooccurrencess of a value
        """
        count = self.elements.count(element)
        return f"The count of {element} is {count}."

    def handle_sort(self):
        """
            Sort the list.
        Raises:
            TypeError: If the list contains elements of different data types.
        Returns:
            sorted list
        """
        try:
            self.elements.sort()
            return "Sorted list:", self.elements
        except TypeError:
            print("Cannot sort a list with different data types.")

    def handle_reverse(self):
        """
            Reverse the order of elements in the list.
        Returns:
            reversed list
        """
        self.elements.reverse()
        return f'Reversed list:", {self.elements}'

    def handle_copy(self):
        """
            Create a copy of the list.
        Returns:
            list copy
        """
        copied_list = self.elements.copy()
        return copied_list
