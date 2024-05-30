def check_type(data_type, el):
    """
    Checks the type of the `el` against the  data type `data_type`.
    Args:
        data_type (str): The expected data type (int, float, str, bool, list, tuple, set, dict).
        el: The element to be checked.
    Returns:
        The converted element if the type matches or raise error
    Raises:
        TypeError: If the data type is not valid or if the element cannot be converted to the specified type.
    """

    if data_type not in ('int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict'):
        raise ValueError(
            "Invalid type selection. Please choose from int, float, str, bool")

    if data_type in ('int', 'float', 'str', 'bool'):
        # check basic data types
        if data_type == 'int':
            try:
                el = int(el)
            except ValueError:
                raise TypeError("Invalid input. Please enter a whole number.")
        elif data_type == 'float':
            try:
                el = float(el)
            except ValueError:
                raise TypeError("Invalid input. Please enter a floating-point value.")
        elif data_type == 'str':
            el = str(el)  # No conversion needed for strings
        elif data_type == 'bool':
            if el.capitalize() in ('True', 'False'):
                el = bool(el)
            else:
                el = bool(input("Invalid input. Enter a boolean value (True/False):"))
    else:
        # Handle complex data structures (list, tuple, set, dict)
        try:
            el = eval(el)
        except (SyntaxError, NameError):
            raise TypeError(f"Invalid input for {data_type}. Enter a valid {data_type} expression.")

    return el


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

    try:
        # Get user input for position and type
        position_str = input(f"Enter an index between (0 and {len(lst) - 1}): ")
        # Convert to lowercase for matching
        type_el = input("Select type of value to insert: int, float, str, bool, list, tuple, set, dict: ").lower()
        # Validate position as integer
        el = input("Enter a value to be inserted: ")
        try:
            position = int(position_str)
            if position >= len(lst):
                print("The index you provided is bigger than lenght of your list. "
                      "Your value will be added at the end of your list")
        except ValueError:
            raise ValueError("Invalid index. Please enter a number.")

        # Check the user choice and convert
        el = check_type(type_el, el)

        # Insert the element into the list
        lst.insert(position, el)
        print("Element inserted successfully!")
        return lst

    except (TypeError, ValueError) as e:
        print("Error:", e)  # various input errors
        # Reкуrsion for retrying
        if input("Would you like to try again insertion? (y/n): ").lower() == 'y':
            linsert(lst)


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
    try:
        type_el = input("Select type of value to insert: int, float, str, bool, list, tuple, set, dict: ").lower()
        # Validate position (integer and within range)
        el = input("Enter a value to be inserted: ")

        # Check the user choice and convert
        el = check_type(type_el, el)

        # Insert or append the element into the list
        lst.append(el)
        print("Element appended successfully!")
        return lst

    except (TypeError, ValueError) as e:
        print("Error:", e)  # Handle various input errors
        # Recursion for retrying
        if input("Would you like to try again insertion? (y/n): ").lower() == 'y':
            lappend(lst)


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
    try:
        # Get the iterable to extend from
        type_el = input("Select type of value to insert: list, tuple, set, dict: ").lower()
        if type_el == "dict":
            print("Only the keys of your dictionary will be added to the list")
        el = input("Enter a value to be inserted: ")

        # Check if it's an iterable
        el = check_type(type_el, el)

        # Extend the list with the iterable
        lst.extend(el)
        print("List extended successfully!")
        return lst

    except TypeError as e:
        print("Error:", e)  # Handle type errors
        # Recursion for retrying
        if input("Would you like to try again extension? (y/n): ").lower() == 'y':
            lextend(lst)


def display_list_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")
