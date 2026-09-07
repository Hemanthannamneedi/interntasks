# coding task:

while True:
    print("\n ---Calculator Menu---")
    print("1.Addition")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting calculator. THANK YOU!")
        break
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Please select 1 to 5.")
        continue
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    if choice == 1:
        print(f"Addition of {num1} and {num2} is: ",num1 + num2)
    elif choice == 2:
        print(f"Subtraction of {num1} and {num2} is: ",num1 - num2)
    elif choice == 3:
        print(f"Multiplication of {num1} and {num2} is: ", num1 * num2)
    elif choice == 4:
        if num2!= 0:
            print(f"Division of {num1} and {num2} is: ", num1 / num2)
        else:
            print("Cannot divide")




