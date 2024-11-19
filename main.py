# Define the calculation functions
def calculate_area(length, width):
    area = length * width
    return area

def calculate_fraction(numerator, denominator):
    if denominator == 0:
        return "Error: Division by zero"
    fraction = numerator / denominator
    return fraction

def calculate_perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter

def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

# Main loop for multiple calculations
while True:
    # Ask the user for their choice of calculation
    choice = input("What would you like to calculate? (Area, Fraction, Perimeter, or Volume): ").strip().lower()

    # Handle the user's choice and prompt for necessary inputs
    if choice == 'area':
        length = int(input("Length: "))
        width = int(input("Width: "))
        area = calculate_area(length, width)
        print(f"The area is {area}.")
    elif choice == 'fraction':
        numerator = int(input("Numerator: "))
        denominator = int(input("Denominator: "))
        fraction = calculate_fraction(numerator, denominator)
        print(f"The decimal form of the fraction is {fraction}.")
    elif choice == 'perimeter':
        length = int(input("Length: "))
        width = int(input("Width: "))
        perimeter = calculate_perimeter(length, width)
        print(f"The perimeter is {perimeter}.")
    elif choice == 'volume':
        length = int(input("Length: "))
        width = int(input("Width: "))
        height = int(input("Height: "))
        volume = calculate_volume(length, width, height)
        print(f"The volume is {volume}.")
    else:
        print("Invalid choice. Please choose either 'Area', 'Fraction', 'Perimeter', or 'Volume'.")

    # Ask if the user wants to do another calculation
    continue_choice = input("Would you like to do another calculation? (yes/no): ").strip().lower()

    if continue_choice != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break
