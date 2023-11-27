#bmi calculator  👆

# importing math module
import math


height = input()
weight = input()

num_height = float(height) ** 2
num_weight = int(weight)

# below code is use to get the data type 👇
# print(type(num_height))
# print(type(num_weight))

bmi = num_weight / num_height
print(math.ceil(bmi))