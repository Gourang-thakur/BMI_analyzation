
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = (round((weight / (height**(2))),2))
#if statement 
if BMI <=18:
  print("you are underweight.")
elif BMI<=22:
  print("you have a normal weight")
elif BMI<=28:
  print("you are slightly overweight")
elif BMI<=33:
  print("you are clinically obese.")
else:
  ("you are clinically obese")