class Tuples:

    def __init__(self, elements: str):
        """
            Initialize the tuple with a string of elements separated by ", ".
        Args:
            elements (str): A string of elements, e.g. "elem1, elem2, elem3".
        """
        self.elements = tuple(elements.split(", "))

    def handle_count(self, element):
        """
            Count the occurrences of a value in the tuple.
        Args:
            element (str): The element which count we want to find.
        Returns:
            The number of occurrences of the element.
        """
        count = self.elements.count(element)
        return f"The count of {element} is {count}."

    def handle_index(self, element):
        """
            Find the index of a value in the tuple.
        Args:
            element (str): The element index we want to find.
        Raises:
            ValueError: If the element is not found in the tuple.
        Returns:
            The index of the element.
        """
        try:
            index = self.elements.index(element)
            return f"The index of {element} is {index}."
        except ValueError:
            return "Element not found in the tuple."
