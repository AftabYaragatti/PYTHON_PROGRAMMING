#Swap of Two Values using Temparary Variable
a=int(input("Enter First Value :"))
b=int(input("Enter Second Value :"))

print('First Method To Swap With Using Temparary Variable')
print(f"A = {a}, B = {b}")
temp=a
a=b
b=temp
print(f"A = {a}, B = {b}")

print('Second Method To Swap Without Using Temparary Variable')
print(f"A = {a}, B = {b}")
a=a+b #a=1,b=2-> a=3
b=a-b #a=3,b=2-> b=1
a=a-b #a=3,b=1-> a=2
print(f"A = {a}, B = {b}")

print('Third Method To Swap Without Using Temparary Variable')
print(f"A = {a}, B = {b}")
a,b=b,a
print(f"A = {a}, B = {b}")

print('Fourth Method To Swap Without Using Temparary Variable')
print(f"A = {a}, B = {b}")
a=a^b
b=a^b
a=a^b
print(f"A = {a}, B = {b}")