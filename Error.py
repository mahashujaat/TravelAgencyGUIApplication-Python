import tkinter as tk
from PIL import Image, ImageTk

class ErrorWindow:
    
    def __init__(self, root, error_message, hint_message):
        self.root = tk.Tk()
        self.root.title("Error")
        self.root.geometry("418x340")
        self.error_message = error_message
        self.hint_message = hint_message

        # Load error icon and background images
        
        icon_image = Image.open("error_icon.png")  # Replace with your actual icon file
        self.icon_photo = ImageTk.PhotoImage(icon_image)

        self.root.iconphoto(True, self.icon_photo)
        self.root.tk.call('wm', 'iconphoto', self.root._w, self.icon_photo)
        
        flight_image = Image.open("error.png")
        width, height = flight_image.size
        new_width = 400  # Set the desired width of the image
        new_height = int((new_width / width) * height)  # Calculate the proportional height
        flight_image = flight_image.resize((new_width, new_height))
        
        flight_photo = ImageTk.PhotoImage(flight_image)
        flight_label = tk.Label(root, image=flight_photo)
        flight_label.image = flight_photo
        flight_label.grid(row=0, column=0, columnspan=3, pady=20)
    
        welcome_label = tk.Label(root, text="Error", font=("Arial", 16, "bold"), fg="#6495ED")
        welcome_label.grid(row=1, column=0, columnspan=3, pady=20)

        # Create a label to display the error message

        error_message_label = tk.Label(self.root, text=self.error_message, font=("Arial", 12, "bold"), fg="red")
        error_message_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Create a label to display the hint message
        hint_message_label = tk.Label(self.root, text=self.hint_message, font=("Arial", 12, "bold"), fg="#6495ED")
        hint_message_label.grid(row=4, column=0, columnspan=3, pady=10)

        # Create a "Close" button to close the error window
        close_button = tk.Button(self.root, text="Close", command=self.close_window, font=("Arial", 12), bg="#6495ED", fg="white", width=45)
        close_button.grid(row=5, column=0, columnspan=3, pady=0)
        

    def close_window(self):
        self.root.destroy()


