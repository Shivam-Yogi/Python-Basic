# '''Python for Beginners #10
# String Functions'''

# a='subscribe,bitten|tech'

# b=len(a)
# c=a.upper()

# d=a.lower()

# e=a.swapcase()

# f=a.isalpha()

# g=a.isalnum()

# h=a.isdigit()

# i=a.replace("sub","del")

# j=a.index('ub')

# k=a.rstrip()

# l=a.split('|')

# print("Length of a:",b)

# print("Upper case of a:",c)

# print("Lower case of a:",d)

# print("Reverse case of a:",e)

# print("Only alphabets of a:",f)

# print("Only alphabets + numbers of a:",g)

# print("Only digits of a:",h)

# print("Replace b with d of a:",i)

# print("Replace sub with del of a:",i)

# print("Index of s in a:",j)

# print("Strip in a:",k)

# print("Split a:",l)

a='Subscribe,now'
b=len(a)
c = a.upper()
d = a.lower()
e = a.swapcase()
f = a.isalnum()
g = a.isalpha()
h = a.isdigit()
i = a.replace("b","d")
j = a.index('e')
k = a.rstrip() # to remove spaces
l = a.split(',')
print("Length of a:",b)
print("Uppercase:",c)
print("lowercase:",d)
print("swapecase:",e)
print("check is all are alphabets & numbers or not:",f)
print("check is all are alphabets or not:",g)
print("check is all are digits or not:",h)
print("Replace b with d:",i)
print("Prints the index number:",j)
print("strip:",k)
print("Splits or string array into list",l)



