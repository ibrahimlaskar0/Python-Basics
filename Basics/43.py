a = int(input("enter your age : "))

if(a>=18):
    print(" you are above the age of consent")

elif(a<0):
    print("invalid negative age")

elif(a==0):
    print(" age is invalid")

else:
    print("you are below the age of consent")

