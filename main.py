import customtkinter as ctk
import math

# Define the calculation functions with formatting
def format_result(value):
    # If the value is an integer, show as integer with commas
    if isinstance(value, float) and value % 1 != 0:
        # Format with up to 10 decimal places and remove trailing zeros
        return "{:,.10f}".format(value).rstrip('0').rstrip('.')  # Remove unnecessary zeros and dots
    else:
        return "{:,}".format(int(value))  # Show as integer with commas

def calculate_area():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        area = length * width
        label_result.configure(text=f"Area: {format_result(area)}")  # Format the result
    except ValueError:
        label_result.configure(text="Error: Invalid input")

def calculate_circle_area():
    try:
        radius = float(entry_radius.get())
        circle_area = pow(radius, 2) * math.pi
        label_result.configure(text=f"Circle Area: {format_result(circle_area)}")  # Format the result
    except ValueError:
        label_result.configure(text="Error: Invalid input")

def calculate_circumference():
    try:
        radius = float(entry_radius.get())
        circumference = radius * 2 * math.pi
        label_result.configure(text=f"Circumference: {format_result(circumference)}")  # Format the result
    except ValueError:
        label_result.configure(text="Error: Invalid input")

def calculate_fraction():
    try:
        numerator = float(entry_numerator.get())
        denominator = float(entry_denominator.get())
        if denominator == 0:
            label_result.configure(text="Error: Division by zero")  # Format the result
        else:
            fraction = numerator / denominator
            label_result.configure(text=f"Fraction: {format_result(fraction)}")  # Format the result
    except ValueError:
        label_result.configure(text="Error: Invalid input")

def calculate_perimeter():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        perimeter = (length + width) * 2
        label_result.configure(text=f"Perimeter: {format_result(perimeter)}")  # Format the result
    except ValueError:
        label_result.configure(text="Error: Invalid input")

def calculate_volume():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        height = float(entry_height.get())
        volume = length * width * height
        label_result.configure(text=f"Volume: {format_result(volume)}")  # Format the result
    except ValueError:
        label_result.configure(text="Error: Invalid input")

def calculate_radius():
    try:
        diameter = float(entry_diameter.get())
        radius = diameter / 2
        label_result.configure(text=f"Radius: {format_result(radius)}")  # Format the result
    except ValueError:
        label_result.configure(text="Error: Invalid input")

# Function to update the result based on the active calculation
def update_result(event=None):
    selected_calculation = dropdown_calculation.get()
    if selected_calculation == "Area":
        calculate_area()
    elif selected_calculation == "Circle Area":
        calculate_circle_area()
    elif selected_calculation == "Circumference":
        calculate_circumference()
    elif selected_calculation == "Fraction":
        calculate_fraction()
    elif selected_calculation == "Perimeter":
        calculate_perimeter()
    elif selected_calculation == "Volume":
        calculate_volume()
    elif selected_calculation == "Radius":
        calculate_radius()

# Show/hide input fields based on selected calculation
def update_input_fields(selected_calculation):
    # Hide all input fields first
    for widget in frame_inputs.winfo_children():
        widget.grid_forget()

    if selected_calculation == "Area":
        entry_length.grid(row=0, column=1, padx=10, pady=10)
        entry_width.grid(row=1, column=1, padx=10, pady=10)

    elif selected_calculation == "Circle Area":
        entry_radius.grid(row=0, column=1, padx=10, pady=10)

    elif selected_calculation == "Circumference":
        entry_radius.grid(row=0, column=1, padx=10, pady=10)

    elif selected_calculation == "Fraction":
        entry_numerator.grid(row=0, column=1, padx=10, pady=10)
        entry_denominator.grid(row=1, column=1, padx=10, pady=10)

    elif selected_calculation == "Perimeter":
        entry_length.grid(row=0, column=1, padx=10, pady=10)
        entry_width.grid(row=1, column=1, padx=10, pady=10)

    elif selected_calculation == "Volume":
        entry_length.grid(row=0, column=1, padx=10, pady=10)
        entry_width.grid(row=1, column=1, padx=10, pady=10)
        entry_height.grid(row=2, column=1, padx=10, pady=10)

    elif selected_calculation == "Radius":
        entry_diameter.grid(row=0, column=1, padx=10, pady=10)

    # Clear result
    label_result.configure(text="Result will appear here")  # Use configure() instead of config()

# Create the main window
app = ctk.CTk()

# Window settings
app.title("Calculator")
app.geometry("400x500")

# Title label
label_title = ctk.CTkLabel(app, text="Calculator", font=("Arial", 20))
label_title.pack(pady=20)

# Dropdown (ComboBox) for calculation selection
dropdown_calculation = ctk.CTkComboBox(app, values=["Area", "Circle Area", "Circumference", "Fraction", "Perimeter", "Volume", "Radius"],
                                        command=update_input_fields)
dropdown_calculation.pack(pady=10)

# Frame to hold input fields
frame_inputs = ctk.CTkFrame(app)
frame_inputs.pack(padx=20, pady=10)

# Length and width entry for rectangle-based calculations
entry_length = ctk.CTkEntry(frame_inputs, placeholder_text="Length")
entry_width = ctk.CTkEntry(frame_inputs, placeholder_text="Width")
entry_radius = ctk.CTkEntry(frame_inputs, placeholder_text="Radius")
entry_numerator = ctk.CTkEntry(frame_inputs, placeholder_text="Numerator")
entry_denominator = ctk.CTkEntry(frame_inputs, placeholder_text="Denominator")
entry_height = ctk.CTkEntry(frame_inputs, placeholder_text="Height")
entry_diameter = ctk.CTkEntry(frame_inputs, placeholder_text="Diameter")

# Label to show results
label_result = ctk.CTkLabel(app, text="Result will appear here")
label_result.pack(pady=20)

# Bind the input fields to trigger update_result automatically when user types
entry_length.bind("<KeyRelease>", update_result)
entry_width.bind("<KeyRelease>", update_result)
entry_radius.bind("<KeyRelease>", update_result)
entry_numerator.bind("<KeyRelease>", update_result)
entry_denominator.bind("<KeyRelease>", update_result)
entry_height.bind("<KeyRelease>", update_result)
entry_diameter.bind("<KeyRelease>", update_result)

# Set initial input visibility
update_input_fields(dropdown_calculation.get())

# Start the app
app.mainloop()
