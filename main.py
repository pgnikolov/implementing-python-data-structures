from lists import Lists
from stack import Stack
from dictionary import Dictionary
from setss import Sets


def lists_display_menu():
    print("\nChoose a list operation:")
    print('\n Choose option:')
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
    print("12. Back to main menu")


def list_menu():
    initial_values = input("Enter initial list values (comma-separated): ")
    elements = Lists(initial_values)

    while True:
        lists_display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            new_element = input("Enter element to be appended: ")
            print(Lists.handle_append(elements, new_element))
        elif choice == '2':
            new_list = input("Enter comma-separated elements to be appended: ").split(", ")
            print(Lists.handle_extend(elements, new_list))
        elif choice == '3':
            index_ = int(input("Enter index to be inserted: "))
            new_element = input("Enter element to be inserted: ")
            print(Lists.handle_insert(elements, index_, new_element))
        elif choice == '4':
            element = input("Enter element to be removed: ")
            print(Lists.handle_remove(elements, element))
        elif choice == '5':
            index_ = int(input("Enter index to be removed or leave empty to remove last: "))
            print(Lists.handle_pop(elements, index_))
        elif choice == '6':
            Lists.handle_clear(elements)
        elif choice == '7':
            element = input("Enter element to find its index: ")
            print(Lists.handle_index(elements, element))
        elif choice == '8':
            element = input("Enter element to count: ")
            print(Lists.handle_count(elements, element))
        elif choice == '9':
            print(Lists.handle_sort(elements))
        elif choice == '10':
            print(Lists.handle_reverse(elements))
        elif choice == '11':
            print(Lists.handle_copy(elements))
        elif choice == '12':
            print("Going back...")
            main()
            break
        else:
            print("Invalid choice. Please try again.")


def dictionary_display_menu():
    print('\n Choose option:')
    print('1. Pop')
    print('2. Items')
    print('3. Get')
    print('4. Copy')
    print('5. Clear')
    print('6. Keys')
    print('7. Values')
    print('8. Update')
    print('9. Popitem')
    print('10. Set Default')
    print('11. Back to Main Menu')


def dictionary_menu():
    key_values_elements = input('Enter key: value pair like this ("key1: value1, key2: value2"): ')
    edictionary = Dictionary(key_values_elements)

    while True:
        dictionary_display_menu()
        choice = input('Enter a choice')
        if choice == '1':
            key_to_pop = input('Enter a key which you want to pop: ')
            print(edictionary.handle_pop(key_to_pop))
        elif choice == '2':
            print(edictionary.handle_items())
        elif choice == '3':
            key_to_get = input('Enter a key to get: ')
            print(edictionary.handle_get(key_to_get))
        elif choice == '4':
            print(edictionary.handle_copy())
        elif choice == '5':
            print(edictionary.handle_clear())
        elif choice == '6':
            print(edictionary.handle_keys())
        elif choice == '7':
            print(edictionary.handle_values())
        elif choice == '8':
            key_values_string = input('Enter key, value pairs to update like this|("key1: value1, key2: value2") ')
            print(edictionary.handle_update(key_values_string))
        elif choice == '9':
            print(edictionary.handle_popitem())
        elif choice == '10':
            kv_setdefault = input('Enter key-value pairs in the format "key1: value1, key2: value2":  ')
            pairs = kv_setdefault.split(", ")
            for pair in pairs:
                key, value = pair.split(": ")
                edictionary.handle_setdefault(key, value)
            print(edictionary)
        elif choice == '12':
            print("Going back...")
            main()
            break
        else:
            print("Invalid choice. Please try again.")


def stack_display_menu():
    print('\n Choose option:')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Size')
    print('5. Back to Main Menu')


def stack_menu():
    initial_values = input("Enter initial list values (comma-separated): ")
    stack = Stack(initial_values)
    while True:
        stack_display_menu()
        choice = input("Enter a choice: ")
        if choice == '1':
            element_push = input("Enter element to push: ")
            print(stack.push(element_push))
        elif choice == '2':
            print(stack.pop())
        elif choice == '3':
            print(stack.peek())
        elif choice == '4':
            print(stack.size())
        elif choice == '5':
            print("Going back...")
            main()
            break
        else:
            print("Invalid choice")


def display_sets_menu():
    print('\n Choose option:')
    print('1. Add')
    print('2. Remove')
    print('3. Discard')
    print('4. Pop')
    print('5. Clear')
    print('6. Union')
    print('7. Intersection')
    print('8. Difference')
    print('9. Copy')
    print('10. Is Super Set')
    print('11. Is Sub Set')
    print('12. Symmetric Difference')
    print('13. Back to Main Menu')


def sets_menu():
    set_values = input("Enter initial list values (comma-separated): ")
    elements = Sets(set_values)
    while True:
        stack_display_menu()
        choice = input()
        if choice == '1':
            new_element = input('Enter new element to add: ')
            print(elements.handle_add(new_element))
        elif choice == '2':
            element_to_remove = input('Enter element to remove: ')
            print(elements.handle_remove(element_to_remove))
        elif choice == '3':
            element_to_discard = input('Enter element to discard: ')
            print(elements.handle_discard(element_to_discard))
        elif choice == '4':
            print(elements.handle_pop())
        elif choice == '5':
            print(elements.handle_clear())
        elif choice == '6':
            values_for_union = input('Enter values for union (comma-separated): ')
            print(elements.handle_union(values_for_union))
        elif choice == '7':
            intersection_values = input('Enter values for intersection (comma-separated): ')
            print(elements.handle_intersection(intersection_values))
        elif choice == '8':
            values_difference = input('Enter values for difference (comma-separated): ')
            print(elements.handle_difference(values_difference))
        elif choice == '9':
            print(elements.handle_copy())
        elif choice == '10':
            values_for_issuperset = input('Enter values for issuperset (comma-separated): ')
            print(elements.handle_union(values_for_issuperset))
        elif choice == '11':
            values_for_issubset = input('Enter values for issubset (comma-separated): ')
            print(elements.handle_difference(values_for_issubset))
        elif choice == '12':
            values_sym_difference = input('Enter values for symmetric difference (comma-separated): ')
            print(elements.handle_difference(values_sym_difference))
        elif choice == '13':
            print("Going back...")
            main()
            break
        else:
            print("Invalid choice")


def display_main_menu():
    print("\nChoose Data Structure:")
    print("1. List")
    print("2. Dictionary")
    print("3. Set")
    print("4. Tuple")
    print("5. Stack")
    print("6. Exit")


def main():
    while True:
        display_main_menu()
        user_choice = input("Enter your choice (1-4):")

        if user_choice == '1':
            list_menu()
        elif user_choice == '2':
            display_main_menu()
        elif user_choice == '3':
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            stack_display_menu()
        elif user_choice == '6':
            pass
        elif user_choice == '7':
            print("Exiting...!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
