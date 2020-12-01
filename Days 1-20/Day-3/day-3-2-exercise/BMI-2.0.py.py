# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/(height**2))
if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"your BMI is {bmi}, you are normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"your BMI is {bmi}, you are slightlt overweight.")
elif bmi > 30 and bmi < 35:
    print(f"your BMI is {bmi}, you are obese.")
else:
    print(f"your BMI is {bmi}, you are clinically obese.")