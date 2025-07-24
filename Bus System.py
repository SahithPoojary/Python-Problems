from datetime import datetime

class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno

    def get_ac(self):
        return self.ac

    def get_cap(self):
        return self.cap

    def display(self):
        print(f"1. BUS NO: {self.get_bno()}")
        print(f"2. AC: {'Yes' if self.get_ac() else 'No'}")
        print(f"3. CAPACITY: {self.get_cap()}")

class Booking:
    def __init__(self):
        name = input("Enter passenger name: ")
        bno = int(input("Enter bus number: "))
        d = input("Enter travel date (YYYY-MM-DD): ")
        date = datetime.strptime(d, "%Y-%m-%d").date()
        self.name = name
        self.bno = bno
        self.date = date
        
    def make_booking(self, BUSES, BOOKINGS):
        if self.is_available(BUSES, BOOKINGS, self.bno, self.date):
            BOOKINGS.append(self)
            print("Booking successful!")
        else:
            print("Booking is full")
        
    def is_available(self, BUSES, BOOKINGS, bno, date):
        booked = 0
        capacity = 0
        for i in BUSES:
            if i.get_bno() == bno:
                capacity = i.get_cap()
                break
        for i in BOOKINGS:
            if i.bno == bno and i.date == date:
                booked += 1
        return booked < capacity

    def display_book_info(self):
        print(f"Passenger Name: {self.name}")
        print(f"Bus Number: {self.bno}")
        print(f"Travel Date: {self.date.strftime('%Y-%m-%d')}")
        print("--------------------------------------------")

# Main Program
BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(3, True, 55)]

print("Available Buses:")
for i in BUSES:
    i.display()
    print("--------------------------------------------")

BOOKINGS = []

while True:
    print("\n----- BUS BOOKING SYSTEM -----")
    print("Press 1 to Book a Bus")
    print("Press 2 to View Bookings")
    print("Press 3 to Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        b = Booking()
        b.make_booking(BUSES, BOOKINGS)
    elif choice == '2':
        if not BOOKINGS:
            print("No bookings available.")
        else:
            for i in BOOKINGS:
                i.display_book_info()
    elif choice == '3':
        print("Exiting the booking system.... THANK YOU!....")
        break
    else:
        print("Invalid choice. Please try again.")
