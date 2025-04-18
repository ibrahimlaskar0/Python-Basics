p1="make a lot of money"
p2="easy money"
p3="join telegram to earn a macbook"
p4="click this link below"

message = input("enter message")


if ((p1 in message) or (p2 in message)or(p3 in message) or (p4 in message)):
    print("this is a spam")

else:
    print(" this is not a spam")


    