# class Kali:

#     def advantage(self):
#         print("More powerful")

#     def disadvantage(self):
#         print("Resource intensive")

# class Parrot:

#     def advantage(self):
#         print("Lighweight")

#     def disadvantage(self):
#         print("Small community")

# kali = Kali()
# parrot = Parrot()

# for object in [kali,parrot]:

#     print(type(object))
#     object.advantage()
#     object.disadvantage()

'''def sum(a,b=0):
    return a+b

print(sum(10))'''

class kali:
    
    def advantage(self):
        print("More powerful")
        
    def disadvantage(self):
        print("Resource intensive")
        
class parrot:
    
    def advantage(self):
        print("Lightweight")
        
    def disadvantage(self):
        print("Small coummunity")
  
  
kali = kali()
parrot = parrot()

for object in [kali,parrot]:
    
    print(type(object))
    object.advantage()
    object.disadvantage()      
        
        