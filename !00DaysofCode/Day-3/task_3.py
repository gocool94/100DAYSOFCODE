
height = input("Enter the height")

weight = float(input("Enter the weight"))

BMI = weight/(height**2)

print(BMI)

if BMI < 18:
    print("Underweight")
elif BMI > 18 and BMI <25:
    print("Normal Weight")
elif BMI > 25 and BMI < 30:
    print("Slightly Overweight")
elif BMI > 30 and BMI < 35:
    print("Obese")
elif BMI > 35:
    print("Clinically obese")

