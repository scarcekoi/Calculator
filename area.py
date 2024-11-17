def calculate_area(length, width):
    area = length * width
    return area

length = int(input("Length: "))
width = int(input("Width: "))

area = calculate_area(length, width)

print(f"The area is {area}.")
