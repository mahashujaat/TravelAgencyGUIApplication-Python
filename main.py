import tkinter as tk
from Administrator import Administrator
from Administrators import Administrators
from Destination import Destination
from Destinations import Destinations
from Flight import Flight
from Flights import Flights
from Agency import Agency,AgencyMenuWindow
# from Utils import Utils
from tkinter import messagebox, ttk
import sys
from PIL import Image, ImageTk


class BendedEntry(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, style="Bended.TEntry", **kwargs)

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        icon_image = Image.open("login_icon.png")  # Replace "login_icon.png" with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Set the window icon
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)

        self.root.geometry("400x199")  # Increase the window size

        style = ttk.Style()

        style.theme_use("clam")

        if "Bended.TEntry" not in style.element_names():
            style.element_create("Bended.TEntry", "from", "clam")

        style.layout("Bended.TEntry", [("Entry.padding", {"sticky": "nswe", "children":
                            [("Entry.textarea", {"sticky": "nswe"})]})])
        style.configure("Bended.TEntry", padding=8, relief="flat", font=("Arial", 14), foreground="black")
        style.map("Bended.TEntry", fieldbackground=[("!focus", "#ffffff")])

        self.heading_label = tk.Label(root, text="Login", font=("Arial", 20, "bold"), fg="#6495ED")
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.username_label = tk.Label(root, text="Username:", font=("Arial", 12, "bold"), fg="#6495ED")
        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.username_entry = BendedEntry(root)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.password_label = tk.Label(root, text="Password:", font=("Arial", 12, "bold"), fg="#6495ED")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.password_entry = BendedEntry(root, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")


        # Center align the widgets
        for i in range(4):
            root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            root.grid_columnconfigure(i, weight=1)

    
        
        self.login_button = tk.Button(root, text="Login", command=self.validate_login, font=("Arial", 12, "bold"), bg="#6495ED", fg="white", width=20)
        self.login_button.grid(row=3, column=0, padx=(0, 0), pady=0, sticky="w")  # Decreased padx value for login button
        
        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=self.root.destroy, font=("Arial", 12, "bold"), bg="#FF4500", fg="white", width=20)
        self.exit_button.grid(row=3, column=1, padx=(0, 0), pady=0, sticky="e")  # Decreased padx value for exit button

        # Center align the widgets
        for i in range(4):
            root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            root.grid_columnconfigure(i, weight=1)

        # Center align the window
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()
        position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
        root.geometry("+{}+{}".format(position_right, position_down))


   
    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        admins = Administrators()

        if admins.has_administrator(username, password):
            admin = admins.get_administrator(username, password)
            self.root.destroy()  # Close the login window
            agency_menu_window = AgencyMenuWindow(tk.Tk(), admin.name)  # Pass the name of the user
        else:
            error_message = "Invalid username or password"
            operation_hint = "Please check your credentials and try again."
            error_window = tk.Toplevel()
            error_view = ErrorWindow(error_window, error_message, operation_hint)





class ErrorWindow:
    def __init__(self, master, error_message, operation_hint):
        self.master = master
        self.master.title("Error")
        self.master.geometry("418x340")  # Set the dimensions of the error window
        self.error_message = error_message
        self.hint_message = operation_hint
        # Load error background picture
        icon_image = Image.open("error_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)

        self.master.tk.call('wm', 'iconphoto', self.master._w, icon_photo)

        flight_image = Image.open("error.png")
        width, height = flight_image.size
        new_width = 418  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        flight_image = flight_image.resize((new_width, new_height))

        flight_photo = ImageTk.PhotoImage(flight_image)
        flight_label = tk.Label(master, image=flight_photo)
        flight_label.image = flight_photo
        flight_label.grid(row=0, column=0, columnspan=5, pady=20)

        # Error message
        welcome_label = tk.Label(master, text="Error", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=3, pady=20)

        # Create a label to display the error message

        error_message_label = tk.Label(master, text=self.error_message, font=("Arial", 12, "bold"), fg="red")
        error_message_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Create a label to display the hint message
        hint_message_label = tk.Label(master, text=self.hint_message, font=("Arial", 12, "bold"), fg="#6495ED")
        hint_message_label.grid(row=4, column=0, columnspan=3, pady=10)

        # Create a "Close" button to close the error window
        close_button = tk.Button(master, text="Close", command=self.close_window, font=("Arial", 12), bg="#6495ED", fg="white", width=45)
        close_button.grid(row=5, column=0, columnspan=3, pady=0)

    def close_window(self):
        self.master.destroy()




if __name__ == "__main__":
    agency = Agency()
    destinations_instance = Destinations(agency)

    login_window = LoginWindow(tk.Tk())
    tk.mainloop()
    
    
