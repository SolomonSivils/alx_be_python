# simple interface for managing a shopping list

def display_menu():
    print("Shopping List Manager")
    print("-----" * 4)
    print("Press 1 to add items")
    print("Press 2 to remove an item")
    print("Press 3 to view list")
    print("Press 4 to exit")

def main():
    # implementation of an array shopping_list
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your selection: ")
        if choice == "1":
            item_to_add= input("Please add the item you want: ")
            shopping_list.append(item_to_add)
            print(f"{item_to_add} added to the shopping list successfully!")
        elif choice == "2":
            item_to_remove = input("Please type item you wish to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} removed from the shopping list successfully")
            else:
                print(f"{item_to_remove} not in the list")       
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            exit()
        else:
            print("Invalid selection")
main()