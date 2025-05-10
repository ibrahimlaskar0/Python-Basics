try:
    num = int(input("enter the number : "))
    print(100/num) 
except ValueError:
    print("please enter a valid number ")
except ZeroDivisionError :
    print("cant divide by zero")



#what it does it it tries to divide it
#
#ifsomeone enter letters instead of int valueerror kicks in and prints enter a valid number(ValueError)
#if someone enters zero then it will print cant divide by zero(ZeroDivisionError)
