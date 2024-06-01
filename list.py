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
				print("Your index is bigger than lenght of your list. Value will be added at the end of your list")
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


def lpop(lst):
	"""
	Pop(remove) elements from a list based on user-specified criteria:
	- index for elements in the list or no index to pop the last element
	Args:
		lst (list): The list from which element will be removed.
	Returns:
		lst without removed element
	Raises:
		ValueError: If an invalid choice is made for the options
		IndexError: if the index to remove is not in the range of the list.
	"""
	if len(lst) == 0:
		print("You can't perform pop from an empty list")
		return lst

	try:
		user_choice = input("Do you want to remove the last element of the list? (y/n): ").lower()
		if user_choice == "y":
			lst.pop()
		elif user_choice == "n":
			index_check = input("Do you know the index of the element you want to remove? (y/n): ").lower()
			if index_check == "n":
				print("On next lines you will see 'Index' - 'Element' for your list")
				for i in range(len(lst)):
					print(f"{i} - {lst[i]}")

			num_el = int(input("Enter index number: "))
			if num_el < 0 or num_el >= len(lst):
				raise IndexError("Invalid index.")
			lst.pop(num_el)
		else:
			raise ValueError("Invalid option selected")
	except (IndexError, ValueError) as e:
		print("Error:", e)
		if input("Would you like to try again? (y/n): ").lower() == 'y':
			lpop(lst)

	return lst


def lclear(lst):
	"""  Removes all elements from a list using the clear() method.
	Args:
		lst: The list from which elements will be removed.
	Returns:
		list: The modified list after clearing all elements.
	Raises:
		TypeError: If the input `lst` is not a list object.
	"""
	try:
		if isinstance(lst, list):  # Use isinstance for type checking
			if len(lst) == 0:
				print("It's already empty")
			else:
				lst.clear()
			return lst
	except TypeError as e:
		print("Error:", e)
		if input("Would you like to try again? (y/n): ").lower() == 'y':
			return lclear(lst)
		else:
			return type(lst)


def lindex(lst):
	"""
	Finds the index(es) of a value in a list and returns them, handling different data types.
	Args:
		lst: The list to search for the value
	Returns:
		list: A list of all indices where the value is found, or an empty list if not found.
	Raises:
		ValueError: If the data type is invalid.
		TypeError: If the element cannot be converted to the specified type.
	"""
	try:
		# Get user input for data type and el
		data_type = input(
			"Enter the type of element you want to find (int, float, str, bool, list, tuple, set, dict): ").lower()
		el = input("Enter the value to find its index(es): ")

		# Check and convert the value using check_type
		value = check_type(data_type, el)

		# Find all occurrences using a loop
		indices = []
		start_index = 0
		if data_type == 'bool':
			# Special for booleans to avoid matchin with 0 and 1
			for index, el in enumerate(lst):
				if isinstance(el, bool) and el == value:
					indices.append(index)
		else:
			while True:
				try:
					index = lst.index(value, start_index)
					indices.append(index)
					start_index = index + 1  # Start searching from the next index
				except ValueError:
					break
		return indices
	except (ValueError, TypeError) as e:
		print(f"Error: {e}")
		return []


def lcount(lst):
	"""
	Counts the occurrences of a value in a list, handling different data types.
	Args:
		lst: The list to search for the value.
	Returns:
		int: The number of times the value appears in the list.
	Raises:
		ValueError: If the data type is invalid or the value is not found in the list.
		TypeError: If the element cannot be converted to the specified type.
	"""

	count = 0
	try:
		data_type = input(
			"Enter the type of element you want to count (int, float, str, bool, list, tuple, set, dict): ").lower()
		valid_types = "int, float, str, bool, list, tuple, set, dict"

		if data_type not in valid_types:
			raise ValueError(f"Invalid type selection. Please choose from {', '.join(valid_types)}")

		el = input("Enter the value to count its occurrences: ")
		# Check and convert the value using check_type
		value = check_type(data_type, el)

		# Special handling for booleans using "is" instead of "==" because we need reference equality
		if data_type == 'bool':
			count = sum(el is value for el in lst)  # Use list comprehension with el is value
		else:
			count = lst.count(value)

		return f"Value - {value} appears {count} times in the list."

	except (ValueError, TypeError) as e:
		print(f"Error: {e}")
		if input("Would you like to try count again with correct value? (y/n): ").lower() == 'y':
			lcount(lst)

	return count


def lsort(lst, inplace=True):
	"""
	Sorts a list in ascending or descending order, handling data structures.
	Args:
		lst: The list to be sorted.
		inplace: (Optional)control in-place sorting or returning a new list. Defaults to True (in-place sorting).
	Returns:
		None (sorts the list in-place) or a new sorted list (if inplace=False).
	Prints the sorted list or an informative message if sorting is not possible.
	"""

	# Get user input for sorting order
	order = input("Enter 'asc' for ascending or 'desc' for descending order: ").lower()

	# Check for unsortable data structures
	unsortable_types = (set, dict)
	if any(isinstance(el, unsortable_type) for el in lst for unsortable_type in unsortable_types):
		print("The list contains mixed data types. Sorting is not possible.")
		return

	# Check if all elements have the same data type
	data_type = type(lst[0])
	if not all(isinstance(el, data_type) for el in lst):
		print("The list contains elements of different data types. Sorting is not possible.")
		return

	# Sort the list based on user input and inplace flag
	if order == "asc":
		if inplace:
			lst.sort()
		else:
			return sorted(lst)
	elif order == "desc":
		if inplace:
			lst.sort(reverse=True)
		else:
			return sorted(lst, reverse=True)
	else:
		print("Invalid order. Please enter 'asc' or 'desc'.")
		lsort(lst)
	# Print the sorted list if in-place sorting
	if inplace:
		print(f"Sorted list: {lst}")


def lreverse(lst):
	"""
	Reverses the order of a list using the reverse() method, handling errors.
	Args:
		lst: The list to be reversed.
	Returns:
		None (modifies the list in-place)
	Prints the reversed list or an informative message if an error occurs.
	"""
	if not isinstance(lst, list):
		raise TypeError("Argument must be a list.")
	lst.reverse()
	return f"Reversed list: {lst}"


def lcopy(lst):
	"""
	Creates a shallow copy of a list using the copy() method, handling errors.
	Args:
		lst: The list to be copied.
	Returns:
		A new list (shallow copy) of the original list.
	Raises:
		TypeError: If the argument is not a list.
	"""

	if not isinstance(lst, list):
		raise TypeError("Argument must be a list.")

	return lst.copy()


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
