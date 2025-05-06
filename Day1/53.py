#length and findin something
# 

name = input("enter you name:")

result = len(name)

print(result)

results= name.find("i") #for first occurance

results= name.rfind("i") # for reverse means it finds the last one, it will give negative if it doesnt find the letter 


print(results)

name = name. capitalize() # capitals the first letter
name = name.upper() # all charac are upper now
#same for the lower .lower

name. isdigit() # means if the sting only contains digit its gonna show true or else false

result = name.isalpha() # is alpha means it always return a bullion means true or false and has no numbers only alphabets

name.replace("-"," ") # replace is used to replace anything

#for need more types and you forgot use
print(help(str))