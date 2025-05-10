#lists are mutable (means it can be changed)


fruits = ["apple", "banana" , "mango"]


print(fruits[0])  # prints the word that we mentioned
#since python takes 0 as first word so it prints apple


#now we will add one more word in the list

fruits.append("orange")
print(fruits)

#now we will remove one word from the list
fruits.remove("banana")
print(fruits)