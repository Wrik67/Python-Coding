w = float(input("Enter your weight in KG: "))
h = float(input("Enter your height in meter: "))

bmi = w / h ** 2
print("Your bmi is: ", bmi)

if bmi < 18.5:
    print("You are under weight. Please gain some wait")
elif 18.5 <= bmi <= 25.9:
    print("Your weight is normal! Keep it up.")
elif 25 <= bmi <= 29.9:
    print("Your are over weight. Please loose some weight.")
elif 30 <= bmi <= 34.9:
    print("Your are obese. Loosing weight is emergency.")
else:
    print("Your are extremly obese. Please visit the doctor as soon as possible.")