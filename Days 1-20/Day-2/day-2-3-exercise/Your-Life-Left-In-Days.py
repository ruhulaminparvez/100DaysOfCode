# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)

age_remaining = 90 - age_as_int

days = age_remaining * 365
weeks = age_remaining * 52
month = age_remaining * 12

print(f"You have {days} days, {weeks} weeks, and {month} months left.")









