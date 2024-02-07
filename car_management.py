class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, make=None, model=None):
        self._id = CarManager.total_cars + 1
        CarManager.total_cars += 1
        self.make = make
        self.model = model
   
    def terminal_application(self):
        print(f'---- WELCOME ----')
        print("1. Add a car")
        print("2. View all cars")
        print("3. View total numbers of cars")
        print("4. See a car's details")
        print("5. Service a car")
        print("6. Update mileage")
        print("7. Quit")

        choice = self.get_user_input()
        self.user_choice(choice)

    def get_user_input(self):
        return input ("Pick a Service: ")
    
    def user_choice(self, choice):
        if choice == "1":
            make = input("Enter make of car here: ")
            model = input("Enter model here: ")
            self.add_car(make, model)

        elif choice == "2":
            print(CarManager.all_cars)

        elif choice == "3":
            print(CarManager.total_cars)
        # elif choice == "4":
        # elif choice == "5":
        # elif choice == "6":
        elif choice == "7":
            print(f"Have a good day!!")


    def add_car(self, make, model):
        car = CarManager(make, model)
        CarManager.all_cars.append(car)
        print("Car added")


CarManager().terminal_application()