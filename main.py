import list as l


def main_list():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        display_list_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            l.lappend(lst)
        elif choice == '2':
            l.lextend(lst)
        elif choice == '3':
            l.linsert(lst)
        elif choice == '4':
            l.lremove(lst)
        elif choice == '5':
            l.lpop(lst)
        elif choice == '6':
            l.lclear(lst)
        elif choice == '7':
            l.lindex(lst)
        elif choice == '8':
            l.lcount(lst)
        elif choice == '9':
            l.lsort(lst)
        elif choice == '10':
            l.lreverse(lst)
        elif choice == '11':
            l.lcopy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_list()
