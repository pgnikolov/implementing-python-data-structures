def linsert(lst):
    """Inserts an element at the position by user choice in the list.
    Handles almost all kindd of data types for 'el' (int, float, str, bool, list, tuple, set, dict)
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
        type_el = input("Select type of value to insert: int, float, str, bool, list, tuple, set, dict): ").lower()
        # Validate position (integer and within range)
        el = None
        try:
            position = int(position_str)
            if position >= len(lst):
                print("The index you provided is bigger than lenght of your list. "
                      "Your value will be added at the end of your list")
        except ValueError:
            raise ValueError("Invalid index. Please enter a number.")
        # check the user choice
        if type_el not in ('int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict'):
            raise ValueError(
                "Invalid type selection. Please choose from int, float, str, bool, list, tuple, set, or dict.")
        # convert element based on user-selected type
        if type_el == 'int':
            el = int(input("Please enter a whole number: "))
        elif type_el == 'float':
            el = float(input("Enter a floating-point value: "))
            el = float(el)
        elif type_el == 'str':
            el = str(input("Enter a string value: "))
            el = str(el)
        elif type_el == 'bool':
            user_choice = input("Enter a boolean value (True/False) or use an bool variable: ").lower()
            if user_choice in ('true', 'false'):
                el = bool(user_choice)
            # check if user_choice is defined as a boolean
            elif user_choice is not None and type(user_choice) is bool:  # Check if user_choice is defined as a boolean
                el = user_choice
            else:
                # if neither user input nor rain is available, prompt again for boolean value
                el = bool(input("Invalid input. Enter a boolean value (True/False):"))
        elif type_el in ('list', 'tuple', 'set', 'dict'):
            el = input(f"Enter the existing {type_el} variable variable (my_listm, my_dict ....): ")
            # check for list, tuple, set or tuple syntax
            if el in ('[', '(', '{', '}', ')', ']'):
                raise TypeError(f"Cannot directly insert {type_el} . Please use an existing {type_el} variable.")
        # insert the element into the list
        lst.insert(position, el)
        print("Element inserted successfully!")
        return lst
    except (TypeError, ValueError) as e:
        print("Error:", e)  # Handle various input errors
        # reкursion to start again if user wants
        if input("Would you like to try again insertion? (y/n): ").lower() == 'y':
            linsert(lst)


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
