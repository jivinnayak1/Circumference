import math

def calculate_circumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference

# Example usage:
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference}")
