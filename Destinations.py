import Destination
import Agency
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from Error import ErrorWindow
# import Utils

class Destinations:
    def __init__(self, agency: Agency):
        self.agency = agency
        self.destinations = []
        self.destinations.append(["Eiffel Tower", "France"])
        self.destinations.append(["Opera House", "Australia"])
        self.destinations.append(["Uluru", "Australia"])
        self.destinations.append(["Machu Picchu", "Peru"])
        self.destinations.append(["Great Pyramids", "Egypt"])
        self.destinations.append(["Niagara Falls", "Canada"])
    
    def add_destination_menu(self):
        name = self.name_entry.get()
        country = self.country_entry.get()

        if not name or not country:
            error_message = "Both Name and Country are required."
            hint_message = "Please enter both Name and Country to add a destination."
            ErrorWindow(error_message, hint_message)
        else:
            destinations.append([name, country])
            self.root.destroy()
            
    
    def remove_destination(self, destination: Destination):
        if self.has_destination(destination.name, destination.country) == False:
            #throw error
            pass
        self.destinations.remove(destination)
    
    def has_destination(self, name, country):
        for d in self.destinations:
            if d.name == name and d.country == country:
                return True
        return False
    
    def get_destination(self, name, country):
        if self.has_destination(name, country) == False:
            #throw error
            pass
        for d in self.destinations:
            if d.name == name and d.country == country:
                return d
        return None
    def __iter__(self):
        for destination in self.destinations:
            yield destination # Return the instance itself as the iterator object

    def __next__(self):
        if self.index < len(self.destinations):
            destination = self.destinations[self.index]
            self.index += 1
            return destination
        else:
            self.index = 0  # Reset the index for the next iteration
            raise StopIteration 
    
    def insert_dummy_data(self):
        self.destinations.append(Destination("Eiffel Tower", "France"))
        self.destinations.append(Destination("Opera House", "Australia"))
        self.destinations.append(Destination("Uluru", "Australia"))
        self.destinations.append(Destination("Machu Picchu", "Peru"))
        self.destinations.append(Destination("Great Pyramids", "Egypt"))
        self.destinations.append(Destination("Niagara Falls", "Canada"))
        for d in self.destinations:
            Utils.Utils.add_flights_for_destination(d, self.agency)
agency = Agency.Agency()
Dest_obj = Destinations(agency)
destinations= Dest_obj.destinations
class ViewByCountryMenuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("View Destinations Filtered by Country")
        self.root.geometry("800x600")  # Set the dimensions of the window
        
        # Load icon image
        icon_image = Image.open("destinations_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        # Load destination image and resize it
        destination_image = Image.open("destination.png")
        width, height = destination_image.size
        new_width = 800  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        destination_image = destination_image.resize((new_width, new_height))
        
        # Create a PhotoImage object from the resized image
        destination_photo = ImageTk.PhotoImage(destination_image)
        
        # Display the destination image in a label
        destination_label = tk.Label(root, image=destination_photo)
        destination_label.image = destination_photo
        destination_label.grid(row=0, column=0, columnspan=5, pady=20)
    
        # Label for the search bar
        search_label = tk.Label(root, text="Search by Country:", font=("Arial", 12, "bold"))
        search_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        # Entry widget for user input (country name)
        self.search_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.search_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.search_entry.bind("<KeyRelease>", self.filter_destinations)  # Bind a function to handle input changes
        
        # Treeview widget to display filtered destinations
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), foreground="#6495ED")
        self.tree = ttk.Treeview(root, columns=("Name", "Country"), show="headings", height=20)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Country", text="Country")
        self.tree.column("Name", width=400)
        self.tree.column("Country", width=400)
        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        # Close button
        self.close_button = tk.Button(root, text="Close", command=self.root.destroy, font=("Arial", 12, "bold"),
                                      bg="#FF4500", fg="white", width=20)
        self.close_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        # Initial display of all destinations
        for destination in destinations:
            self.tree.insert("", "end", values=tuple(destination))
    
    def filter_destinations(self, event):
        # Get the search term from the entry widget
        search_term = self.search_entry.get().lower()
        # Clear the current items in the treeview
        self.tree.delete(*self.tree.get_children())
        # Insert destinations matching the search term into the treeview
        for destination in destinations:
            if search_term in destination[1].lower():  # Check if the search term is in the country name
                self.tree.insert("", "end", values=tuple(destination))


