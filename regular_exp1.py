# using re module and regular expressions in python
import re
result = re.search(r"aza","plaza")
print(result)

print(re.search(r"l.arn","learn")) # . wildcard 

print(re.search(r"l.arn","LEARN")) # case sensitive

print(re.search(r"l.arn","LEARN",re.IGNORECASE)) # to be case insensitive

print(re.search(r"^a","aaa"))

print(re.search(r"^a","bbb"))

print(re.search(r"n$", "earn"))

