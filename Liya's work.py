# Defining peoples ages with a dictionary
peoples_ages= {'Adam': 12, 'Kasim': 29, 'Oliver': 16, 'Amirah': 27, 'Alliyah': 24}

# For loop - continues as long as you add to the dictionary
# Index is ordering the dictionary in the order they were added
# .keys() is a method to take the key from the peoples_ages variable and enumerate it.
# Enumaration is starting from 1 and counting alongside the planets
# start=1 is beginning the list from number 1. Start is an example of a named argument
for index, names in enumerate(peoples_ages.keys(), start=1):
        # printing using an f string for succinctness and remove need for clarity
        # it is indenting variables within the string
        print(f"{index:2d} {names:<5s} is {peoples_ages[names]:2} years old")