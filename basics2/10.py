#indexing = accessing elemnts of a sequence using []

# [start:end:step]

credit_number = "1234-5678-9012-2222"

#print(credit_number[0])  means the first number it will show
print(credit_number[:4]) # it will display the numbers from the first to the fourth character
print(credit_number[5:8])  #it will display the no from the fifth to the 8th number
print(credit_number[5:]) # it will display the no from the 5th to the last number
print(credit_number[-1]) # it will display the lst digit
print(credit_number[::2]) # it will go from the first to the last taking every second character to display


print(credit_number[-4 :])
