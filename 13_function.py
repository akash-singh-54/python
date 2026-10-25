#####.     Functions in Python
# functions are blocks of code that perform a specific task and can be reused throughout a program. 
# They help in organizing code, improving readability, and reducing redundancy. In Python, functions are defined using the `def` keyword, followed by the function name and parentheses. 


# function :- block of code. it run when we call the function. 

#note :- it increase code reusablity 


# how to create a function 

# def keyoword 

# def functionname():    function define 


#function call:-  function name use 


# types :- 
# 1. simple function 
#2. paraeter and arguments 
#3. return 

# 1. simple function :- in this bracket part will be
# empty 


#wap to display yourname using simple function 

#():- parameter bracket blank :- simple function 

# def display():
#     name = "codedesk"
#     print(name)

# display()
# display()
# display()


#wap to add three number 

# def sum():
#     num1 = 100
#     num2 = 50
#     num3 = 10
#     print(num1 + num2 + num3)  


# sum()     
# sum()


#wap to dispaly three stats name using function 


# def state_name():
#     state = input("enter the state name :- ")
#     print(state)

# state_name()
# state_name()



# parameter and arguments :- 



# def display(num1, num2, num3 , num4):
#     print("sum is ", num1 + num2)
#     print("sub is ", num3 - num4)


# display(10,5,3,2)

# display(7,8,46,32)

# display(5,6,78,39)'

# using parameter and argument get the square and cube . 




# def square_cube(num):
#     print("square is ", num ** 2 , "cube is ", num ** 3  )

# square_cube(11)


# # using user input get the student info lke name , course , city , gender  with function



# # def student_info():
# #     name  = input('enter the name :- ')
# #     course  = input('enter the course :- ')
# #     city  = input('enter the city :- ')
# #     gender  = input('enter the gender :- ')

# #     print(name , course , city , gender)


# # student_info()








# # def display(name , course ):
# #     print( name , course)



# # display("code", "python")



# # table of 7  

# #loop :- data repeat until conditon is false 


# #while loop 

# #for loop 


# #while :- 

# #three condition 


# #start point :-  variable 

# #condiiton (start point to end point )

# #statement 

# #increment / decrement 



# #wap to get the 1 to 10 number 


# # num = 1 

# # while(num <= 10):
# #     print(num)   
# #     num+=1 



# #table of 2 


# # num = 2 

# # while(num <= 20):
# #     print(num)
# #     num+=2



# # table of 3 

# # def table():
# #     num = 3 
# #     while(num <= 30):
# #         print(num)
# #         num+=3

# # table()
# # table()

# #table of 9 using function 





# #return function :-  hold the values 


# # def demo():
# #     name = "codedesk"
# #     return(name)

# # print(demo())


# # global and local variable in function  

# # course = "python"
# # def check():
# #     name = "codedesk"
# #     print(name)
    
    

# # check()
# # print(course)

# #recursion :- function calling itself 


# # def test():
# #     print("codedesk")
# #     test()

# # test()




# def table():
#     num = 9
#     while(num <= 90):
#         print(num)
#         num += 9

# table()


#wap using parameter and argument to print squar and cube of a number

def exp(num):
    square = num**2
    cube = num**3
    print("square of the number is ", square, " and cube of the number is ", cube)

exp(4)
exp(8)

#wap using user input get the sudent info (like name course city gender) by using function


def student():
    name = input("Enter Student name: ")
    course = input("Enter Student course: ")
    city = input("Enter Student city student belongs to: ")
    gender = input("Enter Student gender: ")

    print("Student Name is: ", name, "\nLearnung: ", course, "\nBelongs to: ", city, "\nGender: ", gender)

student()
