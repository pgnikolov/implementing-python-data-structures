import list as l


def main_list():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        l.display_list_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            print(l.lappend(lst))
        elif choice == '2':
            print(l.lextend(lst))
        elif choice == '3':
            print(l.linsert(lst))
        elif choice == '4':
            print(l.lremove(lst))
        elif choice == '5':
            print(l.lpop(lst))
        elif choice == '6':
            print(l.lclear(lst))
        elif choice == '7':
            print(l.lindex(lst))
        elif choice == '8':
            print(l.lcount(lst))
        elif choice == '9':
            print(l.lsort(lst))
        elif choice == '10':
            print(l.lreverse(lst))
        elif choice == '11':
            print(l.lcopy(lst))
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_list()
