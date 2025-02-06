# to get the current working directory 
# using os.getcwd()

import os
print(os.getcwd()) 
# to create a new directory
#using os.mkdir()

os.mkdir("testsss") # os.mkdir("directory_name")

# to move to another directory
# using chdir()

os.chdir("testsss")  # os.chdir("directory_name")
print(os.getcwd())

# to remove an empty directory
# using rmdir()
os.rmdir("testsss") # os.rmdir("directory_name")

