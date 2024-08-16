
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import Flights
import Destinations



class Trip:
    def __init__(self):
        self.destinations = []
        self.flights = []

    def get_destinations(self):
        return self.destinations

    def add_destination(self, destination):
        self.destinations.append(destination)

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_itinerary(self):
        itinerary = []
        for destination in self.destinations:
            itinerary.append(f"{destination}")

        for flight in self.flights:
            itinerary.append(f"{flight}")

        return itinerary


trip = Trip()
class AddDestinationMenu:
    def __init__(self, root, trip):
        self.root = root
        self.trip = trip
        self.root.geometry("800x600")
        self.name = ""
        self.destination = ""
        self.root.title("Add Destination")
        # Load flight icon and background image
        icon_image = Image.open("trip_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        flight_image = Image.open("trip.png")
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
        name_label = tk.Label(root, text="Enter Name:")
        name_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        self.destination_label = tk.Label(root, text="Enter Destination:")
        self.destination_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
        self.destination_entry = tk.Entry(root)
        self.destination_entry.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        
        
        
        
        self.add_button = tk.Button(root, text="Add Destination", command=self.add_destination, state=tk.DISABLED)  # Reference to the method here
        self.add_button.grid()
        
        self.name_entry.bind("<FocusOut>", self.check_entries)
        self.destination_entry.bind("<FocusOut>", self.check_entries)

    def check_entries(self, event):
        self.name = self.name_entry.get().strip()
        self.destination = self.destination_entry.get().strip()
        self.check_button_state()

    def check_button_state(self):
        if self.name and self.destination:
            self.add_button.config(state=tk.NORMAL)
        else:
            self.add_button.config(state=tk.DISABLED)

    def add_destination(self):  # Define the method here
        
        try:
            self.trip.add_destination(f"{self.name} in {self.destination}")
            
            self.root.destroy()
        except Exception as e:
            error_message = "Error occurred while adding destination."
            hint_message = str(e)  # You can customize the hint message based on the specific exception
            ErrorWindow(self.root, error_message, hint_message)




    

class AddConnectingFlights:
    def __init__(self, trip, destination, flights_list):
        self.trip = trip
        self.destination = destination
        self.flights_list = flights_list  # Pass the list of flights as a parameter
        self.add_connecting_flights()
        

    def add_connecting_flights(self):
        
        latest_destination = trip.get_destinations()[-1]  # Get the latest destination added
        destination = latest_destination.split(' in ')[-1].strip()  # Extract destination name

        available_flights = [flight for flight in self.flights_list if flight[3] == destination]
        if available_flights:
            for flight in available_flights:
                itinerary_info = f"{flight[0]} Flight {flight[1]} from {flight[2]} to {flight[3]} for {flight[4]}"
                self.trip.add_flight(itinerary_info)
            # messagebox.showinfo("Success", "Connecting flights added successfully!")
        else:
            messagebox.showerror("Error", "No flights available for the selected destination.")
        
        # Update the view trip menu with the modified itinerary
        # self.view_trip_menu()


class RemoveDestination:
    def __init__(self, root, trip):
        self.root = root
        self.trip = trip
        self.root.geometry("800x600")
        self.root.title("Remove Destination")
        
        # UI components for removing destination
        icon_image = Image.open("trip_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        flight_image = Image.open("trip.png")
        width, height = flight_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        flight_image = flight_image.resize((new_width, new_height))
        
        flight_photo = ImageTk.PhotoImage(flight_image)
        flight_label = tk.Label(root, image=flight_photo)
        flight_label.image = flight_photo
        flight_label.grid(row=0, column=0, columnspan=5, pady=20)
        
        welcome_label = tk.Label(root, text="Remove a Destination", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)

        name_label = tk.Label(root, text="Enter Name:")
        name_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        destination_label = tk.Label(root, text="Enter Destination:")
        destination_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
        self.destination_entry = tk.Entry(root)
        self.destination_entry.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        remove_button = tk.Button(root, text="Remove Destination", command=self.remove_destination, font=("Arial", 10), bg="#6495ED", width=20)
        remove_button.grid(row=4, column=0, columnspan=5, pady=10)

    def remove_destination(self):
        name = self.name_entry.get().strip()
        destination = self.destination_entry.get().strip()
        if name and destination:
            destination_to_remove = f"{name} in {destination}"
            if destination_to_remove in self.trip.get_destinations():
                self.trip.get_destinations().remove(destination_to_remove)
                
                self.root.destroy()
            else:
                messagebox.showerror("Error", f"Destination '{destination_to_remove}' not found in the trip itinerary.")
        else:
            messagebox.showerror("Error", "Please enter both name and destination.")



        

class TripMenuWindow:
    def __init__(self, root, admin_name, agency):
        self.root = root
        self.root.title("Display Trip")
        
        self.root.title("Book a Trip")
        self.root.geometry("800x340")
        self.admin_name = admin_name
        self.agency = agency
        
        icon_image = Image.open("trip_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        trip_image = Image.open("trip.png")
        width, height = trip_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        trip_image = trip_image.resize((new_width, new_height))
        
        trip_photo = ImageTk.PhotoImage(trip_image)
        trip_label = tk.Label(root, image=trip_photo)
        trip_label.image = trip_photo
        trip_label.grid(row=0, column=0, columnspan=5, pady=20)
    
        welcome_label = tk.Label(root, text=f"Hi {admin_name}, Welcome to the trips Sections", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)
    
        button_width = 15
        
        Add_destination = tk.Button(root, text="Add Destination", command=self.add_destination_menu, font=("Arial", 10), bg="#6495ED", width=15)
        Add_destination.grid(row=2, column=0, padx=(0, 0), pady=0, sticky="ew")
        
        remove_destination = tk.Button(root, text="Remove Destination", command=self.remove_destination_menu, font=("Arial", 10), bg="#6495ED", width=button_width)
        remove_destination.grid(row=2, column=1, padx=(0, 0), pady=0, sticky="ew")
        
        add_Connecting_Flights_button = tk.Button(root, text="Add Connecting Flights", command=self.add_connecting_flights_menu, font=("Arial", 10),  bg="#6495ED", width=button_width)
        add_Connecting_Flights_button.grid(row=2, column=2, padx=(0, 0), pady=0, sticky="ew")
        
        view_trip_button = tk.Button(root, text="View All trips", command=self.view_trip_menu, font=("Arial", 10), bg="#6495ED", width=button_width)
        view_trip_button.grid(row=2, column=3, padx=(0, 0), pady=0, sticky="ew")
        
        exit_button = tk.Button(root, text="Close", command=self.root.destroy, font=("Arial", 10),  bg="#6495ED", width=button_width)
 
        exit_button.grid(row=2, column=4, padx=(0, 0), pady=0, sticky="ew")
        
        
        # Logic to display trip itinerary in the window
    def add_connecting_flights_menu(self):
        flights_obj = Flights.Flights(self.agency)
        flights_list = flights_obj.allflight
        latest_destination = trip.get_destinations()[-1]  # Get the latest destination added
        destination = latest_destination.split(' in ')[-1]  # Extract destination name
        AddConnectingFlights(trip, destination, flights_list)  # Pass your Flights object here
        
        # Update the view trip menu with the modified itinerary
        # self.view_trip_menu()

    
   
        # AddConnectingFlights()
    def add_destination_menu(self):
        add_destination_window = tk.Toplevel(self.root)
        AddDestinationMenu(add_destination_window, trip)



    def remove_destination_menu(self):
        remove_destination_window = tk.Toplevel(self.root)
        RemoveDestination(remove_destination_window, trip)

    def view_trip_menu(self):
        trip_itinerary = trip.get_itinerary()
        if not trip_itinerary:
            trip_itinerary.append("Nothing planned yet.")
        view_trip_window = ViewTripMenuWindow(tk.Toplevel(self.root), trip_itinerary, self.agency)

class ViewTripMenuWindow:
    def __init__(self, root, trip_itinerary, agency):
        self.root = root
        self.root.title("Display Trip")
        self.trip_itinerary = trip_itinerary
        self.agency = agency
        
        icon_image = Image.open("trip_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        trip_image = Image.open("trip.png")
        width, height = trip_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        trip_image = trip_image.resize((new_width, new_height))
        
        trip_photo = ImageTk.PhotoImage(trip_image)
        trip_label = tk.Label(root, image=trip_photo)
        trip_label.image = trip_photo
        trip_label.pack(pady=20)
    
        welcome_label = tk.Label(root, text="Your Trips", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.pack(pady=20)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(root, height=5, yscrollcommand=scrollbar.set)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        for trip_item in self.trip_itinerary:
            self.listbox.insert(tk.END, trip_item)

        scrollbar.config(command=self.listbox.yview)

        # View Individual button
        self.view_individual_button = tk.Button(root, text="View Individual", command=self.view_individual, font=("Arial", 10), bg="#6495ED", width=15)
        self.view_individual_button.pack(pady=(0, 20))

        # Close button
        close_button = tk.Button(root, text="Close", command=self.root.destroy, font=("Arial", 10),  bg="#6495ED", width=15)
        close_button.pack(pady=(0, 20))
    def view_individual(self):
        selected_item_index = self.listbox.curselection()
        if selected_item_index:
            selected_item_index = selected_item_index[0]
            selected_item = self.trip_itinerary[selected_item_index]
            if ' in ' in selected_item:
                # flight_index = int(selected_item.split()[2]) - 1  # Extract flight index from the selected item
                # flight = self.flights_list[flight_index]
                
                a =Flights.Flights(self.agency)
                a.generate_random_flights()
                Flights.ViewFlightsMenuWindow(tk.Toplevel(self.root))  # Assuming you have a function to display flight details
            elif 'from' in selected_item:
                # destination_index = int(selected_item.split()[1]) - 1  # Extract destination index from the selected item
                # destination = self.destinations_list[destination_index]
                Destinations.ViewdestinationsMenuWindow(tk.Toplevel(self.root))  # Assuming you have a function to display destination details
            else:
                messagebox.showerror("Error", "Invalid selection.")
        else:
            messagebox.showerror("Error", "No item selected.")





