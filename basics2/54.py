username = input("enter your username :")

if len(username) >12:
    print("your username cant be greator than 12 character")
elif not username.find(" ") == -1:
    print(" you username cant contain spaces")
elif not username.isalpha():
    print("your username cnt contains numbers")
else :
    print("awesome you are welcome")




