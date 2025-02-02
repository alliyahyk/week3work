#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# used len method to get the length of the Belgium string
# then multiplied it by a hyphen string to get 81 hyphens as a line
print(len(Belgium) * "-")

# used replace method to change the commas to colons within the string.
print(Belgium.replace(",", ":"))

# created a new variable called country rather than Belgium so it doesn't clash
# with the first variable defined as Belgium
# used a string slice to get the population number from Belgium within the string
# used the 'int' built-in function to convert the string of numbers to integers to
# be able to add them together

country = (int(Belgium[8:16]))

# created a new variable for Brussels and repeated the process as before

capital_city = (int(Belgium[26:32]))

# by creating 2 new variables, able to create a total variable to define the sum

total = country + capital_city

# printed the total which is the country and capital_city added together

print(total)

# Defining baking ingredients as a dictionary
ingredients = {'Flour': 100, 'Caster Sugar': 240, 'Eggs' : 3, 'Unsalted Butter': 240, 'Milk Chocolate': 225, 'Cocoa Powder': 100}

# this is a for loop which will run through each key:value until it has reached
# the final one. We use the for loop as we know how many variables we have.
# shopping_list will order the dictionary from the first item
# question: why don't we have to define what shopping list and baking is?

# enumerate will add a number to the beginning of the key to present as a list.
# this is a built-in function. By using the keys method, this will enumerate the key.
# the named argument 'start' is defining the starting number of enumeration to be 1.

for shopping_list, baking in enumerate(ingredients.keys(), start=1):
# f string allows for variables to be added within the string.
# {} are placeholders to input the variables.
# 2d provides 2 digit space padding moving it more to the right
# <20s moves the values to the left with a 20 character string space padding
# >20s would move the keys to the right by 20 characters string
# 06 gives the number of integers to display in the console.
# .2 gives the number of digits to display after the decimal point.
    print(f"{shopping_list:2d} {baking:<20s} {ingredients[baking]:06.2f}")
