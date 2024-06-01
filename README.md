# Implementing Python Data Structures

![Default_title_picture_for_GitHub_repository_Python_Lists_Tuple_2](https://github.com/pgnikolov/implementing-python-data-structures/assets/151896883/e21970fa-c162-4dea-aef6-f5d46585b818)

### This repository provides a collection of Python functions for commonly used data structures, including:

* Lists
* Tuples
* Sets
* Dictionaries

Each data structure offers methods for performing essential operations like insertion, deletion, searching, and modification. 
The functions are designed to be clear, concise, and efficient.

## List

#### List Manipulation with Type Validation and Error Handling

This Python code provides a comprehensive set of functions for manipulating lists, offering robust data type handling and informative error messages.

1. Key Features:

   - Type Validation: Ensures that inserted elements match the user-specified data type using the check_type function. 
   - Error Handling: Provides informative error messages for various input errors, including invalid index, invalid type selection, and conversion failures.
   - User Input: Interactively prompts the user for the type and value to insert or modify.
   - Recursion: Offers the option to retry operations if errors occur.

2. Supported List Operations:
   - check_type(): Ensures that inserted elements match the user-specified data type.
   ```python 
   def check_type(data_type, el):
    """
    Checks the type of the `el` against the specified data type (`data_type`).
    Args:
        data_type (str): The expected data type (int, float, str, bool, list, tuple, set, dict).
        el: The element to be checked.
    Returns:
        The converted element if the type matches or raises an error.
    Raises:
        TypeError: If the data type is not valid or if the element cannot be converted to the specified type.
    """
   ```
   - linsert(lst): Inserts an element at a specified position.
   ```python
   def linsert(lst):
    """Inserts an element at the position by user choice in the list.
    Handles almost all kinds of data types for 'el' (int, float, str, bool, list, tuple, set, dict)
    based on user-selected type and provides informative error messages.
    Args:
        lst: The list to modify.
    Returns:
        lst with inserted el
    Raises:
        ValueError: If the provided type_el is invalid, if the index which user entered is not int.
        TypeError: If the user-selected type is invalid or conversion fails.
    """
   ```
   - lappend(lst): Adds an element to the end of the list.
   ```python
   def lappend(lst):
    """Inserts an element at the end of the list. Handles almost all kinds of data types for 'el'
    (int, float, str, bool, list, tuple, set, dict)
    based on user-selected type and provides informative error messages.
    Args:
        lst: The list to modify.
    Returns:
        lst with appended el
    Raises:
        ValueError: If the provided type_el is invalid, if the index which user entered is not int.
        TypeError: If the user-selected type is invalid or conversion fails.
    """
   ```
   - lextend(lst): Extends the list with elements from another iterable (list, tuple, string, dict).
   ```python
   def lextend(lst):
    """Extends the list with elements from the provided iterable.
    Handles iterables: lists, tuples, strings, dict.
    Args:
        lst: The list to modify.
    Returns:
        lst with extended elements
    Raises:
        TypeError: If the provided argument is not an iterable.
    """
   ```
   - lremove(lst): Remove by single value (first occurrence) or Remove all occurrences of entered value
   ```python
   def lremove(lst):
    """
    Removes elements from a list based on user-specified criteria:
    - value for single el to be removed
    - all occurancies of entered value to be removed
    Args:
        lst (list): The list from which elements will be removed.
    Returns:
        lst without removede element/elements
    Raises:
        ValueError: If an invalid choice is made for the removal method or
                    if the value to remove is not found in the list.
    """
   ```
   - lpop(lst): Remove last element of the list if index is not specified or an element which index user entered.
   ```python
   def lpop(lst):
    """
    Pop(remove) elements from a list based on user-specified criteria:
    - index for elements in the list or no index to pop the last element
    Args:
        lst (list): The list from which element will be removed.
    Returns:
        lst without removede element
    Raises:
        ValueError: If an invalid choice is made for the options
        IndexError: if the index to remove is not in the range of the list.
    """
   ``` 
   - lclear(lst): Removes all elements from a list using the clear() method.
   ```python
   def lclear(lst):
    """  Removes all elements from a list using the clear() method.
    Args:
        lst: The list from which elements will be removed.
    Returns:
        list: The modified list after clearing all elements.
    Raises:
        TypeError: If the input `lst` is not a list object.
    """
   ```
   - display_list_menu(): Displays a menu of common list operations.

3. (To be implemented):
   - finding indices, counting elements, sorting, reversing, and copying lists.


