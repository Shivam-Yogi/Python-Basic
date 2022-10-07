# def func(a,b):
#     div = 0
#     try:
#         #anything which can produce an exception
#         div = a + b
#     except:
#         #handle the exception
#         print("Exception caught")
#     else:
#         #if no exception
#         print("All is well")
#         return div
#     finally:
#         #this runs no matter what
#         print("I always run")
#     return False

# a = int(input("Enter number"))
# b = input("Enter number")
# div = func(a,b)
# print(div)

# try:
#     file = open("D:\\sample.txt",'w') #r
#     print(file.read())
# except FileNotFoundError:
#     print("File not found exception caught")
# except OSError:
#     print('Not authorized')
# except TypeError:
#     pass
# except TimeoutError:
#     pass


def func(a,b):
    div = 0
    try:
        div = a+b
    except:
        print("Exception caught")
    else:
        print("All is well")
        return div
    finally:
        print("I always come")
        return False
        
a = int(input("Enter number"))
b = int(input("Enter number"))
div = func(a,b)
print(div)

try:
    file = open("D:\\sample.txt", 'w')
    print(file.read())
except FileNotFoundError:
    print("File not found exception caught")
except OSError:
    print("Not Authorized")
except TypeError:
    pass
except TimeoutError:
    pass