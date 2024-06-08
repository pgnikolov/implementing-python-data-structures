# Implementing Python Data Structures 🧱

<img src="https://github.com/pgnikolov/implementing-python-data-structures/assets/151896883/e21970fa-c162-4dea-aef6-f5d46585b818" width="700" height="400"/>

### This repository provides a collection of Python functions for commonly used data structures, including:

* Lists

Coming soon ⏳

* Tuples
* Sets
* Dictionaries

Each data structure offers methods for performing essential operations like insertion, deletion, searching, and modification.
The functions are designed to be clear, concise, and efficient.

## List

#### List Manipulation with Type Validation and Error Handling

This Python code provides a comprehensive set of functions for manipulating lists.

1. 🧰 Key Features: 

- Error Handling: Provides informative error messages for various input errors, including invalid index, invalid type selection, and conversion failures.
- User Input: Interactively prompts the user for the type and value to insert or modify.
- 
2. 🛠️ Supported List Operations: 
  
    - def handle_insert(lst): Inserts an element at a specified position.
   ```python
	"""
		Insert a new element into the list at a specified index.
	Args:
		list to insert the element into.
	Raises:
		ValueError: If the input index is not an integer.
	Returns:
		updated list
	"""
   ```
    - handle_append(lst): Adds an element to the end of the list.
   ```python
   """
   		Appends a new element to the end of the list.
	Args:
		list to modify.
	Returns:
		The updated list.
	"""
   ```
    - handle_extend(lst): Extends the list with elements from another iterable (list, tuple, string, dict).
   ```python
	"""
   		Extend a list by appending elements from iterable.
	Args:
		list to modify.
	Returns:
		The updated list.
	"""
   ```
	- handle_remove(lst):  Remove by single value (first occurrence)
   ```python
	"""
		Remove an element from the list.
	Args:
		list to remove the element from.
	Raises:
		ValueError: If the value is not found in the list.
	Returns:
		updated list
	"""
   ```
    - handle_pop(lst): Remove last element of the list if index is not specified or an element which index user entered.
   ```python
	"""
		Pop an element at a specified index or the last element if no index is provided.
	Args:
		list to pop the element from.
	Raises:
		IndexError: If the index is out of range.
		ValueError: If the input index is not an integer.
	Returns:
		updated list
	"""
   ``` 
    - handle_clear(lst): Removes all elements from a list using the clear() method.
   ```python
	"""
		Clear all elements from the list.
	Argss:
		list to clear.
	Returns:
		empty list
	"""
   ```
    - handle_index(lst): Find an index of given element.
   ```python
	"""
		Find the index of a specified value in the list.
	Args:
		list to search for the value.
	Raises:
		ValueError: If the value is not found in the list.
	Returns:
		index of value
	"""
   ```
    - handle_count(lst): Counts the occurrences of a value in a list.
   ```python
	"""
		Count the occurrences of a specified value in the list.
	Args:
		list to count the occurrences of the value.
	Returns:
		number of ooccurrencess of a value
	"""
   ```
    - handle_sort(lst): Sorts a list.
   ```python
	"""
		Sort the list.
	Argss:
		list to sort.
	Raises:
		TypeError: If the list contains elements of different data types.
	Returns:
		sorted list
	"""
   ```
   - handle_reverse(lst)
   ```python
	"""
		Reverse the order of elements in the list.
	Args:
		list to reverse.
	Returns:
		reversed list
	"""
   ```
   - handle_copy(lst):
   ```python
	"""
		Create a copy of the list.
	Argss:
		list to copy.
	Returns:
		list copy
	"""
   ```
   - display_list_menu(): Displays a menu of common list operations.

#### Installation ⚙️

To use these functions, simply clone the repository and import the desired functions into your Python script.
```bash
git clone https://github.com/pgnikolov/implementing-python-data-structures.git
cd implementing-python-data-structures
```
#### Contributing 🤝
Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

#### License 📝
This project is licensed under the MIT License.

#### Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)

