def greet():
    print("Hello from function!")

greet()
greet()
# so what it does is if i need to run the code multiple time 
#i just write greet() the no of times i write this the no of 
#time it prints

#ARGUMENTS

def greet(name, time):
    print(f"Hello{name}")
    print(f"its{time}now")

greet("ibrahim",7)

#example of arguments
def invoice(name, price, date):

    print(f" hello {name} , your total amount is {price} and the date is {date}")

invoice("ibrahim", 42 , "08/05/2005")
    

#return
def add(x,y):
    z = x+y
    return z
print(add(1,2))

#example

def create_name(first,last):
    first = first.capitalize()
    last= last.capitalize()
    return first+ " " + last

full_name = create_name("ibrahim", "laskar")
print(full_name)