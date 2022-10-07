# #Positional arguments
# def func(*args):
#     print(args)
# #func(10,20)

# #sum of n numbers
# def sum(*args):
#     sum=0
#     for arg in args:
#         sum+=arg
#     print(sum)
# #sum(10,20,30,40)
# #sum(10,20,30,40,50,60)

# #Keyword arguments
# def func1(**kwargs):
#     print("I like",kwargs['food'])
# #func(food='apple', vegetable='onion')

# #Positional arguments with keyword arguments
# def func2(*args,**kwargs):
#     print(args)
#     print(kwargs)

# func2(10,20,30,food='apple',vegetable='onion')

def func(*args):
    print(args)
func(10,20)

def sum(*args):
    sum=0
    for arg in args:
        sum += arg
        print(sum)
sum(10,20,30,40,50)

def func1(**kwargs):
    print("I like",kwargs['food'])
func1(food='apple',vegetable='onion')

def func2(*args,**kwargs):
    print(args)
    print(kwargs)
    
func2(10,20,30,40,food='apple',vegetable='ladyfinger')