class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, rate_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.rate_per_day = rate_per_day
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Rented"
        return f"ID:{self.vehicle_id} | {self.model} | ({self.year} | {status})"
    
    def rent(self, days):
        if not self.available:
            return None
        self.available = False
        return self.calculate_rent(days)
    
    def return_vehicle(self):
        if self.available:
            return "Vehicle already available"
        self.available = True
        return "Vehicle returned sucessfully"
    
    def calculate_rent(self, days):
        return self.rate_per_day * days
    

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rate_per_day, seats):
        super().__init__(vehicle_id, brand, model, year, rate_per_day)
        self.seats = seats

    def calculate_rent(self, days):
        return super().calculate_rent(days) + 500

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rate_per_day, engine_cc):
        super().__init__(vehicle_id, brand, model, year, rate_per_day)
        self.engine_cc = engine_cc

    def calculate_rent(self, days):
        base = super().calculate_rent(days)
        return base + 200 if self.engine_cc > 150 else base

class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rate_per_day, load_capacity):
        super().__init__(vehicle_id, brand, model, year, rate_per_day)
        self.load_capacity = load_capacity

    def calculate_rent(self, days):
        return super().calculate_rent(days) + (self.load_capacity * 100)

class VehicleManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_all(self):
        for v in self.vehicles:
            print(v.display_info())

    def rent_vehicle(self, vehicle_id, days):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                cost = v.rent(days)
                if cost is None:
                    return "Vehicle not available"
                return f"Total Rent: {cost} Taka"
        return "Vehicle not found"

    def return_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                return v.return_vehicle()
        return "Vehicle not found"

manager = VehicleManager()

manager.add_vehicle(Car(1, "Toyota", "Corolla", 2022, 3000, 5))
manager.add_vehicle(Car(2, "Tesla", "Y3", 2022, 3000, 5))
manager.add_vehicle(Bike(4, "Royel Enfield", "SC53", 2022, 3000, 5))
manager.add_vehicle(Bike(5, "Yamaha", "R15", 2021, 800, 155))
manager.add_vehicle(Truck(6, "Volvo", "FH16", 2020, 7000, 20))

while True:
    print("\n--- Vehicle Management System ---")
    print("1. Show Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        manager.show_all()

    elif choice == "2":
        vid = int(input("Enter Vehicle ID: "))
        days = int(input("Enter days: "))
        print(manager.rent_vehicle(vid, days))

    elif choice == "3":
        vid = int(input("Enter Vehicle ID to return: "))
        print(manager.return_vehicle(vid))

    elif choice == "4":
        break

    else:
        print("Invalid choice")