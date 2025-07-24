# simple interface for managing a shopping list

def display_menu():
    # display menu options to users
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # implementation of an array shopping_list
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            item_to_add= input("Please add the item you want: ")
            shopping_list.append(item_to_add)
            pass
        elif choice == '2':
            item_to_remove = input("Please type item you wish to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                pass
            else:
                print(f"{item_to_remove} not in the list") 
                pass      
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid selection")
main()