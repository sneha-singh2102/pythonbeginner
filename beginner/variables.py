## number variables
import math

currentYear = 2024
birthYear = 1992
age =  currentYear - birthYear

print("current age = ", age)

## area of a rectangle
length = 12
breadth = 6
area = length * breadth
print("rectangle area = ", area)

## area of a circle
radius = 6
area = radius * radius * math.pi
print("circle area = ", area)
print("circel area round off to 2 decimals = ", round(area,2))

## strings
street = "6th cross 12th main"
area = "HSR Layout"
city = "Bangalore"
state = "Karnataka"
print("Address using vars", street, area, city, state)
f_string_address = f'{street} {area} {city} {state}'
print("Address using f-string",f_string_address)
print("print main in street using negative index", street[-4:])
print(f"i live in {state}")

