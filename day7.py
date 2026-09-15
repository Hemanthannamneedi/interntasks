# coding task:
marks = [86,98,56,64,63]
total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print("marks: ",marks)
print("total: ",total)
print("average: ",average)
print("grade: ",grade)



# assignment:

number = [43,46,12,6,75,8]
print("Original numbers: ",number)
number.sort()
print("After sorting: ",number)
search = int(input("enter a number to search: "))
if search in number:
    print(search,"is present in the list.")
else:
    print(search,"is not present in the list.")


# list:

fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits)
fruits.insert(1, "Grapes")
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.sort()
print(fruits)

# tuple:

coordinates = (16.0, 80.0)
print("Coordinates:", coordinates)
print("First value:", coordinates[0])
print("Second value:", coordinates[1])

# sets:

# fruits = {"Apple", "Banana", "Mango", "Apple"}
# print(fruits)
# fruits.add("Orange")
# print(fruits)
