#bmi calculator  👆

# importing math module
import math

print("Welcome to BMI calculator. Lets check your BMI")
weight = int(input("What is you weight in kg?\n"))
height = float(input("What is your height in meters?\n"))

# num_height = float(height) ** 2
# num_weight = int(weight)

# below code is use to get the data type 👇
# print(type(num_height))
# print(type(num_weight))

# bmi = num_weight / num_height
bmi = round(weight / height ** 2, 2)

# print(math.ceil(bmi))


#Condition check
if bmi < 18.5:
    print(f"Your bmi is {bmi}, your are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
