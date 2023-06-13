# **Intro to Python**

#### Python is a dynamically typed programming language. i.e., Python recognises the data type so it doesn't have to be assigned manually.

## Variables

 A variable is a way to store data within a program. It can be a reference to that data, and is mutable.

 Variables can be created using this method:

```commandline
variable_name = variable_data
```
For example,

```commandline
greeting = "Hello world!"
a = 2
b = 4.5
```
Variables are mutable and can be overwritten.
In the following example, the first value of *a* will be printed, followed by the second value of *a*.
```commandline
a = 2
print(a)
a = 5
print(a)
```
Sometimes, we may not know the data for a variable, and we need to get this from a user. We can do this using the *input()* method.

```commandline
print("What is your name? ")
name = input()
print("Hi " + name)

age = input("What is your age? ")
print("Wow, " + age + " is well old!")

dob = input("What is yur date of birth? ")
print("I'm pretty sure the dinosaurs were around in " + dob)

address = input("What is your address? ")
print(address + " is a lovely part of the world")
```
In this instance, the user's name, age, date of birth and address are stored in variables after the user has entered them.

## Data Types

There are three main data types: numbers, strings and booleans. We can use arithmetic and comparison operators to perform operations on variables.

### Numbers
Numbers would include integers, floats, complex numbers and longs. They can be stored in variables to perform arithmetic.
```commandline
a = 24
b = 16

print(a + b)
print(a - b)
print(a / b)
```

### Strings
Strings are any characters within single or double quotation marks. Strings can be stored in variables.
```commandline
hi = "Hello World"
print(hi)
```
If we just want one section of the string, we can slice it. The index of the first character is 0, the second character is 1, and so on.
```
print(hi[2:7])
print(hi[-5:])
```
Strings can be concatenated 
### Booleans
Booleans are where an expression is **True** or **False**.
```commandline
x = 5
y = 10
print(x == y)
```
The answer to the above is *False*.
```commandline
print(x < y)
```
The answer to the above is *True*.

```commandline
a = True
b = False

print(a == b)
print(a != b)
print(a >= True)
print(b <= False)
```
The output for the above is:
```commandline
False
True
True
True
```