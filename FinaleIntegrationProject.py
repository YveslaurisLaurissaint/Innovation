"""

This program is actually useful to me as I am heavily interested in
fitness and enjoy training.
A calculator that calculates your body fat and approximate BMI.
Also features a quiz that helps you determine your basic knowledge and
comprehension of fitness.
Sources - Calculator.net, Ideal weight and BMI calculators

"""
__author__ = "Yveslauris Laurissaint"


def calculateperimeterofquadrilateral(a, b, c, d):
    """

    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    perimeter = a + b + c + d
    return perimeter


def main():
    """
    this is the main part of the code that runs entire program
    """
    print("Hello!")
    keepLooping = True
    firstLetter = "a"
    lastLetter = "z"
    # variables created for conditional statement
    while keepLooping:
        userName = input("What is your name?: ").lower()
        if firstLetter <= userName <= lastLetter:
            # received help from professor Oscheroff for if statement
            print("Hi,", userName + "!",
                  "Welcome to the Fitness Information Dispensary.")
            keepLooping = False
        # concatenation was used in the line above, hence the +
        else:
            print("Error, please enter a name using only letters.")
    print(
        "A program in which your ideal weight, approx BMI, and fitness "
        "knowledge "
        "will be estimated and tested.")
    print(
        "(In order for accurate results, must be over 5 ft tall and at "
        "least 18 years of age.)")
    # if else statement, if anything other than an alphabetical value is
    # entered,
    # then it will print error statement
    moveOn = input("Please enter any key to continue: ")
    # point in which user can take their time to read and continue when ready
    print("Firstly, your estimated ideal weight will be calculated!")
    keepLooping = True
    while keepLooping:
        try:
            age = int(input("Enter your age: "))
            keepLooping = False

        except ValueError:
            print("Enter a valid number please.")
    keepLooping = True
    while keepLooping:
        try:
            height = int(input("Enter your height in inches: "))
            keepLooping = False

        except ValueError:
            print("Enter a valid number please.")

    keepLooping = True
    while keepLooping:
        gender = input("Please enter your gender, M or F: ").lower()
        if gender == "m" or gender == "f":
            keepLooping = False
        # concatenation was used in the line above, hence the +
        else:
            print("Error, please enter M or F.")

    over5 = float(height - 60)
    # for ideal weight formula, inches over 5 feet is needed for calculation
    manIdeal = float(52 + (1.9 * over5))
    womanIdeal = float(49 + (1.7 * over5))
    # multiplying variable by values to get ideal weight
    lbsManIdeal = (manIdeal * 2.205)
    lbsWomanIdeal = (womanIdeal * 2.205)
    # conversion used to change both genders ideal weights from kgs to lbs
    # overall equation that was used is from calculator.net
    if gender == "m":
        print(userName, ", your estimated ideal weight in lbs is: ",
              format(lbsManIdeal, '.2f', ) + "!", sep="")
    elif gender == "f":
        print(userName, ", your estimated ideal weight in lbs is: ",
              format(lbsWomanIdeal, '.2f', ) + "!", sep="")
        # + was used in attempt of concatenation for both if and elif
    else:
        print("Ideal Weight cannot be calculated!")
        # specify what was wrong, add loop so user can retry
    # if anything other than male or female is inputted, your weight will not
    # be calculated.
    moveOn = input("Please enter any key to continue: ")

    print(
        "Now that you've calculated your ideal weight, it's time to find out "
        "about BMI!")
    print(
        "Your body mass index is a equation that determines whether you are "
        "at "
        "a "
        "healthy weight for your bodily measures.")

    moveOn = input("Please enter any key to continue: ")
    height2 = int(height ** 2)
    # in order for calculation to work, height in inches must be raised to
    # power of 2 (exponent)
    keepLooping = True
    while keepLooping:
        try:
            weight = float(input("Enter your current weight in pounds "
                                 "please: "))
            keepLooping = False
        except ValueError:
            print("Enter a valid number please.")

    BMI = float(703 * (weight / height2))
    # * and / were used in the equation to calculate the BMI (multiplication
    # and division)
    print(userName, ", your approximate BMI is: ", format(BMI, '.1f') + "!",
          sep="")

    if BMI <= 18.5:
        # if bmi is less than or equal to 18.5, basically same thing occurs
        # in other statements, just with different values
        print("You are underweight!")
    elif 18.5 <= BMI < 25:
        print("You are in normal range!")
    elif 30 >= BMI > 25:
        print("You are in overweight range!")
    elif 40 >= BMI > 30:
        print("You are in obese range!")
    else:
        print("BMI not found")

    print("I used the end= argument", ", I finally did all requirements",
          end=",")

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
    print("But first, you must guess this!",
          "At what age does your body and strength peak? (hint : between 20 - "
          "30)")
    continueToLoop = True
    # initial input for while statement

    skipPast = input("Enter S if you wish to skip this question: ").lower()
    if skipPast != "s":
        while continueToLoop:
            tempAnswer = input("Enter a number or S to skip: ").lower()
            if tempAnswer == "s":
                continueToLoop = False
            else:
                try:
                    answer = int(tempAnswer)
                    if answer == 25:
                        print("Correct, great job! Now to begin the real "
                              "quiz. ")
                        continueToLoop = False

                except ValueError:
                    print("Enter a valid number please.")
    else:
        print("Onward!")

    # while loop so the user retries answer until correct to continue on
    # or enters an S in order to skip, either in beginning or mid-loop
    # also made with help from Prof Osheroff

    MO = "Moving on"
    total = 0
    # use of accumulator so quiz score could be calculated
    print("Question 1: What is a calorie?")
    print(
        "A - A unit of energy that your body burns in order to survive. \nB - "
        "A special type of fat stored within your "
        "body. \nC - A unit used to measure your body fat.")
    user_answer = input("Enter a letter choice: ")
    if user_answer == "A" or user_answer == "a":
        total += 1
        # adding to accumulator if correct answer is chosen, repeats in other
        # questions
        print(MO)
        # print whether answer is correct
    else:
        print(MO)

    print(
        "Question 2: What weighs more and what requires protein to be formed "
        "in your body between muscle, fat, "
        "and lipids?")
    for loop in range(1):
        user_answer = input(
            "Enter an option between the 3 from above: ").lower()
        user_answer2 = input("Enter another option between "
                             "the 3 from above: ").lower()
        # for loop that makes the user enter two answers one time
        # I understand that part of this is unnecessary
    if user_answer == "muscle" and user_answer2 == "muscle":
        total += 1
        print(MO)
    else:
        print(MO)

    print("Question 3: true or false \nExercising turns fat into muscle")
    user_answer = input("Enter T or F: ").lower()
    if user_answer == "f":
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

    perimeter = calculateperimeterofquadrilateral(3, 2, 4, 2)
    print(perimeter)
    # everything from lines 225 and on are merely for requirements


main()
