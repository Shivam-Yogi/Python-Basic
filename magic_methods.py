# class Student:

#     def __init__(self,rollno,name):

#         self.rollno = rollno
#         self.name = name

#     def __str__(self):
#         return "Class str is called"

#     def __len__(self):
#         return len(self.name)

#     def __del__(self):
#         print("Student is destroyed")

# student = Student(12,'Atul')
# print(str(student))
# print(len(student))
# del student


class Student:
    
    def __init__(self,rollno,name):
        
        self.rollno = rollno
        self.name = name
    
    def __str__(self):
       return "class str is called"
   
    def __len__(self):
       return len(self.name)
    
    def __del__(self):
        print("Student is destroyed")
        
Student = Student(12,'Shiv')
print(str(Student))
print(len(Student))
del Student