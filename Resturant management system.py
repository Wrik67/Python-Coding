TAX_RATE = 0.065

menu = {

1: ("Burger", 150.00),
2: ("Fried Chicken", 175.00),
3: ("Soda", 60.00),
4: ("Salad", 120.00),
5: ("Pizza", 500.00),
6: ("Ice Cream", 150.00),
7: ("Coffee", 200.00),
8: ("Tea", 55.00),
9: ("Juice", 90.00),
10: ("Fried Rice", 210.00),
11: ("Pasta", 250.00),
12: ("Sandwich", 200.00),
13: ("Water", 20.00),
14: ("Meetbox", 250.00)
}

order = {}

def show_menu():
    print("\nMenu:")
    for serial, (item, price) in menu.items():
        print(f"{serial}. {item} - Tk. {price}")

def take_order():
    while True:
        choice = input("\nEnter item name or serial number (or 'done' to finish): ").strip()
        if choice.lower() == "done":
            break

        selected_item = None

        if choice.isdigit() and int(choice) in menu:
            selected_item = menu[int(choice)][0]
        else:
            for _ , (item , _ ) in menu.items():
                if item.lower() == choice.lower():
                    selected_item = item
                    break

        if selected_item:
            quantity = int(input(f"Enter quantity for {selected_item}:"))
            order[selected_item] = order.get(selected_item, 0) + quantity
        else:
            print("Invalid selection. Please try again.")

def calculate_total():
    total = 0.0
    for item, quantity in order.items():
        for _ , (menu_item, price) in menu.items():
            if menu_item == item:
                total += price * quantity
                break
    tax = total * TAX_RATE
    return total, tax, total + tax

def print_bill():
    print("\n--- Bill Summary ---")
    total, tax, total_with_tax = calculate_total()
    for item, quantity in order.items():
        for _ , (menu_item, price) in menu.items():
            if menu_item == item:
                print(f"{item} x {quantity} = Tk. {price * quantity:.2f}")
                break
    print(f"Subtotal: Tk. {total:.2f}")
    print(f"Tax (6.7%): Tk. {tax:.2f}")
    print(f"Total Amount: Tk. {total_with_tax:.2f}")

if __name__ == "__main__":
    show_menu()
    take_order()
    print_bill()
    print("\nThank you for dining with us!")