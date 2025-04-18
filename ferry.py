ticket_counter = 20000 
class TicketBooking:
    bookings = [] 

    def _init_(self, passenger_id, name, travel_date, id_type):
        global ticket_counter
        self.ticket_id = ticket_counter
        self.passenger_id = passenger_id
        self.name = name
        self.travel_date = travel_date
        self.id_type = id_type
        self.total_amount = 0
        self.status = "Pending"
        self.approval_ref = ""
        ticket_counter += 1

    def gather_customer_info(self):
        self.id_type = input("Please provide form of ID (Passport, Driver's License): ")
        self.passenger_id = input("Enter your ID number: ")
        self.name = input("Enter your name: ")
        print(f"Ticket ID {self.ticket_id} has been generated for {self.name}")

    def choose_services(self):
        services = []
        total_cost = 0
        while True:
            service_name = input("Enter service name (type 'done' to finish): ")
            if service_name.lower() == 'done':
                break
            else:
                price = float(input(f"Enter price for {service_name}: $"))
                services.append((service_name, price))
                total_cost += price
                print("Invalid input, please enter a valid price.")

        self.total_amount = total_cost
        print(f"Total service cost: ${self.total_amount:.2f}")

    def approve_booking(self):
        if self.total_amount < 300:
            self.status = "Approved"
        else:
            self.status = "Not Approved"

        print(f"Booking Status: {self.status}")
        if self.status == "Approved":
            self.approval_ref = self.passenger_id[:3] + str(self.ticket_id)[-2:]
            print(f"Your approval reference number: {self.approval_ref}")

    def display_booking_details(self):
        print(f"\n=== Booking Details ===")
        print(f"Form of ID: {self.id_type}")
        print(f"ID Number: {self.passenger_id}")
        print(f"Passenger Name: {self.name}")
        print(f"Travel Date: {self.travel_date}")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Total Amount: ${self.total_amount:.2f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference: {self.approval_ref}")

    @classmethod
    def display_statistics(cls):
        total = len(cls.all_bookings)
        approved_count = 0
        pending_count = 0
        not_approved_count = 0

        for booking in cls.bookings:
            if booking.status == "Approved":
                approved_count += 1
            elif booking.status == "Pending":
                pending_count += 1
            else:
                not_approved_count += 1

        print("\n--- Booking Statistics ---")
        print(f"Total Bookings: {total}")
        print(f"Approved Bookings: {approved_count}")
        print(f"Pending Bookings: {pending_count}")
        print(f"Not Approved Bookings: {not_approved_count}")



bookings_list = []
counter = 0  

while counter < 5:
    print(f"\nBooking {counter + 1}")
    passenger_id = input("Enter Passenger ID: ")
    passenger_name = input("Enter Passenger Name: ")
    travel_date = input("Enter Travel Date (e.g., 2025-04-11): ")
    id_type = input("Enter Form of ID (Passport, Driver's License): ")

    new_booking = TicketBooking(passenger_id, passenger_name, travel_date, id_type)

    new_booking.gather_customer_info()
    new_booking.choose_services()

    bookings_list.append(new_booking)
    counter += 1 

print("\nBooking Statistics (Initial):")
TicketBooking.display_statistics()

for booking in bookings_list:
    booking.approve_booking()

print("\n=== Booking Details After Approval ===")
for booking in bookings_list:
    booking.display_booking_details()

print("\nBooking Statistics (Final):")
TicketBooking.display_statistics()


