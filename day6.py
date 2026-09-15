# coding task:
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "cannot divide by zero"
num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))

print("addition: ",add(num1,num2))
print("subtraction: ",sub(num1,num2))
print("multiplication: ",mul(num1,num2))
print("division: ",div(num1,num2))



# assignment:
# 1.factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
num = int(input("enter value: "))
print(f"factorial of {num} =",factorial(num))

# 2.palindrome
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
word = input("Enter a word: ")
if is_palindrome(word):
    print("it is palindrome")
else:
    print("not a palindrome")

# 3.area of circle
def ar_of_circle(radius):
    return 3.14159 * radius *radius
radius = float(input("Enter value: "))
print("Ar of circle= ",ar_of_circle(radius))

# 4.simple interest
def SI(principal,time,rate):
    return principal * time * rate / 100
p = float(input("Enter principal amount: "))
t = float(input("Enter time: "))
r = float(input("Enter rate of interest: "))
print("SI= ",SI(p,t,r))

# 5.even or odd
def check_E_O(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter value: "))
print("Number is: ",check_E_O(number))
