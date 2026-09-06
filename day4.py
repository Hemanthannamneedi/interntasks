# hands on practice:
# import random
#
# a = random.randint(1,7)
# print(a)
#
# cars = ["VW","AUDI","BMW","BENZ","PORSHE","RR","TATA","JAGUAR"]
# b = random.choice(cars)
# print(b)


# coding task:
# import random
#
# a = random.randint(1,9)
# guess = int(input("Guess any number in between (1 to 9): "))
#
# if guess == a:
#     print("Congratulations you predicted correct value.")
# else:
#     print("Sorry wrong guess, better luck next time.")
#     print("The correct number is: ",a)


# Assignment:
import random
a = random.randint(1,10)
attempts = 0
score = 10

while True:
    guess = int(input("Enter any number you guess in between (1 to 10): "))
    attempts += 1
    if guess == a:
        print("congratulations, you guessed the right one.")
        print("No.of Attempts: ",attempts)
        print("Your score: ",score)

    elif guess < a:
        print("The number you guess is too low, Try again")
        score -= 1
    else:
        print("The number you guessed is too high, Try again")
        score -= 1

    if score == 0:
        print("Game OVER!!!")
        print("Correct number is: ",a)
        print("Score: ",score)
        break