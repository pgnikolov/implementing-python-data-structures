class Sets:

    def __init__(self, elements: str):
        """
            Initialize the set with a string of elements separated by ", ".
        Args:
            elements (str): A string of elements, e.g. "elem1, elem2, elem3".
        """
        self.elements = set(elements.split(", "))

    def handle_add(self, new_element):
        """
            Add a new element to the set.
        Args:
            new_element (str): The element to be added.
        Returns:
            The updated set.
        """
        self.elements.add(new_element)
        return self.elements

    def handle_remove(self, element):
        """
            Remove an element from the set.
        Args:
            element (str): The element to be removed.
        Raises:
            KeyError: If the element is not found in the set.
        Returns:
            The updated set.
        """
        try:
            self.elements.remove(element)
            return self.elements
        except KeyError:
            return "Element not found in the set."

    def handle_discard(self, element):
        """
            Discard an element from the set.
        Args:
            element (str): The element to be discarded.
        Returns:
            The updated set.
        """
        self.elements.discard(element)
        return self.elements

    def handle_pop(self):
        """
            Remove and return an arbitrary element from the set.
        Raises:
            KeyError: If the set is empty.
        Returns:
            The removed element.
        """
        try:
            return self.elements.pop()
        except KeyError:
            return "The set is empty."

    def handle_clear(self):
        """
            Remove all elements from the set.
        Returns:
            A confirmation message.
        """
        self.elements.clear()
        return "The set has been cleared."

    def handle_union(self, values_for_union: str):
        """
            Return the union of the set and another set.
        Args:
            values_for_union (str): Values for the union, commma-separated.
        Returns:
            The union of the two sets.
        """
        set_for_union = set(values_for_union.split(","))
        return self.elements.union(set_for_union)

    def handle_intersection(self, intersection_values: str):
        """
            Return the intersection of the set and another set.
        Args:
            intersection_values (str): Values for the intersection, commma-separated.
        Returns:
            The intersection of the two sets.
        """
        set_for_intersection = set(intersection_values.split(","))
        return self.elements.intersection(set_for_intersection)

    def handle_difference(self, values_difference: str):
        """
            Return the difference of the set and another set.
        Args:
            values_difference (str): Values for the difference, commma-separated.
        Returns:
            The difference of the two sets.
        """
        set_for_difference = set(values_difference.split(","))
        return self.elements.difference(set_for_difference)

    def handle_copy(self):
        """
            Create a copy of the set.
        Returns:
            A new set that is a copy of the original.
        """
        return self.elements.copy()

    def handle_issuperset(self, values_for_issuperset: str):
        """
            Test if the set is a superset of another set.
        Args:
            values_for_issuperset (str): Values for the issuperset, commma-separated.
        Returns:
            True if the set is a superset, otherwise False.
        """
        set_for_superset = set(values_for_issuperset.split(","))
        return self.elements.issuperset(set_for_superset)

    def handle_issubset(self, values_for_issubset: str):
        """
            Test if the set is a subset of another set.
        Args:
            values_for_issubset (str) : Values for the issubset, commma-separated.
        Returns:
            True if the set is a subset, otherwise False.
        """
        set_for_issubset = set(values_for_issubset.split(","))
        return self.elements.issubset(set_for_issubset)

    def handle_symmetric_difference(self, set_for_symmetric_str: str):
        """
            Return the symmetric difference of two sets as a new set.
        Args:
            set_for_symmetric_str (str): Values for set for the symmetric difference, commma-separated.
        Returns:
            A new set with elements in either set but not both.
        """
        set_for_symmetric = set(set_for_symmetric_str.split(","))
        return self.elements.symmetric_difference(set_for_symmetric)
