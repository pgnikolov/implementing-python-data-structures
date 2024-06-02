def display_menu():
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


def handle_append(lst):
	"""Appends a new element to the end of the list.
	Args:
		list to modify.
	Returns:
		The updated list.
	"""
	value = input("Enter a value to append: ")
	lst.append(value)
	print("Updated list:", lst)


def handle_extend(lst):
	"""Extend a list by appending elements from iterable.
	Args:
		list to modify.
	Returns:
		The updated list.
	"""
	values = input("Enter values to extend the list (comma-separated): ")
	lst.extend(values.split(','))
	print("Updated list:", lst)


def handle_insert(lst):
	"""
	Insert a new element into the list at a specified index.
	Args:
		list to insert the element into.
	Raises:
		ValueError: If the input index is not an integer.
	Returns:
		updated list
	"""
	try:
		index = int(input("Enter the index to insert at: "))
		value = input("Enter the value to insert: ")
		lst.insert(index, value)
		print("Updated list:", lst)
	except ValueError:
		print("Invalid index. Please enter an integer.")


def handle_remove(lst):
	"""
	Remove an element from the list.
	Args:
		list to remove the element from.
	Raises:
		ValueError: If the value is not found in the list.
	Returns:
		updated list
	"""
	value = input("Enter a value to remove: ")
	try:
		lst.remove(value)
		print("Updated list:", lst)
	except ValueError:
		print("Value not found in the list.")


def handle_pop(lst):
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
	index = input("Enter the index to pop (leave empty to pop the last item): ")
	try:
		if index == "":
			print("Popped value:", lst.pop())
		else:
			print("Popped value:", lst.pop(int(index)))
		print("Updated list:", lst)
	except IndexError:
		print("Index out of range.")
	except ValueError:
		print("Invalid index. Please enter an integer.")


def handle_clear(lst):
	"""
	Clear all elements from the list.
	Argss:
		list to clear.
	Returns:
		empty list
	"""
	lst.clear()
	print("Updated list:", lst)


def handle_index(lst):
	"""
	Find the index of a specified value in the list.
	Args:
		list to search for the value.
	Raises:
		ValueError: If the value is not found in the list.
	Returns:
		index of value
	"""
	value = input("Enter a value to find its index: ")
	try:
		index = lst.index(value)
		print(f"The index of {value} is {index}.")
	except ValueError:
		print("Value not found in the list.")


def handle_count(lst):
	"""
	Count the occurrences of a specified value in the list.
	Args:
		list to count the occurrences of the value.
	Returns:
		number of ooccurrencess of a value
	"""
	value = input("Enter a value to count: ")
	count = lst.count(value)
	print(f"The count of {value} is {count}.")


def handle_sort(lst):
	"""
	Sort the list.
	Argss:
		list to sort.
	Raises:
		TypeError: If the list contains elements of different data types.
	Returns:
		sorted list
	"""
	try:
		lst.sort()
		print("Sorted list:", lst)
	except TypeError:
		print("Cannot sort a list with different data types.")


def handle_reverse(lst):
	"""
	Reverse the order of elements in the list.
	Args:
		list to reverse.
	Returns:
		reversed list
	"""
	lst.reverse()
	print("Reversed list:", lst)


def handle_copy(lst):
	"""
	Create a copy of the list.
	Argss:
		list to copy.
	Returns:
		list copy
	"""
	copied_list = lst.copy()
	print("Copied list:", copied_list)


def main():
	initial_values = input("Enter initial list values (comma-separated): ")
	lst = initial_values.split(',')

	while True:
		display_menu()
		choice = input("Enter your choice (1-12): ")
		if choice == '1':
			handle_append(lst)
		elif choice == '2':
			handle_extend(lst)
		elif choice == '3':
			handle_insert(lst)
		elif choice == '4':
			handle_remove(lst)
		elif choice == '5':
			handle_pop(lst)
		elif choice == '6':
			handle_clear(lst)
		elif choice == '7':
			handle_index(lst)
		elif choice == '8':
			handle_count(lst)
		elif choice == '9':
			handle_sort(lst)
		elif choice == '10':
			handle_reverse(lst)
		elif choice == '11':
			handle_copy(lst)
		elif choice == '12':
			print("Exiting the application.")
			break
		else:
			print("Invalid choice. Please try again.")


if __name__ == "__main__":
	main()
