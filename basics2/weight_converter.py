#python weight converter


weight = float(input("enter you weight :"))

unit = input(" kilograms or pounds? (K or L): ")

if unit == "k":
    weight = weight*2.205
    unit = "lbs"
    print(f"the weight after conversion is {weight} {unit}")

    
elif unit == "l":
    weight = weight /2.205
    unit = "kgs"
    print(f"the weight after conversion is {weight} {unit}")
else:
    print(f"its invalid {unit}")
