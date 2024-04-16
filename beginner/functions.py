import math
def calculate_area(length, breadth, shape):

    if shape=="triangle":
        area = length * breadth *1/2
        perimeter = 2 * (length + breadth)
    elif shape=="square":
        area = length * breadth
        perimeter = 2 * (length + breadth)
    elif shape=="rectangle":
        area = length * breadth
        perimeter = 2 * (length + breadth)
    elif shape=="circle":
        area = length * breadth *math.pi
        perimeter = 2 * length * math.pi
    else:
        print("Invalid shape")
        area=0
        perimeter=0
    return area, perimeter

print("area and perimeter of triangle: ", calculate_area(13,5,"triangle"))

