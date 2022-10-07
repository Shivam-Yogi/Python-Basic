# #Access modes
# #r
# #w
# #r+
# #w+
# #a
# #a+

# #read a file
# file = open('D:\\test.txt',mode='r')
# print(file.read())
# file.seek(0)
# print(file.readlines())
# file.close()

# #write to a file
# file = open('D:\\test.txt',mode='w')
# file.write('Hello World\nBitten Tech\nTechHacker')
# file.close()

# #read a file
# file = open('D:\\test.txt',mode='r')
# print(file.read())
# file.close()

# #append to a file
# with open('D:\\test.txt',mode='a') as file:
#     file.write('Hello World\nBitten Tech\nTechHacker')

# file = open('D:\\test.txt',mode='r')
# print(file.read())



file = open('D:\\test.txt',mode='r')
print(file.read())
file.seek(0)
print(file.readlines())
file.close()

file = open("D:\\test.txt",mode='w')
print(file.write("Bittentech\nIs a good teacher\nbut boring too"))
file.close()

with open('D:\\test.txt',mode='a') as file:
    file.write("HelloWorld\nBittentech\nTechHacker")
    
file = open("D:\\test.txt",mode='r')
print(file.read())
