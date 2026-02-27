def semi_to_meter(s):
    return measure / 100

def meter_to_semi(f):
    return measure * 100

print("=== Measurement Conversion System ===")

while True:
    print("\n1. Sentimeter to Meter")
    print("2. Meter to Sentimeter")
    print("3. Exit")

    try:
        choice = int(input("Select an option: "))

        if choice == 3:
            print("System terminated successfuly.")
            break

        if choice not in (1,2):
            print("Invalid selection. Please choose a valid option: ")
            continue

        measure = int(input("Enter measurement value: "))

        if choice == 1:
            result = semi_to_meter(measure)
            print(f"Converted measurement: {result:.2f} m")
        elif choice == 2:
            result = meter_to_semi(measure)
            print(f"Converted measurement: {result:.2f} sm")
    except ValueError:
        print("Invalid input")
        continue