# Defining planets with dictionary
planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 149.597870, 'Mars': 227.94}

# string.format() example
# For loop is continuing to run for as long as you add in keys and values to the dictionary.
# Index is ordering the dictionary from the beginning to start with Mercury
# .keys() is a method to take the key from the planets variable and enumerate it.
# start=1 is beginning this from number 1
# Enumaration is starting from 1 and counting alongside the planets
# start is an example of a named argument
for index, planet_name in enumerate(planets.keys(), start=1):
    # print(index, planet_name, planets[planet_name])
    # .format() is a method to present the print/arguments in a particular order and style
    print("{:2d} {:<10s} {:06.2f} Gm".format(index, planet_name, planets[planet_name]))
# above is a string, it is using the format method of a string
# we want it to look nice so the format is making it look nice
# positional passing of arguments 1 on left goes to 1 on right
# d is saying its a whole number, 2 is the width
# < left alignment
# last one f is floating number, entire width should take up 6 characters


# literal string interpolation
# 'f' string - stops the need for needing the method
# Line 23 is a more succinct version of line 13
# f is being used to indent variables into the string
# {} act as placeholders in the string
for index, planet_name in enumerate(planets.keys(), start=1):
    # print(index, planet_name, planets[planet_name])
    print(f"{index:2d} { planet_name:<10s} {planets[planet_name]:06.2f} Gm")
#     f string is a format string used at the start
