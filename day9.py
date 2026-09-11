# Coding Task:
# text = "    heMAnTh anNaMneEdI  "
# cleaned_text = text.strip().title()
# print("Original String: ",text)
# print("After Cleaning: ",cleaned_text)

# Assignment:
# Count vowels:

# text = input("enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print("No.of Vowels: ",count)

# Reverse a String:

# text = input("enter a string: ")
# print("Reversed String: ",text[::-1])

# Check palindrome:

# text = input("enter a string: ")
# if text == text[::-1]:
#     print("String is Palindrome.")
# else:
#     print("String is not a Palindrome.")

# Count a character:

# text = input("enter a string: ")
# char = input("enter a charecter: ")
# print("Count: ",text.count(char))

# Replace a word:

# text = input("enter a string: ")
# old_name = input("Enter word to replace: ")
# new_name = input("Enter new word: ")
# result = text.replace(old_name,new_name)
# print("Updated sentence: ",result)

# Comprehension Programs:
# square:

# numbers = [1, 2, 3, 4, 5]
# squares = [x ** 2 for x in numbers]
# print(squares)

# Even numbers:
# numbers = [1,1,3,4,2,2,6,8,4,3,7]
# EN = [x for x in numbers if x % 2 == 0]
# print("Even numbers: ",EN)

# lower to upper:
# a = input("Enter first word: ")
# b = input("Enter second word: ")
# print(a.upper(),b.upper())