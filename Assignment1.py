# create an inventory management program, use loops to update or display list of stock items

# Inventory Management Program  
inventory = ["Apples", "Bananas", "Oranges","juice", "Bread", "Milk", "Eggs", "Cheese", "Butter", "Yogurt"]

def display_inventory():
    global inventory
    print("\nCurrent Inventory:")
    for item in inventory:
        print(f"- {item}")

def add_item():
    global inventory
    item = input("Enter the item to add to inventory: ")
    if item not in inventory:
        inventory.append(item)
        print(f"{item} has been added to the inventory.")
    else:
        print(f"{item} is already in the inventory.")

def remove_item():
    global inventory    
    item = input("Enter the item to remove from inventory: ")
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from the inventory.")
    else:
        print(f"{item} is not in the inventory.")

def main():
    while True:
        print("\nInventory Management Menu:")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
            
main()