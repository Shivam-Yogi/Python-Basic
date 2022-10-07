# #range
# for i in range(100,50,-2):
#     #print(i)
#     pass
# result=list(range(0,10))
# print(result)

# #enumerate
# string = 'subscribe'
# count=0
# for j,i in enumerate(string):
#     print (j,i)

# #zip
# list1 = [1,2,3,4,5,11,12,13]
# list2 = [6,7,8,9,10]

# for j,i in zip(list1, list2):
#     print(j,i)

# #in
# print(10 in {'key':10})

# #max, min
# list1=list(range(10))
# print(min(list1))
# print(max(list1))

# #random, shuffle, randint
# from random import random
# list1=[1,2,3,4,5]
# num = random()
# num = randint(0,100)
# shuffle(list1)
# print(num)

# #type function
# a = (1,2,3)
# print(type(a))


import random
num = random.randrange(0,91,5)
print(num)

for i in range(100,50,-2):
    print(i)
    pass
result=list(range(0,10))
print(result)

string = 'HelloColz'
count=0
for j,i in enumerate (string):
    print(j,i)
    
list1 = [25,26,48,25,4,1,12]
list2 = [54,64,65,77]

for i,j in zip(list1,list2):
    print(i,j)
    
print(10 in {'key':10})

list1=list(range(10))
print(min(list1))
print(max(list1))

list3 = [1,2,3,4,5,6,7]
# num = random()
num = random.randint(0,100)
print(num)
random.shuffle(list3)
print(list3)

print(type(list3))
