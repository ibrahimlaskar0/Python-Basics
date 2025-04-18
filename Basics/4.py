import os
#select the directory jiska content chahiye
directory_path = '/windows/Web'


#use the os module to list the directory content
contents = os.listdir(directory_path)

#to print the contents of the directory
for items in contents:
    print(items)