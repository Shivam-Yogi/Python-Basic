# #simple function
# def func():
#     print('hello')
# #func()

# #with arguments
# def func1(name):
#     print("Hello "+name)
# #func1('Ansh')

# #with default arguments
# def func2(name='Default'):
#     print("Hello "+name)
# #func2()

# #with default arguments
# def func3(a,b,c=5):
#     print(a+b+c)
# #func3(3,4)

# #return values
# def func4(a,b,c=5):
#     return a+b+c
# #result=func3(3,4)

# #example: checking if a number is prime
# def check_prime(num):
#     flag=0
#     for i in range(2,num):
#         if(num%i==0):
#             flag=1
#             break
#     return flag==0

# result=check_prime(int(input("Enter number")))
# print(result)



def function():
    print("Hello")
    
function()

def func(name='Default'):
    print("Hello"+name)
func()

def func1(name):
    print('Hello'+name)
func1("Ansh")

def func2(a,b,c=5):
    print(a+b+c)
func2(3,5)

def func3(a,b,c=5):
    return a+b+c

result=func3(3,5)

def prime_num(num):
    flag=0
    for i in range(2, num):
        if(num%i==0):
            flag=1
            break
    if(flag==0):
        return True
    else:
        return False

    
result = prime_num(int(input("Enter number")))
print(result)