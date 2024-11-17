import os
import subprocess

# Ask the user for their choice
choice = input("What would you like to calculate? (Area, Fraction, Perimeter, or Volume): ").strip().lower()

# Based on the user's choice, decide which file to run
if choice == 'area':
    if os.path.exists('area.py'):
        print("Running area.py...")
        subprocess.run(['python', 'area.py'])  # Run area.py
    else:
        print("Error: fraction.py not found.")
elif choice == 'fraction':
    if os.path.exists('fraction.py'):
        print("Running fraction.py...")
        subprocess.run(['python', 'fraction.py'])  # Run perimeter.py
    else:
        print("Error: fraction.py not found.")
elif choice == 'perimeter':
    if os.path.exists('perimeter.py'):
        print("Running perimeter.py...")
        subprocess.run(['python', 'perimeter.py'])  # Run perimeter.py
    else:
        print("Error: perimeter.py not found.")
elif choice == 'volume':
    if os.path.exists('volume.py'):
        print("Running volume.py...")
        subprocess.run(['python', 'volume.py'])  # Run volume.py
    else:
        print("Error: volume.py not found.")
else:
    print("Invalid choice. Please choose either 'Area', 'Perimeter', or 'Volume'.")
