# reading the contents of a file using readlines()
file = open("spider.txt")
lines = file.readlines()
print(lines)
lines.sort()
print(lines)
file.close()