# Data types

# Numbers -> floats, ints, complex, longs
# Strings
# Booleans -> True or False

# Operators

# Arithmetic operators
# + - / * %

# Comparison operators
# < > == != >= <=

# Numeric types

a = 24
b = 16

print(a + b)
print(a - b)
print(a / b)
print(a <b)

FloatNum = 1.356
IntNum = 4
print(type(FloatNum + IntNum))

one_third = 1 / 3
print(one_third)
print(one_third * 3)

# Strings

single_quotes = 'Single'
double_quotes = "Double"
print(single_quotes)
print(double_quotes)

# String slicing

hi = "Hello World"
print(hi[2:7])
print(hi[-5:])

# String Methods

white_space = "Lots of white space                                                   "
print(len(white_space))
print(len(white_space.strip()))
print(white_space.strip())
print(white_space.lower())
print(white_space.count("e"))
print(white_space.replace("white" , "black"))

# Concatenation & Casting

x = 2
y = 5.4
z = "This is a string"
zz = "This is also a string"
print(z + " " + zz)
print(str(x) + " " + str(y) + " " + z)

int_string = "6"
print(int(int_string))
print(type(int(int_string)))

# F-Strings

name = "kipo"
years = 3
height_cm = 32.5

print(f"{name.upper()} is {years} years old")

pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi: .3f}")