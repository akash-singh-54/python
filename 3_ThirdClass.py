"""

* Python variable: Variables are a collection of values. 

example:-   x=10
            name "akash"

example2:-  
           x="hello"
           x="world"
           print(x)  #world  # It takes the latest value when we use the same variable name. 


* What are the conditions to assign a variable name:- 

1. can't start with a number to assign a variable name. 
ex:-    1a="akash"   #wrong
        a1="akash"   #right 

2. can't use special charachters. 

ex:-   @abc="akash"  #wrong
        abc="akash"  #right 


3. can't take space between two variable names:- 

ex:-  a b=123  #wrong 
      ab=123   #right 

4. among all the special charachters only underscore(_) can be used to assign a variable name. 

ex:-    _a="akash"  #right 
        a_b_c="akash" #right 

5. can't take predefined function name. 
ex:-  print = 123 #wrong



* assign multiple variable names with multiple values in a single line:- 

ex:-   x,y,z=1,2,3
       print(x,y,z)  #1,2,3
       print(z,y,x)  #3,2,1

       x,y,z=1
       print(x,y,z)  #error #unpack we have to give the same number of values as variable names.

      

* multiple variable names with single values. 

ex:-  x=y=z=1
      print(x,y,z)  #1,1,1 it assigns same value to each variable.
   
      x=y=z=1,2
      print(x,y,z)  #(1,2) (1,2)  (1,2)
 

* case sensitive:- letters formatting 

 abc="akash"
 print(ABC)  #error #in python a,A are different charachters

 abc="akash"

 print(abc)  #akash 



* variable casting:-  
  x=10            #integer 
  y=10.5         #float 
  z="akash"   #string
  
"""
