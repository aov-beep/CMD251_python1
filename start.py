from src.functions import get_all_users

exit = False

while not exit:
    print("1. Get all users")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        get_all_users()
    elif choice == '0':
        exit = True
    else:
        print("Invalid choice. Please try again.")
