# Constructor: It is a special function that is automatically called when an object of a class is created, and there is no need to call the constructor.
# syntax:- 


# def __init__(self): 
#      #code 

# example:-  

# class A:
#      def __init__(self):
#          a="codedesk"
#          print(a)

# object=A()


# #types of constructors:-  


# 1. default(simple) constructer 
# 2. Parameterized constructor 


# 1. Default: It is also called the empty constructor because it does not have any parameters. 

# ex:-       class A:
#              a=10
#                  def __init__(self):
#                       print(self.a)

# object=A()


# 2. Parameterized constructor:- In this constructor, we assign a parameter. 

# example:-     class A:
#                   def __init__(self,name,age):
#                       print(name,age)

#               object=A("codedesk",15)



# ex:-2 

# class Check():
    
#     def __init__(self,name,course):
#         print(name,course)
        

# obj=Check("codedesk",None)



# assignment 

# 1. Write a program to get the square and cube using the constructor 

# 2. Write a program to get a table of 6 in reverse order using a constructor 






# Inheritance: It is used to provide primary class access to the child class. 


# syntex:-         
#              class PRIMARY:
#                    #code


#              class CHILD(PRIMARY):
#                    #CODE 

#             object=child()
#             object.function name 



# Types of inheritance:-   

# 1. Multilevel inheritance 

# 2. Multiple inheritance 



# 1. Multilevel: in this, get access from parent to child and child to grandson 


# example:-         

#               class CHECK:
#                     def sum(self,a,b):
#                         print(a+b)


#               class CHECK1(CHECK):
#                     def subs(self,a,b):
#                         print(a-b)

#               class CHECK3(CHECK1):
#                     def multi(self,a,b):
#                         print(a*b)

#               object=CHECK3()
#               object.sum(10,20)
#               object.subs(20,10)
#               object.multi(10,10)


# example :- with constructor:- 


# class top1():
#    def __init__(self,x,y):
#        print(x+y)

# class top2(top1):
#     def __init__(self,x,y,p,q):
#         super().__init__(x,y)
#         print(p-q)

# class top3(top2):
#     def __init__(self,x,y,p,q,a,b):
#         super().__init__(x,y,p,q)
#         print(a*b)



# object = top3(10,9,8,7,6,5)

         

# 2. multiple inheritance :-  in this get the access 
# of parent and child class into grandson class 




#                   class CHECK:
#                     def sum(self,a,b):
#                         print(a+b)


#                  class CHECK1():
#                     def subs(self,a,b):
#                         print(a-b)

#                  class CHECK3(CHECK,CHECK1):
#                     def multi(self,a,b):
#                         print(a*b)

#               object=CHECK3()
#               object.sum(10,20)
#               object.subs(20,10)
#               object.multi(10,10)





# assignment 

# 1. Write a program to create a four-class and perform logical operators 

# 2. Write a program to perform logical operators using inheritance 









# Encapsulation: It is a process that restricts variables and methods globally by using public, private, and protected access modifiers. 


# access modifier:-  

# public  (only variable name)  #access everywhere(same class, other class, inheritace, function)

# protected (_)   #access on same class, function, inheritance

# private(__) #only access same class

# a=10   #public 

# _a=50   # protected

# __a=60   #private 


# example:-1  


# class A:
#     a=5
#     _b=10 
#     __c=20
#    print(a,_b,__c)

# object=A()   #5,10,20


# exapmle:- 2. 

# class A:
#     a=5
#     _b=10 
#     __c=20


# obj=A() 
# print(obj.a)   #5
# print(obj._b)   #10
# #print(obj.__c)   #error  




# example 3:- 

# class A:
#     a=5
#     _b=10 
#     __c=20

#      def display(self):
#       print(sefl.a, self._b, self.__c)


# obj=A()   #5,10,20



# example4:- 

# class A:
#     a=5
#     _b=10 
#     __c=20

#      def display(self):
#       print(sefl.a, self._b, self.__c)


# class B(A):
#      def demo(self):
#        print(self.a, self_b)   #self.__c (this is private)


     
 
# object=B()
# object.display()  
# object.demo()   #5,10, #private cant acces here 





# assignment 

# * Check employee name, post, and salary.  give private to the salary and public to the name, and protected to the post 




# * Polymorphism: same name but different behaviour : 

 
# class A: 
#      def display(self, name=""):
#       print(name)

#      def display (self, course="", address=""):
#          print(name)

#      def dispaly(self, contact="", dob="",gender=""):
#           print(place, course) 

# object=A()
# object.display("codedesk")   #codedesk
# object.display("python","jaipur")  #python, jaipur
# object.display("9649879", "10-5-1998","male")  #9649879, 10-5-1998,male



# assignment 

# 1. Write a program to use the function name user  and get some info about the user by overriding