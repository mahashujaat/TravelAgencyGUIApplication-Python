import Agency
import Flight
import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
class Flights:
    
    def __init__(self, agency:Agency):
        self.agency = agency
        self.allflight = []
        self.generate_random_flights()
    def get_flights_by_landing_country(self, country):
        # Logic to filter flights based on landing country
        return [flight for flight in self.all_flights if flight.landing_country == country]
    
    def generate_random_flights(self):
        airlines = ["American Airlines", "QANTAS", "JetStar", "Tiger Airways", "United Airlines", "Egypt Air", "Etihad", "Singapore Airlines", "British Air", "Cathay Dragon"]
        flight_min = 11
        flight_max = 999
        cost_min = 49.99
        cost_max = 999.99

        for _ in range(9):
            airline = random.choice(airlines)
            flight_number = random.randint(flight_min, flight_max)
            takeoff = random.choice(["France", "Australia", "Peru", "Egypt", "Canada"])
            landing = random.choice(["France", "Australia", "Peru", "Egypt", "Canada"])
            while takeoff == landing:
                landing = random.choice(["France", "Australia", "Peru", "Egypt", "Canada"])
            cost = round(random.uniform(cost_min, cost_max), 2)
            flight = Flight.Flight(airline, flight_number, takeoff, landing, cost)
            self.allflight.append([flight.airline, flight.flight_no, flight.takeoff, flight.landing, flight.cost])
    def add_flight(self, flight: Flight):
        if self.has_flight(flight.takeoff, flight.landing):
            raise ValueError("Flight already exists.")
        self.flights.append(flight)

    def remove_flight(self, flight: Flight):
        if self.has_flight(flight.takeoff, flight.landing) == False:
            raise ValueError("Flight not found.")
        self.flights.remove(flight)
    
    def has_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return True
        return False
    
    def get_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return f
        return None
    
    def get_filtered_flights(self,country):
        filtered = []
        for f in self.flights:
            if f.landing.lower().contains(country.lower()) or f.takeoff.lower().contains(country.lower()):
                filtered.append(f)
        return filtered
    
    def get_total_cost(self):
        cost = 0.0
        for f in self.flights:
            cost = cost + f.cost
        return cost


def generate_random_flights():
    airlines = ["American Airlines", "QANTAS", "JetStar", "Tiger Airways", "United Airlines", "Egypt Air", "Etihad", "Singapore Airlines", "British Air", "Cathay Dragon"]
    flight_min = 11
    flight_max = 999
    cost_min = 49.99
    cost_max = 999.99

    for _ in range(9):
        airline = random.choice(airlines)
        flight_number = random.randint(flight_min, flight_max)
        takeoff = random.choice(["France", "Australia", "Peru", "Egypt", "Canada"])
        landing = random.choice(["France", "Australia", "Peru", "Egypt", "Canada"])
        while takeoff == landing:
            landing = random.choice(["France", "Australia", "Peru", "Egypt", "Canada"])
        cost = round(random.uniform(cost_min, cost_max), 2)
        flight = Flight.Flight(airline, flight_number, takeoff, landing, cost)
        allflight.append([flight.airline, flight.flight_no, flight.takeoff, flight.landing, flight.cost])
allflight = []
generate_random_flights()

