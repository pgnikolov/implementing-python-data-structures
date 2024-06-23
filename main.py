from lists import Lists


def lists_display_menu():
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


def display_main_menu():
    print("\nChoose Data Structure:")
    print("1. List")
    print("2. Dictionary")
    print("3. Set")
    print("4. Tuple")
    print("5. Exit")


def main():
    while True:
        display_main_menu()
        user_choice = input("Enter your choice (1-4):")

        if user_choice == '1':
            list_menu()
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            print("Exiting...!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
