# # CONSTRUCTORS 
# class Student:
#     # default constructors
#     def __init__(self):
#        pass

#     # parameterized constructors
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..")

# s1 = Student("Rohit", 99)
# print(s1.name,s1.marks) # rohit

# s2 = Student("sajal", 96)
# print(s2.name, s2.marks)

# Class & Instance Attributes --> data
# Class.attr
# # obj.attr
# class Student:
#     collage_name = "ABC Collage"
#     name = "anonymous"

#     def __init__(self, name, marks):# self --> perameter / new object of a student class
#        self.name = name
#        self.marks = marks
#        print("Adding new student in database..")


# s1 = Student("sajal",95)
# s2 = Student("ankit",89)
# print(s1.name)
# print(s2.name)
# # METHODS --> Methods are functions that blong to object
# const = 540
# const = 1200 # const me value asign ho gyi hai toh 1200 hi rahegi
# final = const + const -- 700 # -- ka matlab hai -(-700) means +700
# # final = const (1200) + const (1200) + 700 
# # final = 1200 + 1200 + 700

# print(final)

# def foo(x):
#     x[0] = ['def']
#     x[1] = ['abc']
#     return id(x)
# y = ['abc', 'def']
# print(id(y) == foo(y))
# class student:
#     name = "sajal"

# s1 = student()
# print(s1)#__main__.student object at  This location -->0x00000175FD147230

# __init__ FUNCTION

# attributes --> data:variable
# class student():
#     collage_name = "ABC collage"
#     name = "anonimus"

#     def __init__(self, name, marks):
#         self.name = name # obj attr = class attr
#         self.marks = marks
#         print("Adding new student in database..")

# s1 = student("sajal",87)
# print(s1.name)
# print(s1.name,s1.marks) # sajal


# s2 = student("sanskar",45)
# print(s2.name,s2.marks)

# print(s2.collage_name)


# METHODS -->Method are function that belong to object

# class student:
#     collage_name = "ABC collage"

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = student("sajal",96)
# s1.welcome()
# print(s1.get_marks())

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi",self.name,"your avg score is:",sum/3)
        
# s1 = Student("tony stark",[99,98,97])
# s1.get_avg()

# Static Methods --> Method that don't use the self perameter (work at class level)
#  decorator --> @staticmethod
# class Student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks
    
#     @staticmethod
#     def hello():
#         print("Hello sir ")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hii ",self.name, "your avg score is: ",sum/3)
    
# s1 = Student("Tony stark",[99,98,87])
# s1.get_avg()
# s1.hello()

# Important 
# OOPS:-

# Abstration--> Hiding the implementation details of a class and only showing the essential feature to the user.

# Encapsulation --> Wrapping data and function into a single unit (object).

#  Inheritance --> When one class(child/drived) derives the properties & methods of another class(parent/base).
# class Car:
# ......start ,stop, color, methode use in a car 

# class ToyotaCar(Car):

# .....



# Polymorphism -->when the same operator is allowed to have diffrent meaning according to the context.
# operator & dunder function 
 

# Abstraction example:-

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started...")

# car1 = car()
# car1.start()


# Encapsulation example:-
# prectice -> Create account class with 2 attributes-blance &
# account no. create methods for debit,credit & printing the blance 

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
    
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount, " Was debited")
#         print("total balance = ", self.get_balance())

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.", amount, " Was credited")
#         print("total balance = ", self.get_balance())


#     def get_balance(self):
#         return self.balance
    

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(10000)


# del keyword --> Use to delete object properties or object itself.
# del s1.name -> isme attributes ko delete karte hai 
# del s1 -> isme hum complate object ko delete kar sakte hai

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("sajal")
# print(s1.name)
# del s1.name 
# print(s1.name)

# Private keyword(like) attributes & methods
# compceptual implimentation in python ->private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)


# acc1 = Account("12345", "abcd")

# print(acc1.acc_no)
# print(acc1.reset_pass)# __acc_pass is a private 



# class Person:
#     __name = "dvdfrijo"


#     def __hello(self):
#         print("Hello person")
    
#     def welcome(self):
#         self.__hello()
# p1 = Person()

# print(p1.welcome())

# Inheritance example:-

# class Car:


#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())

# Type of Inheritance
#  Single Inheritance 
#  Multilevel Inheritance
#  Multiple Inheritance


# Single Inheritance:-


# class Car:


#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())


# Multilevel Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.name = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type


# car1 = Fortuner("Desel")
# car1.start()

# Multiple Inheritance

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "wlcome to class B"

# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# Super Methode-->Super() method is use to access method of the parent class

# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name,type):
#         self.name = name
#         super().__init__(type)

# car1 = ToyotaCar("Prius","electric")
# print(car1.type)



# Class method--> A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & genrally for utility.


# class Person:
#     name =  "anonymous"

#     def changeNmae(self, name):
#         self.name = name

# p1 = Person()
# p1.changeNmae("Rahul kumar")
# print(p1.name)
# print(Person.name)

# Instance methods
# class Person:
#     name =  "anonymous"

#     # def changeNmae(self, name):
#     #     self.__class__.name = "rahul"

#     @staticmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changeNmae("Rahul kumar")
# print(p1.name)
# print(Person.name)

#  Property--> We use @decorator on any method in the class to use the method as a property.

# class Student:
#     def __init__(self, phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
       

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3)+"%"
    
# stu1 = Student(98,54,99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)

# Decorators--> multiple, property,static,class mathode,getter ,setter.

# getter and setter


# print(12+34)
# print("aapna"+" collage")#concatenate
# print([1,2,3,4] + [4,5,6]) # marge

# print(type([1,2,3]))

class Complax:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i", self.img, "j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complax(newreal, newimg)

# Creating objects
num1 = Complax(1, 3)
num1.showNumber()

num2 = Complax(4, 6)
num2.showNumber()

# Adding objects
num3 = num1 + num2
num3.showNumber()


# class Complax:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i", self.img,"j")
    
#     def __add__(self,num2):
#         newreal= self.real + num2.real
#         newimg = self.img + num2.img
#         return complex(newreal,newimg)
        


# num1 = Complax(1,3)
# num1.showNumber()

# num2 = Complax(4,6)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()
 # use a Dunder Function



# print(1 + 2)#3
# print("apna" + "collage")# concatenate
# print([1,2,3] + [4,5,6])# merge
# print(type([1,2,3]))





# Complex numbers
