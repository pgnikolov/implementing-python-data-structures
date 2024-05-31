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

    if data_type not in ('int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict'):
        raise ValueError(
            "Invalid type selection. Please choose from int, float, str, bool, list, tuple, set, dict")

    if data_type in ('int', 'float', 'str', 'bool'):
        # basic data types
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
            if el.lower() == 'true':
                el = True
            elif el.lower() == 'false':
                el = False
            else:
                raise TypeError("Invalid input. Enter a boolean value (True/False):")
    else:
        # complex data structures (list, tuple, set, dict)
        if data_type == 'list':
            # Check if the input is a valid list expression
            try:
                el = eval(el)
                if not isinstance(el, list):
                    raise TypeError("Invalid input for list. Enter a valid list expression.")
            except (SyntaxError, NameError):
                raise TypeError(f"Invalid input for list. Enter a valid list expression.")
        elif data_type == 'tuple':
            # Check if the input is a valid tuple expression
            try:
                el = eval(el)
                if not isinstance(el, tuple):
                    raise TypeError("Invalid input for tuple. Enter a valid tuple expression.")
            except (SyntaxError, NameError):
                raise TypeError(f"Invalid input for tuple. Enter a valid tuple expression.")
        elif data_type == 'set':
            # Check if the input is a valid set expression
            try:
                el = eval(el)
                if not isinstance(el, set):
                    raise TypeError("Invalid input for set. Enter a valid set expression.")
            except (SyntaxError, NameError):
                raise TypeError(f"Invalid input for set. Enter a valid set expression.")
        elif data_type == 'dict':
            # Check if the input is a valid dictionary expression
            try:
                el = eval(el)
                if not isinstance(el, dict):
                    raise TypeError("Invalid input for dictionary. Enter a valid dictionary expression.")
            except (SyntaxError, NameError):
                raise TypeError(f"Invalid input for dictionary. Enter a valid dictionary expression.")

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
        try:
            position = int(position_str)
            if position >= len(lst):
                print("The index you provided is bigger than lenght of your list. "
                      "Your value will be added at the end of your list")
        except ValueError:
            raise ValueError("Invalid index. Please enter a number.")

        # Convert to lowercase for matching
        type_el = input("Select type of value to insert: int, float, str, bool, list, tuple, set, dict: ").lower()
        valid_types = ("int", "float", "str", "bool", "list", "tuple", "set", "dict")

        if type_el not in valid_types:
            raise ValueError(f"Invalid type selection. Please choose from {', '.join(valid_types)}")

        # Validate position as integer
        el = input("Enter a value to be inserted: ")

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
        valid_types = ("int", "float", "str", "bool", "list", "tuple", "set", "dict")

        if type_el not in valid_types:
            raise ValueError(f"Invalid type selection. Please choose from {', '.join(valid_types)}")
        el = input("Enter a value to be appended: ")

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
        type_el = input("Select extension type - list, tuple, set, dict: ").lower()
        valid_types = ("list", "tuple", "set", "dict")

        if type_el not in valid_types:
            raise ValueError(f"Invalid type selection. Please choose from {', '.join(valid_types)}")

        if type_el == "dict":
            print("Only the keys of your dictionary will be added to the list")

        el = input("Enter a extension value: ")

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
    try:
        # Get user choice for removal method
        choice = input("Choose removal method (value, all): ").lower()

        # Remove by value (first occurrence)
        if choice == "value":
            # Get user input for value type
            type_el = input("Select type of value to remove (int, float, str, bool, list, tuple, set, dict): ").lower()

            # Check type and convert
            value = check_type(type_el, input("Enter the value to remove: "))

            try:
                if type_el == 'bool':
                    # Special handling for booleans to avoid confusion with 0 and 1
                    for index, el in enumerate(lst):
                        if isinstance(el, bool) and el == value:
                            lst.pop(index)
                            print("Element removed successfully!")
                            break
                else:
                    # Remove the first occurrence of the value
                    try:
                        lst.remove(value)
                    except ValueError:
                        print("Value not found in the list.")
                print("Element removed successfully!")
            except ValueError:
                print("Value not found in the list.")

        # Remove all occurrences
        elif choice == "all":
            # Get user input for value type
            type_el = input(
                "Select type of value to remove all occurrences of "
                "(int, float, str, bool, list, tuple, set, dict): ").lower()

            # Check type and convert
            value = check_type(type_el, input("Enter the value to remove all occurrences of: "))

            if type_el == 'bool':
                # Special handling for booleans to avoid confusion with 0 and 1
                lst = [el for el in lst if not (isinstance(el, bool) and el == value)]
            else:
                # Remove all occurrences of the value
                lst = [el for el in lst if el != value]

            print("All occurrences of the value removed successfully!")

        else:
            raise ValueError("Invalid choice. Please choose 'value' or 'all'.")

        return lst

    except ValueError as e:
        print("Error:", e)  # Handle various input errors
        if input("Would you like to try again removal? (y/n): ").lower() == 'y':
            return lremove(lst)
        else:
            return lst


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
