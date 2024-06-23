class Dictionary:

    def __init__(self, elements: str):
        """
            Initialize the dictionary with a string of key-value pairs separated by ", " and ":".
        Args:
            elements (str): A string of key-value pairs ("key1: value1, key2: value2".)
        """
        self.elements = dict(item.split(": ") for item in elements.split(", "))

    def handle_pop(self, key):
        """
            Remove a specified key and return the corresponding value.
        Args:
            key (str): The key to remove.
        Returns:
            The value associated with the key, or a message if the key is not found.
        """
        try:
            return self.elements.pop(key)
        except KeyError:
            print(f"Provided key - {key} doesn't exsist")

    def handle_items(self):
        """
            Get all key-value pairs in the dictionary.
        Returns:
            A list of tuples containing key-value pairs.
        """
        return list(self.elements.items())

    def handle_get(self, key):
        """
            Get the value for a specified key in the dictionary.
        Args:
            key (str): The key to look up.
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self.elements.get(key)

    def handle_copy(self):
        """
            Create a shallow copy of the dictionary.
        Returns:
            A new dictionary that is a copy of the original.
        """
        return self.elements.copy()

    def handle_clear(self):
        """
            Remove all key-value pairs from the dictionary.
        Returns:
            A confirmation message.
        """
        self.elements.clear()
        return "The dictionary has been cleared."

    def handle_keys(self):
        """
            Get all keys in the dictionary.
        Returns:
            A list of all keys in the dictionary.
        """
        return list(self.elements.keys())

    def handle_values(self):
        """
            Get all values in the dictionary.
        Returns:
            A list of all values in the dictionary.
        """
        return list(self.elements.values())

    def handle_update(self, new_elements):
        """
            Update the dictionary with key-value pairs.
        Args:
            new_elements (str): The new key-value pairs to update the dictionary with.
        Returns:
            The updated dictionary.
        """
        new_elements_dict = dict(item.split(": ") for item in new_elements.split(", "))
        self.elements.update(new_elements_dict)
        return self.elements

    def handle_popitem(self):
        """
            Remove and return a key-value pair from the dictionary.
        Returns:
            The removed key-value pair, or a message if the dictionary is empty.
        """
        try:
            return self.elements.popitem()
        except KeyError:
            return "The dictionary is empty."

    def handle_setdefault(self, key, default=None):
        """
            Get the value for a specified key, and set it to a default value if the key is not found.
        Args:
            key (str): The key to look up.
            default: The default value to set if the key is not found.
        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        return self.elements.setdefault(key, default)


