def calculate_perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter

length = int(input("Length: "))
width = int(input("Width: "))

perimeter = calculate_perimeter(length, width)

print(f"The perimeter is {perimeter}.")
