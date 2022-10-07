# class Private:

#     def __init__(self,a,b):

#         self._a = a
#         self.b = b
#         print("Private class is created")

#     def _sum(self):
#         return self._a + self.b

# priv = Private(10,20)
# print(priv._sum())
# print(priv._a)

class Private:
    
    def __init__(self,a,b):
        
        self._a = a
        self.b = b
        print("Private class is created")
        
    def _sum(self):
        return self._a + self.b
    
priv = Private(10,20)
print(priv._sum())
print(priv._a)

