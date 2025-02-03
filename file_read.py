# reading file contents using python
file = open("spider.txt") # opening a file for read operations
print(file.readline()) # reading a single line
print(file.readline())
print(file.read()) # reading the entire content of the file from the current position till end of file
file.close() # closing the file
