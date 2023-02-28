# Build BMI Calculator

# Take in user's name
name = input("Hi, kindly enter your name here: ")

# Take in user's weight and height
weight = int(input(f"{name}, input your weight (in pounds): "))
height = int(input(f"{name}, input your height (in inches): "))

# Calculate BMI
bmi = (weight * 703) / (height ** 2)

# BMI result
if bmi > 0:
    if bmi < 18.5:
        print(f"{name}, your BMI is {bmi}, you are underweight")
    elif bmi <= 24.9:
        print(f"{name}, your BMI is {bmi}, you are normal weight")
    elif bmi <= 29.9:
        print(f"{name}, your BMI is {bmi}, you are overweight")
    elif bmi <= 34.9:
        print(f"{name}, your BMI is {bmi}, you are obese")
    elif bmi <= 39.9:
        print(f"{name}, your BMI is {bmi}, you are severely obese")
    elif bmi >= 40:
        print(f"{name}, your BMI is {bmi}, you are morbidly obese")
# Incase wrong values were inputted
else:
    print("Oops, looks like you entered wrong inputs, kindly retry")