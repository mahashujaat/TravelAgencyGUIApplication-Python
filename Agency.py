import Destination
from Flights import Flights
import Trip
from Administrators import Administrators
import tkinter as tk
from PIL import Image, ImageTk
from Flight import FlightsMenuWindow



class Agency:
    def __init__(self):
        self.loggedInUser = None  # You need to initialize loggedInUser to a value, it's not clear what this variable is supposed to store
        self.admins = Administrators()
        # self.destinations = Destinations.Destinations(self)
        self.flights = Flights(self)
        self.admins.insert_dummy_data()  # Correct the method call by adding parentheses
        # self.destinations.insert_dummy_data()  # Correct the method call by adding parentheses
class AgencyMenuWindow:
    def __init__(self, root, admin_name):
        self.root = root
        self.root.title("Prog2 Travel Agency")
        self.root.geometry("800x340")
        
        icon_image = Image.open("agency_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.agency = Agency()
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        agency_image = Image.open("agency.png")
        width, height = agency_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        agency_image = agency_image.resize((new_width, new_height))
        
        agency_photo = ImageTk.PhotoImage(agency_image)
        agency_label = tk.Label(root, image=agency_photo)
        agency_label.image = agency_photo
        agency_label.grid(row=0, column=0, columnspan=4, pady=20)
        self.admin_name = admin_name
        welcome_label = tk.Label(root, text=f"Hi {admin_name}, Welcome to the Prog2 Travel Agency", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=4, pady=20)

        explore_flights_button = tk.Button(root, text="Explore Flights", command=self.open_flights_menu, font=("Arial", 10), bg="#6495ED")
        explore_flights_button.grid(row=2, column=0, padx=0, pady=0, sticky="ew")

        explore_destinations_button = tk.Button(root, text="Explore Destinations", command=self.open_destinations_menu, font=("Arial", 10), bg="#6495ED")
        explore_destinations_button.grid(row=2, column=1, padx=0, pady=0, sticky="ew")

        book_trip_button = tk.Button(root, text="Book a Trip", command=self.open_trip_menu, font=("Arial", 10),  bg="#6495ED")
        book_trip_button.grid(row=2, column=2, padx=0, pady=0, sticky="ew")

        exit_button = tk.Button(root, text="Exit", command=self.root.destroy, font=("Arial", 10),  bg="#6495ED")
        exit_button.grid(row=2, column=3, padx=0, pady=0, sticky="ew")
        
    def open_flights_menu(self):
        agency = Agency()
        FlightsMenuWindow(tk.Toplevel(self.root),self.admin_name, agency)

    def open_destinations_menu(self):
        destinations_menu_window =Destination.DestinationsMenuWindow(tk.Toplevel(self.root),self.admin_name)

    def open_trip_menu(self):
        agency = Agency()
        trip_menu_window = Trip.TripMenuWindow(tk.Toplevel(self.root),self.admin_name, agency)









