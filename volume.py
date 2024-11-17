def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

length = int(input("Length: "))
width = int(input("Width: "))
height = int(input("Height: "))

volume = calculate_volume(length, width, height)

print(f"The volume is {volume}.")
