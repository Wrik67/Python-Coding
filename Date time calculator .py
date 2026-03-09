import datetime
import calendar

def showtime():
    now = datetime.datetime.now()
    print("\nCurrent Time:", now.strftime("%I:%M:%S %p"))

def showdate():
    now = datetime.datetime.now()
    print("\nCurrent Date:", now.strftime("%A, %d %B %Y"))

def showcalendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print("\n", calendar.month(year, month))

def main_menu():
    while True:
        print("\n--- SMART REAL-TIME PLANNER---")
        print("1. Show Current Time")
        print("2. Show Current Date")
        print("3. View Monthly Calendar")
        print("4. Exit")

        choice = input("Select an option:")

        if choice == "1":
            showtime()
        elif choice == "2":
            showdate()
        elif choice == "3":
            showcalendar()
        elif choice == "4":
            print("\nSystem session closed successfully.")
            break
        else:
            print("\nInvalid selection. Please retry.")

main_menu()