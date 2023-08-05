# class computer:
    
#     #init mehtod will get call automatically FOR EVERY OBJECT IT WILL GET CALLED ONCE
#     #assigning cpu and ram to the object  

#     def __init__(self,cpu,ram): 
#         self.cpu = cpu
#         self.ram = ram
#         print("in int")

#     def config(self):
#         print(self.cpu , self.ram)


# com1=computer('i7 12 gen' , 32)
# com2=computer('ryzen' ,16)

# print(type(com1))

# 2 mehtods to call object

# computer.config()

# com1.config() # in this behimd the scene config takes com1 as the parameter and will pass it in himself
# com2.config()

#------------------------------------------------------------------------------

# Constructors

# class computer:
#     def __init__(self) -> None:
#         self.name="vipul"
#         self.age=28

#     def update(self) -> None:    # self is a pointer
#         self.age=30
        

# c1=computer() #computer() is the default constructor and it is called internallly
# c2=computer() 

# c1.name="dhir"
# c1.age= 20

# c1.update()


# print("address location of an object in heap memory",id(c1))
# print(c1.name)
# print(c2.name)

#------------------------------------------------------------------------------

# INSTANCE VARIABLES

# class car:
     
#     wheels=4  #class variables vlues can be changed using cars.wheels=5

#     def __init__(self) -> None:     # mil and com are instance variables , instance variables are different for different variables. 
#                                     #there values can be changed
#         self.mil=15
#         self.com="BMW"

# c1 = car()
# c2 = car()

# c1.com ="honda"
# car.wheels=5

# print(c1.com , c1.mil , c1.wheels)
# print(c2.com , c2.mil , c2.wheels)

#-----------------------------------------------------------------------

# MEHTODS

# class student:

#     school ="xaviers"

#     def __init__(self, m1 ,m2 ,m3) -> None:
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg (self): #instance mehtod because it works with objects self is passed
#         return (self.m1 + self.m2 + self.m3)/3
    
#     @classmethod   #decoders used to declare class mehtods
#     def info(cls):
#         return cls.school
    
#     #static mehtods which have nothing to do with instance or class variables
#     @staticmethod
#     def stat_mehtod(): #keep brackets blank 
#         print("this is a static mehtod because it has nothing to do with class or instance var")


# s1=student(20,34,56)
# s2=student(56,32,12)

# print(s1.avg())
# print(s1.m1 ,s1.m2 ,s1.m3)
# print(student.info())

# student.stat_mehtod()

#----------------------------------------------------------------------------

# INHERITANCE - child class extracting features from parent class 
                # multiple inheritance also possible

# class A: #super class / parent class
#     def feature1(self):
#         print("this feature 1 is working")
#     def feature2(self):
#         print("this feature 2 is working")


# class B: #sub class / child class
#     def feature3(self):
#         print("this feature 3 is working")
#     def feature4(self):
#         print("this feature 4 is working")

# # multiple inheritance
# class C(A,B): #sub class / child class 
#     def feature5(self):
#         print("this feature 5 is working")
#     def feature6(self):
#         print("this feature 6 is working")


# a1=A()
# a1.feature1()
# a1.feature2()


# c1=C()
# c1.feature1

# CONSTRUCTOR IN INHERITANCE

class A:

    def __init__(self) -> None:
        print("constructor called in A")
        

    def feature1(self):
        print("this feature 1 is working")
    def feature2(self):
        print("this feature 2 is working")


class B(A): 

    def __init__(self) -> None:
        print("constructor called in b")

    def feature3(self):
        print("this feature 3 is working")
    def feature4(self):
        print("this feature 4 is working")


b1=B() 
# if we have a constructor in  a and not in b and we create an object of b 
# and call it it will call the constructor of a but if both 
# classes have a constructor then object of b will call only the constructor of a 
# but if we want to call both the constructors we will use super() keyword