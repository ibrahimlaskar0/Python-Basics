letter = ''' dear <|Name|>,
             you are slected!
             <|Date|>'''

name=input (" enter your name:")

date= input ("enter date:")


print(f"dear {name},\nYou are selected!\n{date}")


#or without user inpur it can be written as
letter = ''' dear <|Name|>,
             you are slected!
             <|Date|>'''

print(letter.replace("<|Name|>", "ibrahim").replace("<|Date|>"," 21st september"))
