# #map
# def cube(num):
#     return num**3

# print(list(map(cube,[1,2,3,4,5])))
# list1 = ['1','2','3','4','5']
# for i in map(int,list1):
#     print(i)
    
# #filter
# def even(num):
#     return num%2==0

# list2= [1,2,3,4,5,6]
# print(list(filter(even,list2)))



# def cube(num):
#     return num**3

# print(list(map(cube,[1,2,3,4,5])))

# list1 = ['1','2','3','4','5']
# for i in map(int,list1):
#     print(i)

# def even(num):
#     return num%2==0

# list2 = [1,3,2,4,5,6,7]
# print(list(filter(even,list2)))

# x = lambda a,b : a+b

# print(x(10,20))

# list2 = [1,2,3,4,5,6,7,8,9,10]

# print(list(map(lambda x:x**3,list2)))
# print(list(filter(lambda x:x%2==0,range(10))))






x=100

def sample(x):
    x = 50
    # print(x)
    
    def cube(x):
        print(x**3)
        
    cube(x)
        
    
sample(x)
print(x)