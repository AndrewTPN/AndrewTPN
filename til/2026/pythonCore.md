# Today I Learned

## Date: January 15, 2026

## Core Python Concepts

### Function

A function is a block of code that can be used to perform a specific task.

**Example:**

 python
name = input("What your name is?: ")  # This is how we collect the input from the user as variable name

def greeting(name):  # This is how to define a function
    print("Hello, " + name)  # This is the output

greeting(name)  # Function call

-------------------------------------------------
### Function vs Method

**Function:** A function does not have any relationship with an object.

```python
name = 'Andrew'
def greeting(name):
    return "Hello, " + name

print(greeting(name))
```

**Method:** A method is a function that is abstracted from an object.

```python
# Method belongs to an object
name.greeting()  # In here greeting belongs to the object name
```

**Key Difference:** A method is a function that is abstracted from an object. With function, it does not have any relationship with an object.
----------------------------------------------------------------------

### Format Specifier in Python

- `{:.2f}` = Round the number to 2 decimal places
- `{:.0f}` = Round the number to 0 decimal places
- `{:.number}` = Allocate the number of decimal places
----------------------------------------------------------------------
### Operators

An operator is a symbol that is used to perform an operation. We have 2 kinds:

1. **Normal syntax:** `(+, -, *, /, %, **, //)` - For basic calculations
2. **Operator functions:** `(add, subtract, multiply, divide, modulo, power, floor division)` - For more complex calculations
----------------------------------------------------------------------
**Normal Syntax Examples:**

1 + 1 = 2      # Addition
1 - 1 = 0      # Subtraction
1 * 1 = 1      # Multiplication
2 / 1 = 2      # Division
1 % 1 = 0      # Modulo (remainder of division)
3 ** 2 = 9     # Power (exponent)
5 // 2 = 2     # Floor division (division rounded down to nearest integer)

**Operator Functions (using math module):**
```python
import math
math.add(a, b)
math.subtract(a, b)
math.multiply(a, b)
math.divide(a, b)
math.modulo(a, b)
math.power(a, b)
math.floor_division(a, b)
```

### Index Operator

Index operator is a way to access the element of a list or a string.

**Examples:**
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])      # Output: 1
print(numbers[-1])     # Output: 5 (last element)
print(numbers[1:3])    # Output: [2, 3] (slicing)
print(numbers[:3])     # Output: [1, 2, 3] (from start to index 3)
print(numbers[3:])     # Output: [4, 5] (from index 3 to end)
print(numbers[:])      # Output: [1, 2, 3, 4, 5] (all elements)
print(numbers[::2])    # Output: [1, 3, 5] (every 2nd element)
print(numbers[1::2])   # Output: [2, 4] (every 2nd element starting from index 1)
print(numbers[::-1])   # Output: [5, 4, 3, 2, 1] (reversed)
```

### String Operations

**Count characters in a string:**
```python
text = "I am a software developer"
print(len(text))  # Output: 27 (counts all characters including spaces)
```

**Count words in a string:**
```python
text = "I am a software developer"

def count_words(text):
    return len(text.split())  # Split by space and count the number of words

print(count_words(text))  # Output: 5
```

**Access first character of a string:**
```python
text = "I am a software developer"
print(text[0])  # Output: 'I' (first index of the string)
```
-------------------------------------------------------------------
Data structure:
**Dictionary**



