# class Bird:

#     def __init__(self,color,wingspan,residence):

#         #self points to current object
#         #variables used with self are attributes of the object
#         #variables without self are arguments and normal user inputs

#         self.col = color
#         self.wing = wingspan
#         self.residence = residence

# bird = Bird('blue',10,residence='India')
# bird.residence = 'Asia'
# print(bird.residence)

class Bird:
    
    def __init__(self,color,wingspan,residnece):
        
        self.col = color
        self.wingspan = wingspan
        self.residence = residnece
        
bird = Bird('blue',10,'india')
print(bird.residence)