import tkinter as tk
from PIL import Image, ImageTk

class ErrorWindow:
    def __init__(self, root, error_message, hint_message):
        self.root = root
        self.root.title("Error")
        self.root.geometry("418x340")

        # Load error icon and background images
        
        icon_image = Image.open("error_icon.png")  # Replace with your actual icon file
        icon_photo = ImageTk.PhotoImage(icon_image)
        
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_photo)
        
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

        hint_message_label = tk.Label(self.root, text=error_message, font=("Arial", 12, "bold"), fg="red")
        hint_message_label.grid(row=3, column=0, columnspan=3, pady=10)
        # Create a label to display the hint message
        hint_message_label = tk.Label(self.root, text=hint_message, font=("Arial", 12, "bold"), fg="#6495ED")
        hint_message_label.grid(row=4, column=0, columnspan=3, pady=10)

        # Create a "Close" button to close the error window
        close_button = tk.Button(self.root, text="Close", command=self.close_window, font=("Arial", 12), bg="#6495ED", fg="white", width = 45)
        close_button.grid(row=5, column=0, columnspan=3, pady=0)

    def close_window(self):
        self.root.destroy()

# Usage
if __name__ == "__main__":
    root = tk.Tk()
    error_message = "An error occurred while performing an operation."
    hint_message = "Please check your input and try again."
    error_window = ErrorWindow(root, error_message, hint_message)
    root.mainloop()
