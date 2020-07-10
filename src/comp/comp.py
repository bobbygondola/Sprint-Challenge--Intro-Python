# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("=====================================\n")
print("Starts with D:")
a = [humans.name for humans in humans if humans.name[0] == "D"]
print(a)
print("=====================================\n\n\n")
print("**")
# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("=====================================\n")
print("Ends with e:")
b = [human.name for human in humans if human.name[-1] == "e"]
print(b)
print("=====================================\n\n")
print("**")

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("=====================================\n")
print("Starts between C and G, inclusive:")
c = [human.name for human in humans if human.name[0] in ['C','D','E','F','G']] 
print(c)
print("=====================================\n\n")
print("**")

# Write a list comprehension that creates a list of all the ages plus 10.
print("=====================================\n")
print("Ages plus 10:")
d = [x.age + 10 for x in humans]
print(d)
print("=====================================\n\n")
print("**")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("=====================================\n")
print("Name hyphen age:")
e = ["".join(humans.name[0:] + "-" + str(humans.age)) for humans in humans]
print(e)
print("=====================================\n\n")
print("**")
# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("=====================================\n")
print("Names (TUPLES) and ages between 27 and 32:")
f = [f'({human.name}, {human.age})' for human in humans if human.age in range(27,33)]
print(f)
print("=====================================\n\n")
print("**")
# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.

print("=====================================\n")
print("All names uppercase:")
g = [(human.name.upper(), human.age + 5) for human in humans]
print(g)
print("=====================================\n\n")
print("**")
# Write a list comprehension that contains the square root of all the ages.
print("=====================================\n")
print("Square root of ages:")
import math
h = [math.sqrt(humans.age) for humans in humans]
print(h)
print("=====================================\n\n")
print("**")
