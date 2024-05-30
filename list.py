def check_type(data_type, el):
    """
    Checks the type of the provided element (`el`) against the specified data type (`type_el`).
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
        user_choice = input("Enter a boolean value (True/False): ")
        if user_choice.capitalize() in ('True', 'False'):
            el = bool(user_choice)
        else:
            el = bool(input("Invalid input. Enter a boolean value (True/False):"))
    elif data_type in ('list', 'tuple', 'set', 'dict'):
        # Check if el is an instance of chosen data type
        if not isinstance(el, eval(data_type)):
            raise TypeError(
                f"Invalid input for {data_type}. Enter a valid {data_type} variable.")

    return el


def linsert_simple(lst):
    """Inserts an element at the position by user choice in the list.
    Handles (int, float, str, bool) data types for 'el'
    based on user-selected type and provides informative error messages.
    Args:
        lst: The list to modify.
    Raises:
        ValueError: If the provided type_el is invalid, if the index which user entered is not int
        TypeError: If the user-selected type is invalid or conversion fails, or in case the user
        wants to add data structers with the input, which are not asigned to variable.
    Returns:
        lst with inserted el
    """
    try:
        # Get user input for position and element type
        position_str = input(f"Enter an index between (0 and {len(lst) - 1}): ")
        # Convert to lowercase for matching
        type_el = input("Select type of value to insert: int, float, bool: ").lower()
        # Validate position (integer and within range)
        el = input("Enter a value to be inserted: ")
        try:
            position = int(position_str)
            if position >= len(lst):
                print("The index you provided is bigger than lenght of your list. "
                      "Your value will be added at the end of your list")
        except ValueError:
            raise ValueError("Invalid index. Please enter a number.")
        # check if user tried to insert data structure
        if el in ('[', '(', '{', '}', ')', ']'):
            print(f"Cannot directly insert Data Structure and it will be inserted as a string.")

        # Check the user choice and convert
        el = check_type(type_el, el)

        # Insert the element into the list
        lst.insert(position, el)
        print("Element inserted successfully!")
        return lst

    except (TypeError, ValueError) as e:
        print("Error:", e)  # Handle various input errors
        # Recursion for retrying
        if input("Would you like to try again insertion? (y/n): ").lower() == 'y':
            linsert_simple(lst)


def linsert_complex(lst, el):
    """Inserts an element at the position by user choice in the list.
    Handles complex data structures (list, tuple, set, dict).
    Args:
        lst: The list to modify.
        el: variable with asigned data structure to it
    Returns:
        lst with inserted el
    Raises:
        ValueError: If the provided type_el is invalid, if the index which user entered is not int.
        TypeError: If the user-selected type is invalid, conversion fails, or
                   if the user tries to directly insert a data structure without using an existing variable.
    """

    try:
        # Get user input for position and element type
        position_str = input(f"Enter an index between (0 and {len(lst) - 1}): ")
        # Convert to lowercase for matching
        type_el = input("Select type of value to insert: list, tuple, set, dict: ").lower()
        # Validate position (integer and within range)
        try:
            position = int(position_str)
            if position >= len(lst):
                print("The index you provided is bigger than lenght of your list. "
                      "Your value will be added at the end of your list")
        except ValueError:
            raise ValueError("Invalid index. Please enter a number.")

        # Check the user choice and handle complex data structures
        if type_el in ('list', 'tuple', 'set', 'dict'):
            # Check for list, tuple, set or tuple syntax
            check_type(type_el, el)
        # Insert the element into the list
        lst.insert(position, el)
        print("Element inserted successfully!")
        return lst
    except (TypeError, ValueError) as e:
        print("Error:", e)  # Handle various input errors
        # Recursion for retrying
        if input("Would you like to try again insertion? (y/n): ").lower() == 'y':
            linsert_complex(lst, el)


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
