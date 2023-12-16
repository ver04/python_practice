# user height in meters
height = float(input())
# user weight in kilograms 
weight = int(input())

# count bmi
bmi = weight / (height **2)

# print the result of bmi
if bmi < 18.5:
  result = f"Your BMI is {bmi}, you are underweight."
  print(result)
elif bmi < 25:
  result = f"Your BMI is {bmi}, you have a normal weight."
  print(result)
elif bmi < 30:
  result = f"Your BMI is {bmi}, you are slightly overweight."
  print(result)
elif bmi < 35:
  result = f"Your BMI is {bmi}, you are obese."
  print(result)
else:
  result = f"Your BMI is {bmi}, you are clinically obese."
  print(result)

