def calculate_fraction(numerator, denominator):
    fraction = numerator / denominator
    return fraction

numerator = int(input("Numerator: "))
denominator = int(input("Denominator: "))

fraction = calculate_fraction(numerator, denominator)

print(f"The decimal form of the fraction is {fraction}.")
