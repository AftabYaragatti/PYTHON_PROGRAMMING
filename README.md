# Python-Practice-Daily
Python Basics | Core Python | Python Problem Solving | DSA with Python
# 🐍 Core Python – Practical Learning Repository

Welcome 👋  
This repository is a **hands-on Core Python guide** where I document my learning journey with **clear explanations, clean examples, and interview-relevant concepts**.
The goal is simple 👉 *learn Python properly and apply it confidently*.

## 🚀 Why I Created This Repository
Python is everywhere today — from web apps to AI.  
Instead of just watching tutorials, I wanted a **structured place to practice and revise Core Python**, so I created this repository.

This repo is useful for:
- 👶 Beginners starting Python
- 🎓 Students preparing for exams
- 💼 Interview preparation
- 🔁 Quick revision of concepts

## 📌 What You’ll Find Here
✔ Simple explanations  
✔ Real examples  
✔ Clean and readable code  
✔ Interview-oriented concepts  
✔ Beginner-friendly structure  

## 📚 Core Python Topics Covered
| 🔢 | Topic |
|----|------|
| 1️⃣ | Introduction to Python |
| 2️⃣ | Variables & Data Types |
| 3️⃣ | Operators |
| 4️⃣ | Conditional Statements |
| 5️⃣ | Looping Statements |
| 6️⃣ | Strings |
| 7️⃣ | Lists, Tuples, Sets & Dictionaries |
| 8️⃣ | Functions |
| 9️⃣ | Modules |
| 🔟 | Object-Oriented Programming |
| 1️⃣1️⃣ | Exception Handling |
| 1️⃣2️⃣ | File Handling |

## 🟢 1. Introduction to Python
Python is a **high-level, interpreted language** known for its simplicity and readability.
```python
print("Hello, Python 👋")
```

## 🟢 2. Variables & Data Types
Variables store data values.
```python
name = "Aftab"
age = 22
percentage = 85.5
is_developer = True
print(name, age, percentage, is_developer)
```
🔹 Python automatically understands the data type  
🔹 No need to declare types explicitly

## 🟢 3. Operators
### ➕ Arithmetic Operators
```python
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

### 🔍 Relational Operators
```python
print(a > b)
print(a == b)
```

### 🔗 Logical Operators
```python
print(a > 5 and b < 5)
```

## 🟢 4. Conditional Statements
Used to make decisions in programs.
```python
marks = 78
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 60:
    print("Good")
else:
    print("Needs Improvement")
```
💡 Used in grading systems, validations, authentication, etc.

## 🟢 5. Looping Statements
### 🔁 for Loop
```python
for i in range(1, 6):
    print(i)
```

### 🔄 while Loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

## 🟢 6. Strings
```python
text = "Python Programming"
print(text.upper())
print(text.lower())
print(text[0:6])
print(len(text))
```
✨ Strings are immutable  
✨ Powerful built-in methods available

## 🟢 7. Python Collections
### 📋 List
```python
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)
```

### 📦 Tuple
```python
colors = ("red", "green", "blue")
print(colors)
```

### 🔑 Set
```python
unique_numbers = {1, 2, 2, 3}
print(unique_numbers)
```

### 🗂 Dictionary
```python
student = {
    "name": "Aftab",
    "age": 22,
    "course": "Python"
}
print(student["name"])
```

## 🟢 8. Functions
Functions help in **code reusability and clarity**.
```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```
✔ Cleaner code  
✔ Less repetition  

## 🟢 9. Modules
```python
import math
print(math.sqrt(16))
```
📦 Modules help organize large programs.

## 🟢 10. Object-Oriented Programming (OOP)
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student("Aftab", 22)
s1.display()
```
### 🧱 OOP Concepts
- Class & Object
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

## 🟢 11. Exception Handling
Used to handle runtime errors gracefully.
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Program executed successfully")
```

## 🟢 12. File Handling
### ✍ Writing to a File
```python
file = open("data.txt", "w")
file.write("Hello Python")
file.close()
```

### 📖 Reading from a File
```python
file = open("data.txt", "r")
print(file.read())
file.close()
```

## 🎯 Learning Outcomes
By completing this repository, I have:
- Built strong Core Python fundamentals
- Improved logical thinking and problem-solving
- Gained confidence for interviews
- Prepared a solid base for advanced topics like AI & ML

## 📌 Best Practices Followed
✔ Meaningful examples  
✔ Clean formatting  
✔ Beginner-friendly approach  
✔ Interview-relevant concepts  

## 👨‍💻 About Me

**Aftab Yaragatti**  
Frontend Developer | Python Programmer
🔗 GitHub: https://github.com/AftabYaragatti  

⭐ If you find this repository helpful, feel free to give it a **star**!
