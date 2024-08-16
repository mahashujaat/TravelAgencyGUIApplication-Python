import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import random
import Flights

# import Agency

class Flight:
    def __init__(self, airline, flight_no, takeoff, landing, cost):
        self.airline = airline
        self.flight_no = flight_no
        self.takeoff = takeoff
        self.landing = landing
        self.cost = cost
    
    def __str__(self):
        return f"{self.airline} Flight {self.flight_no} from {self.takeoff} to {self.landing} for {self.cost}"
    

class FlightsMenuWindow:
    def __init__(self, root, admin_name, agency):
        self.root = root
        self.root.title("Explore Flights")
        self.root.geometry("800x340")
        self.agency = agency
        
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
    
        welcome_label = tk.Label(root, text=f"Hi {admin_name}, Welcome to the Flights Sections", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)
    
        button_width = 15
        
        view_flights_button = tk.Button(root, text="View All Flights", command=self.view_flights_menu, font=("Arial", 10), bg="#6495ED", width=button_width)
        view_flights_button.grid(row=2, column=0, padx=(0, 0), pady=0, sticky="ew")
        
        view_by_country_button = tk.Button(root, text="View Flights by Country", command=self.view_by_country_menu, font=("Arial", 10), bg="#6495ED", width=button_width)
        view_by_country_button.grid(row=2, column=1, padx=(0, 0), pady=0, sticky="ew")
        
        add_flight_button = tk.Button(root, text="Add Flight", command=self.add_flight_menu, font=("Arial", 10),  bg="#6495ED", width=button_width)
        add_flight_button.grid(row=2, column=2, padx=(0, 0), pady=0, sticky="ew")
        
        remove_flights_button = tk.Button(root, text="Remove Flight", command=self.remove_flights_menu, font=("Arial", 10), bg="#6495ED", width=button_width)
        remove_flights_button.grid(row=2, column=3, padx=(0, 0), pady=0, sticky="ew")
        
        exit_button = tk.Button(root, text="Close", command=self.root.destroy, font=("Arial", 10),  bg="#6495ED", width=button_width)
        exit_button.grid(row=2, column=4, padx=(0, 0), pady=0, sticky="ew")
        
    # Inside FlightsMenuWindow class
    def view_flights_menu(self):
        
            view_flights_menu_window = Flights.ViewFlightsMenuWindow(tk.Toplevel(self.root))
        

    def view_by_country_menu(self):
       
            view_by_country_menu_window = Flights.ViewByCountryMenuWindow(tk.Toplevel(self.root))
       

    def add_flight_menu(self):
        
            add_flight_menu_window = Flights.AddFlightMenuWindow(tk.Toplevel(self.root), self.agency)
        

    def remove_flights_menu(self):
        
            remove_flight_menu_window = Flights.RemoveFlightMenuWindow(tk.Toplevel(self.root))
       
        
