# Part B - Shopping List Manager

shopping_list = []

while True:
    command = input("\nEnter a command (add / remove / show / done): ").strip().lower()

    if command == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(f"{item} added to your list.")
        else:
            print("Please enter an item.")

    elif command == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from your list.")
        else:
            print("That item is not on your list.")

    elif command == "show":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif command == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Please choose add, remove, show, or done.")