class AddFlightMenuWindow:
    def __init__(self, root, agency):
        self.root = root
        self.root.title("Add Flights")
        self.root.geometry("800x600")
        self.agency = agency

        # Load flight icon and background image
        icon_image = Image.open("flights_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        flight_image = Image.open("flight.png")
        width, height = flight_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        flight_image = flight_image.resize((new_width, new_height))
        
        flight_photo = ImageTk.PhotoImage(flight_image)
        flight_label = tk.Label(root, image=flight_photo)
        flight_label.image = flight_photo
        flight_label.grid(row=0, column=0, columnspan=5, pady=20)
    
        welcome_label = tk.Label(root, text="Add a Flight", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)
        # Flight Information Labels and Entry Fields
        airline_label = tk.Label(root, text="Airline:")
        airline_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        self.airline_entry = tk.Entry(root)
        self.airline_entry.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        flight_number_label = tk.Label(root, text="Flight Number:")
        flight_number_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
        self.flight_number_entry = tk.Entry(root)
        self.flight_number_entry.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        takeoff_label = tk.Label(root, text="Takeoff Country:")
        takeoff_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")
        self.takeoff_entry = tk.Entry(root)
        self.takeoff_entry.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        landing_label = tk.Label(root, text="Landing Country:")
        landing_label.grid(row=5, column=1, padx=10, pady=5, sticky="e")
        self.landing_entry = tk.Entry(root)
        self.landing_entry.grid(row=5, column=2, padx=10, pady=5, sticky="w")

        cost_label = tk.Label(root, text="Cost:")
        cost_label.grid(row=6, column=1, padx=10, pady=5, sticky="e")
        self.cost_entry = tk.Entry(root)
        self.cost_entry.grid(row=6, column=2, padx=10, pady=5, sticky="w")

        # Add Flight Button
        self.add_flight_button = tk.Button(root, text="Add Flight", command=self.add_flight, state=tk.DISABLED)
        self.add_flight_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Validate Entry Fields and Enable/Disable Add Flight Button Accordingly
        self.validate_entries()

        # Event bindings to validate entry fields on user input
        self.airline_entry.bind("<KeyRelease>", self.validate_entries)
        self.flight_number_entry.bind("<KeyRelease>", self.validate_entries)
        self.takeoff_entry.bind("<KeyRelease>", self.validate_entries)
        self.landing_entry.bind("<KeyRelease>", self.validate_entries)
        self.cost_entry.bind("<KeyRelease>", self.validate_entries)

    def validate_entries(self, event=None):
        # Check if all entry fields are filled
        if all((self.airline_entry.get(), self.flight_number_entry.get(),
                self.takeoff_entry.get(), self.landing_entry.get(), self.cost_entry.get())):
            # Enable Add Flight button
            self.add_flight_button.config(state=tk.NORMAL)
        else:
            # Disable Add Flight button
            self.add_flight_button.config(state=tk.DISABLED)

    def add_flight(self):
        
        
        # Get input values from entry fields
        airline = self.airline_entry.get()
        flight_number = self.flight_number_entry.get()
        takeoff = self.takeoff_entry.get()
        landing = self.landing_entry.get()
        cost = self.cost_entry.get()

        # Validate flight number and cost as numbers
        if not flight_number.isdigit() or not cost.replace(".", "", 1).isdigit():
            messagebox.showerror("Error", "Flight Number and Cost must be numbers.")
    
            # Create Flight object and add it to the Flights
        # Assuming you have variables airline, flight_number, takeoff, landing, and cost defined before this line
        flight = [airline, flight_number, takeoff, landing, float(cost)]


        allflight.append(flight)

        self.root.destroy()
class ViewFlightsMenuWindow:
    def __init__(self, root):
        
        self.root = root
        self.root.title("View Flights")
        self.root.geometry("800x700")
        self.allflight = allflight
        
        icon_image = Image.open("flights_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        flight_image = Image.open("flight.png")
        width, height = flight_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        flight_image = flight_image.resize((new_width, new_height))
        flight_photo = ImageTk.PhotoImage(flight_image)
        
        flight_label = tk.Label(root, image=flight_photo)
        flight_label.image = flight_photo
        flight_label.pack(fill=tk.X)  # Use pack manager for the image label
    
        welcome_label = tk.Label(root, text="Flights", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.pack(pady=20)  # Use pack manager for the welcome label
        
        # Flight Information Labels and Entry Fields
        self.tree = ttk.Treeview(root, columns=("Airline", "Flight Number", "Takeoff", "Landing", "Cost"))
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), foreground="#6495ED")
        self.tree.heading("#0", text="Airline")
        self.tree.heading("#1", text="Flight Number")
        self.tree.heading("#2", text="Takeoff")
        self.tree.heading("#3", text="Landing")
        self.tree.heading("#4", text="Cost")
        self.tree.column("#0", width=150, anchor=tk.W)  # Airline
        self.tree.column("#1", width=150, anchor=tk.W)  # Flight Number
        self.tree.column("#2", width=150, anchor=tk.W)  # Takeoff
        self.tree.column("#3", width=150, anchor=tk.W)  # Landing
        self.tree.column("#4", width=150, anchor=tk.W)  # Cost
        self.tree_height = min(len(self.allflight), 6)
        self.tree.pack(expand=True, padx=10, pady=10, side=tk.TOP, fill=tk.BOTH)

        # Populate the table with flight data
        for flight in allflight:
            self.tree.insert("", "end", values=tuple(flight))

        # Close Button
        close_button = tk.Button(root, text="Close", command=root.destroy, bg="#6495ED", fg="white", width=20)
        close_button.pack(pady=10, side=tk.TOP, fill=tk.X)

class ViewByCountryMenuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("View Flights Filtered")
        self.root.geometry("800x700")
        
        icon_image = Image.open("flights_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        flight_image = Image.open("flight.png")
        width, height = flight_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        flight_image = flight_image.resize((new_width, new_height))
        flight_photo = ImageTk.PhotoImage(flight_image)
        
        flight_label = tk.Label(root, image=flight_photo)
        flight_label.image = flight_photo
        flight_label.pack(fill=tk.X)  # Use pack manager for the image label
        
        welcome_label = tk.Label(root, text="View Flights Filtered", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.pack(pady=10)  # Use pack manager for the welcome label
        
        # Search Bar
        search_label = tk.Label(root, text="Search Country:")
        search_label.pack(padx=10, pady=5, anchor=tk.W)
        self.search_entry = tk.Entry(root)
        self.search_entry.pack(padx=10, pady=5, fill=tk.X)
        self.search_entry.bind("<KeyRelease>", self.filter_flights)
        
        # Flight Information Table
        self.tree = ttk.Treeview(root, columns=("Airline", "Flight Number", "Takeoff", "Landing", "Cost"))
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), foreground="#6495ED")
        self.tree.heading("#0", text="Airline")
        self.tree.heading("#1", text="Flight Number")
        self.tree.heading("#2", text="Takeoff")
        self.tree.heading("#3", text="Landing")
        self.tree.heading("#4", text="Cost")
        self.tree.column("#0", width=150, anchor=tk.W)  # Airline
        self.tree.column("#1", width=150, anchor=tk.W)  # Flight Number
        self.tree.column("#2", width=150, anchor=tk.W)  # Takeoff
        self.tree.column("#3", width=150, anchor=tk.W)  # Landing
        self.tree.column("#4", width=150, anchor=tk.W)  # Cost
        self.tree_height = min(len(allflight), 6)
        self.tree.pack(expand=True, padx=10, pady=10, side=tk.TOP, fill=tk.BOTH)
        
        # Populate the table with flight data
        for flight in allflight:
            self.tree.insert("", "end", values=tuple(flight))
        
        # Close Button
        close_button = tk.Button(root, text="Close", command=root.destroy, bg="#6495ED", fg="white", width=20)
        close_button.pack(pady=10, side=tk.TOP, fill=tk.X)
    
    def filter_flights(self, event=None):
        search_term = self.search_entry.get().strip().capitalize()
        self.tree.delete(*self.tree.get_children())  # Clear existing data in the table
        for flight in allflight:
            if search_term in flight[2].capitalize() or search_term in flight[3].capitalize():
                self.tree.insert("", "end", values=tuple(flight))

class RemoveFlightMenuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Remove Flight")
        self.root.geometry("400x700")
        
        icon_image = Image.open("flights_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        flight_image = Image.open("flight.png")
        width, height = flight_image.size
        new_width = 400  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        flight_image = flight_image.resize((new_width, new_height))
        flight_photo = ImageTk.PhotoImage(flight_image)
        
        flight_label = tk.Label(root, image=flight_photo)
        flight_label.image = flight_photo
        flight_label.pack(fill=tk.X)  # Use pack manager for the image label
        
        welcome_label = tk.Label(root, text="Remove Flight", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.pack(pady=20)  # Use pack manager for the welcome label
        
        # Takeoff Country Label and Entry
        takeoff_label = tk.Label(root, text="Takeoff Country:")
        takeoff_label.pack(padx=10, pady=5, anchor=tk.W)
        self.takeoff_entry = tk.Entry(root)
        self.takeoff_entry.pack(padx=10, pady=5, fill=tk.X)
        
        # Landing Country Label and Entry
        landing_label = tk.Label(root, text="Landing Country:")
        landing_label.pack(padx=10, pady=5, anchor=tk.W)
        self.landing_entry = tk.Entry(root)
        self.landing_entry.pack(padx=10, pady=5, fill=tk.X)
        
        # Remove Flight Button
        self.remove_flight_button = tk.Button(root, text="Remove Flight", command=self.remove_flight, state=tk.DISABLED)
        self.remove_flight_button.pack(pady=10)
        
        # Validate Entry Fields and Enable/Disable Remove Flight Button Accordingly
        self.validate_entries()
        
        # Event bindings to validate entry fields on user input
        self.takeoff_entry.bind("<KeyRelease>", self.validate_entries)
        self.landing_entry.bind("<KeyRelease>", self.validate_entries)

    def validate_entries(self, event=None):
        # Check if both entry fields are filled
        if all((self.takeoff_entry.get(), self.landing_entry.get())):
            # Enable Remove Flight button
            self.remove_flight_button.config(state=tk.NORMAL)
        else:
            # Disable Remove Flight button
            self.remove_flight_button.config(state=tk.DISABLED)

    def remove_flight(self):
        takeoff_country = self.takeoff_entry.get().strip().capitalize()
        landing_country = self.landing_entry.get().strip().capitalize()

        # Check if the flight exists in the flight list
        found = False
        for flight in allflight:
            if flight[2].capitalize() == takeoff_country and flight[3].capitalize() == landing_country:
                allflight.remove(flight)
                found = True
                break
        
        if found:
            messagebox.showinfo("Success", "Flight removed successfully.")
            # Update the Flights Menu Window with the updated flight information
            # self.flights_menu_window.update_flight_list()

        else:
            messagebox.showerror("Error", "Flight not found.")
