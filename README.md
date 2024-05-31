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
   - linsert(lst): Inserts an element at a specified position.
   - lappend(lst): Adds an element to the end of the list.
   - lextend(lst): Extends the list with elements from another iterable (list, tuple, string, dict).
   - lremove(lst): Remove by single value (first occurrence) or Remove all occurrences of entered value
   - lpop(lst): Remove last element of the list if index is not specified or an element which index user enter
   - display_list_menu(): Displays a menu of common list operations.

3. (To be implemented)  Functions for:
   - clearing, finding indices, counting elements, sorting, reversing, and copying lists.


