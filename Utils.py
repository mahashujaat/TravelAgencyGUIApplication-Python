# import Destination

# import random
# import Flight
# class Utils:
#     @staticmethod
#     def add_flights_for_destination(destination: Destination):
#         country = destination.country
#         airlines = ["American Airlines", "QANTAS", "JetStar", "Tiger Airways", "United Airlines", "Egypt Air", "Etihad", "Singapore Airlines", "British Air", "Cathay Dragon"]
#         flight_min = 11
#         flight_max = 999

#         cost_min = 49.99
#         cost_max = 999.99

#         countries = []
#         for d in Destinations.destinations:
#             countries.append(d.country)
        
#         for s in countries:
#             try:
#                 agency.flights.add_flight(Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(flight_min, flight_max), country, s, random.uniform(cost_min, cost_max)))
#                 agency.flights.add_flight(Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(flight_min, flight_max), s, country, random.uniform(cost_min, cost_max)))
#             except:
#                 continue
# destination = Destination.Destination("Paris", "France")


# # Call the static method to add flights for the destination
# Utils.add_flights_for_destination(destination)

# # Now you can access the flights in the agency's flights attribute
# for flight in agency.flights:
#     print(flight)
