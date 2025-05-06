#logical operators =evaluate multiple conditions (or,and,not)

# or = at least one condition must be true 
#and = both conditions must be tru
#not = inverts the condition (not faLse , not true)

temp = 25
is_raining = False

if temp> 35 or temp <0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("the outdoor event is still scheduled")


#now for and

temp = 25
is_sunny = True

if temp >=28 and is_sunny:
    print("It is hot outside")
    print("it is sunny")
elif temp <= 0 and is_sunny:
    print(" it is cold outside")
    print("it is sunny")
else:
    print("the weather is moderate")
    if is_sunny:
        print("it is sunny")