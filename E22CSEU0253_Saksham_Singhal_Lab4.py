class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        results = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                results.append(flight)
        return results

    def search_by_source(self, source):
        results = []
        for flight in self.flights:
            if flight.source == source:
                results.append(flight)
        return results

    def search_between_cities(self, source, destination):
        results = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                results.append(flight)
        return results

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)

    print("Flight Table Application")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city: ")
        results = flight_table.search_by_city(city)
    elif choice == 2:
        source = input("Enter the source city: ")
        results = flight_table.search_by_source(source)
    elif choice == 3:
        source = input("Enter the source city: ")
        destination = input("Enter the destination city: ")
        results = flight_table.search_between_cities(source, destination)
    else:
        print("Invalid choice")
        return

    if results:
        print("Flight ID\tSource\tDestination\tPrice")
        for flight in results:
            print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()