class AdddestinationMenuWindow(Destinations):
    def __init__(self, root):
        self.root = root
        self.root.title("Add Destinations")
        self.root.geometry("800x700")
        self.agency = Agency.Agency()

        
        
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
    
        welcome_label = tk.Label(root, text="Add a Destination", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.country_label = tk.Label(root, text="Country:")
        self.country_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.country_entry = tk.Entry(root)
        self.country_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.add_button = tk.Button(root, text="Add Destination", command=self.add_destination_menu)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        self.close_button = tk.Button(root, text="Close", command=self.root.destroy)
        self.close_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        self.name_entry.bind("<KeyRelease>", self.validate_input)
        self.country_entry.bind("<KeyRelease>", self.validate_input)
        


    def validate_input(self, event):
        name = self.name_entry.get()
        country = self.country_entry.get()
        if name and country:
            self.add_button.config(state=tk.NORMAL)
        else:
            self.add_button.config(state=tk.DISABLED)

    def add_destination_menu(self):
        name = self.name_entry.get()
        country = self.country_entry.get()

        # destination = Destination.Destination(name, country)
        
        destinations.append([name, country])

        
        self.root.destroy()
        
class ViewdestinationsMenuWindow(Destinations):
    
    def __init__(self, root):
        self.root = root
        self.root.title("Destinations")
        self.root.geometry("800x600")
        self.agency = Agency.Agency()


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
    
        welcome_label = tk.Label(root, text="Destinations", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), foreground="#6495ED")
        self.tree = ttk.Treeview(root, columns=("Name", "Country"), show="headings", height=20)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Country", text="Country")
        self.tree.column("Name", width=400)
        self.tree.column("Country", width=400)
        
        

        self.tree.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Close button
        self.close_button = tk.Button(root, text="Close", command=self.root.destroy, font=("Arial", 12, "bold"),
                                      bg="#FF4500", fg="white", width=20)
        self.close_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    

        for destination in destinations:
            self.tree.insert("", "end", values=tuple(destination))

        
class RemovedestinationsMenuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Remove Destination")
        self.root.geometry("800x700")

        
        icon_image = Image.open("destinations_icon.png")
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
        destination_image = Image.open("destination.png")
        width, height = destination_image.size
        new_width = 800
        new_height = int((new_width / width) * height)
        destination_image = destination_image.resize((new_width, new_height))
        
        destination_photo = ImageTk.PhotoImage(destination_image)
        destination_label = tk.Label(root, image=destination_photo)
        destination_label.image = destination_photo
        destination_label.grid(row=0, column=0, columnspan=5, pady=20)
    
        welcome_label = tk.Label(root, text="Remove a Destination", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=5, pady=20)
        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        self.country_label = tk.Label(root, text="Country:")
        self.country_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.country_entry = tk.Entry(root)
        self.country_entry.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.remove_button = tk.Button(root, text="Remove Destination", command=self.remove_destination_menu)
        self.remove_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        self.close_button = tk.Button(root, text="Close", command=self.root.destroy)
        self.close_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        self.name_entry.bind("<KeyRelease>", self.validate_input)
        self.country_entry.bind("<KeyRelease>", self.validate_input)

    def validate_input(self, event):
        name = self.name_entry.get()
        country = self.country_entry.get()
        if name and country:
            self.remove_button.config(state=tk.NORMAL)
        else:
            self.remove_button.config(state=tk.DISABLED)

    def remove_destination_menu(self):
        name = self.name_entry.get()
        country = self.country_entry.get()
        if not name or not country:
            # Handle case when name or country is empty
            return
        
        # Find the destination with the given name and country and remove it
        found_destination = None
        for destination in destinations:
            if destination[0] == name and destination[1] == country:
                found_destination = destination
                break
        
        if found_destination:
            destinations.remove(found_destination)
            
            # Optionally, you can update the treeview to reflect the changes
            # self.tree.delete(*self.tree.get_children())
            # for destination in destinations:
            #     self.tree.insert("", "end", values=tuple(destination))
        else:
            print(f"Destination not found: {name}, {country}")
        
        self.root.destroy()  # Close the window after removing the destination

