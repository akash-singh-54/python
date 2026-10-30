# assignment 

# 1. Write a program to get the square and cube using the constructor

class sq:
    def __init__(self,num):
        print("Square is:", num**2,"\nCube is:", num**3)

object = sq(6)
print("\n")

# 2. Write a program to get a table of 6 in reverse order using a constructor 


class table:
    def __init__(self,num):
        for i in range(10,0,-1):
            print(num,"*",i,"=",num*i)

object = table(6)
print("\n")



# inheritance assignment 

# 1. Write a program to create a four-class and perform logical operators 

class logic_and():
    def AND(self,x,y):
        print("x>y and x!=y",x>y and x!=y)

class logic_or():
    def OR(self,x,y):
        print("x<y or x==y",x<y or x==y)

class logic_not():
    def NOT(self,x,y):
        print("not(x<y and x!=y)",not(x<y and x!=y))

object = logic_and()
object.AND(6,8)
object = logic_or()
object.OR(54,345)
object = logic_not()
object.NOT(637,87)

print("\n")


# 2. Write a program to perform logical operators using inheritance 

class logic():
    def AND(self,x,y):
        print("x>y and x!=y",x>y and x!=y)

class logic2(logic):
    def OR(self,x,y):
        print("x<y or x==y",x<y or x==y)

class logic3(logic2):
    def NOT(self,x,y):
        print("not(x<y and x!=y)",not(x<y and x!=y))

object = logic3()
object.AND(6,8)
object.NOT(637,87)
object.OR(54,345)
print("\n")