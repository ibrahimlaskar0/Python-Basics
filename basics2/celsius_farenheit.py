unit = input ("is the temp in celsius and farenheit (C/F) :")
temp = float(input("enter the temp:"))

if unit == "C":
    temp = (temp*9/5) + 32
    unit = "F"
    print(f" the temp is {temp} {unit}")
elif unit == "F":
    temp = (temp-32) *5/9
    unit = "C"
    print(f" the temp is {temp} {unit}")
else:
    print(f" this {unit} is not a valid unit")