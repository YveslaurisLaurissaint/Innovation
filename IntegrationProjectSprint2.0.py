# Yveslauris Laurissaint, 1:30 - 2: 45
# This program is actually useful to me as I am heavily interested in fitness and enjoy training.
# A calculator that calculates your body fat and approximate BMI.
# Also features a quiz that helps you determine what your exact goals in the gym are.
# Sources - Calculator.net, Ideal weight and BMI calculators
print("Hello!")
userName = input("What is your name?: ").lower()
x = "a"
y = "z"
# variables created
if x <= userName <= y:
    # received help from professor Oscheroff for if statement
    print("Hi,", userName + "!", "Welcome to the Fitness Information Dispensary.")
    # concatenation was used in the line above, hence the +
else:
    print("Error, please enter your name.")
print("A program in which your ideal weight, approx BMI, and fitness knowledge will be estimated and tested.")
print("(In order for accurate results, must be over 5 ft tall and at least 18 years of age.)")
# if else statement, if anything other than an alphabetical value is entered, then it will print error statement
moveOn = input("Please enter any key to continue: ")
# point in which user can take their time to read and continue when ready
print("Firstly, your estimated ideal weight will be calculated!")

age = int(input("Enter your age: "))
height = int(input("Enter your height in inches: "))
print("Enter your gender" ",", "male or female: ")
gender = input()
# line 25,26 was also done using information provided by prof Oscheroff
over5 = float(height - 60)
# for ideal weight formula, inches over 5 feet is needed for calculation
manIdeal = float(52 + (1.9 * over5))
womanIdeal = float(49 + (1.7 * over5))
# multiplying variable by values to get ideal weight
lbsManIdeal = (manIdeal * 2.205)
lbsWomanIdeal = (womanIdeal * 2.205)
# conversion used to change both genders ideal weights from kgs to lbs
# overall equation that was used is from calculator.net
if gender == "male":
    print(userName, ", your estimated ideal weight in lbs is: ", format(lbsManIdeal, '.2f', ) + "!", sep="")
elif gender == "female":
    print(userName, ", your estimated ideal weight in lbs is: ", format(lbsWomanIdeal, '.2f', ) + "!", sep="")
    # + was used in attempt of concatenation for both if and elif
else:
    print("Ideal Weight cannot be calculated!")
# if anything other than male or female is inputted, your weight will not be calculated.
moveOn = input("Please enter any key to continue: ")

print("Now that you've calculated your ideal weight, it's time to find out about BMI!")
print(
    "Your body mass index is a equation that determines whether you are at a healthy weight for your bodily measures.")

moveOn = input("Please enter any key to continue: ")
age2 = age
gender2 = gender
height2 = int(height ** 2)
# in order for calculation to work, height in inches must be raised to power of 2 (exponent)
weight = float(input("Enter your current weight please: "))
BMI = float(703 * (weight / height2))
# * and / were used in the equation to calculate the BMI (multiplication and division)
print(userName, ", your approximate BMI is: ", format(BMI, '.1f') + "!", sep="")

if BMI <= 18.5:
    # if bmi is less than or equal to 18.5, basically same thing occurs in other statements, just with diff values
    print("You are underweight!")
elif 18.5 <= BMI < 25:
    print("You are in normal range!")
elif 30 >= BMI > 25:
    print("You are in overweight range!")
elif 40 >= BMI > 30:
    print("You are in obese range!")
else:
    print("BMI not found")

print("I used the end= argument", ", I finally did all requirements", end=",")

print(44 % 9)
# modulus operator , prints out remainder
print(44 // 9)
# floor division , prints out whole number of remainder
print("strong" * 10)
# string multiplication
print("strong" + "10")
# String addition

print("Now you will be quizzed on your general fitness knowledge!")
moveOn = input("Please enter any key to continue: ")
# point of continuation
print("But first, you must guess this!"
      , "At what age does your body and strength peak? (hint : between 20 - 30)")
answer = int(input("Enter a Number: "))
# initial input for while statement
while answer != 25:
    print("Nope! Try again. ")
    answer = int(input("Enter a Number: "))
print("Correct, great job. Now to begin the real quiz. ")
# while loop so the user retries answer until correct to continue on


MO = "Moving on"
total = 0
# use of accumulator so quiz score could be calculated
print("Question 1: What is a calorie?")
print("A - A unit of energy that your body burns in order to survive. \nB - A special type of fat stored within your "
      "body. \nC - A unit used to measure your body fat.")
user_answer = input()
if user_answer == "A" or user_answer == "a":
    total += 1
    # adding to accumulator if correct answer is chosen, repeats in other questions
    print(MO)
else:
    print(MO)

print("Question 2: What weighs more and what requires protein to be formed in your body between muscle, fat, "
      "and lipids?")
for loop in range(1):
    user_answer = input("Enter an option from above: ").lower()
    user_answer2 = input("Enter an option from above: ").lower()
    # for loop that makes the user enter two answers one time
    # I understand that part of this is unnecessary
if user_answer == "muscle" and user_answer2 == "muscle":
    total += 1
    print(MO)
else:
    print(MO)

print("Question 3: true or false \nExercising turns fat into muscle")
user_answer = input().lower()
if user_answer == "false":
    total += 1
    print(MO)
else:
    print(MO)

print("Question 4: How many calories are in a pound of fat?")
print("A - 500 \nB - 1350 \nC - 2700 \nD - 3500")
# newline character used so answer choices output on separate lines
user_answer = input().lower()
if user_answer == "d":
    total += 1
    print("That was the last question!")
else:
    print("That was the last question!")

print("Your overall score was", total, "out of 4!")
# print statement telling the user their score on the quiz
condition = True
print(not condition)


# using the not boolean operator

def calculatePerimeterOfQuadrilateral(a, b, c, d):
    perimeter = a + b + c + d
    return perimeter
# defining a new function and allowing for parameters

grandTotal1 = 0

grandTotal1 -= 2
print(grandTotal1)
grandTotal2 = 3

grandTotal2 *= 3
print(grandTotal2)
grandTotal3 = 2

grandTotal3 /= 2
print(grandTotal3)

x = int(input("Choose a number: "))
if x > 5:
    print("Requirements done.")
else:
    print("Requirements still done.")
