

import Destinations
import tkinter as tk
from PIL import Image, ImageTk
class Destination:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def to_string(self):
        return self.name + " in " + self.country



class DestinationsMenuWindow:
    def __init__(self, root, admin_name):
        self.root = root
        self.root.title("Destinations Menu")
        self.root.geometry("800x340")
        
        icon_image = Image.open("destinations_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        destination_image = Image.open("destination.png")
        width, height = destination_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        destination_image = destination_image.resize((new_width, new_height))
        
        destination_photo = ImageTk.PhotoImage(destination_image)
        destination_label = tk.Label(root, image=destination_photo)
        destination_label.image = destination_photo
        destination_label.grid(row=0, column=0, columnspan=5, pady=20)
    
        welcome_label = tk.Label(root, text=f"Hi {admin_name}, Welcome to the destinations Sections", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)
    
        button_width = 15
        
        view_destinations_button = tk.Button(root, text="View All destinations", command=self.view_destinations_menu, font=("Arial", 10), bg="#6495ED", width=button_width)
        view_destinations_button.grid(row=2, column=0, padx=(0, 0), pady=0, sticky="ew")
        
        view_by_country_button = tk.Button(root, text="View destinations by Country", command=self.view_by_country_menu, font=("Arial", 10), bg="#6495ED", width=17)
        view_by_country_button.grid(row=2, column=1, padx=(0, 0), pady=0, sticky="ew")
        
        add_destination_button = tk.Button(root, text="Add destination", command=self.add_destination_menu, font=("Arial", 10),  bg="#6495ED", width=button_width)
        add_destination_button.grid(row=2, column=2, padx=(0, 0), pady=0, sticky="ew")
        
        remove_destinations_button = tk.Button(root, text="Remove destination", command=self.remove_destinations_menu, font=("Arial", 10), bg="#6495ED", width=button_width)
        remove_destinations_button.grid(row=2, column=3, padx=(0, 0), pady=0, sticky="ew")
        
        exit_button = tk.Button(root, text="Close", command=self.root.destroy, font=("Arial", 10),  bg="#6495ED", width=button_width)
        exit_button.grid(row=2, column=4, padx=(0, 0), pady=0, sticky="ew")
        
    
    def view_destinations_menu(self):
        

        self.view_destinations_menu_window = Destinations.ViewdestinationsMenuWindow(tk.Toplevel(self.root))
    
    def view_by_country_menu(self):
        view_by_country_menu_window = Destinations.ViewByCountryMenuWindow(tk.Toplevel(self.root))
    
    def add_destination_menu(self):
        
        
        add_destination_menu_window = Destinations.AdddestinationMenuWindow(tk.Toplevel(self.root))
        
    def remove_destinations_menu(self):

        remove_destination_menu_window = Destinations.RemovedestinationsMenuWindow(tk.Toplevel(self.root))