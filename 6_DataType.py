#data types :- use to check the type of data 

#types :- 
# 1.  Immutable data types 
# 2.  mutable data types 

#1. immutable :- cant change or update the vlaues 
#int , flaot , boolean , string , tuple , set 

# 2.  mutable data types :- we can change or update the values 
#list , dictionary 


#immutable :- 

# int :-  number vlaues 
num1 = 100 
# #use 'type' to check the types of data 
print(num1, type(num1))


# #float :- decimal value 
num2 = 10.9
print(num2 , type(num2))


# # boolean :- output in true or false 

num3 = True 
print(num3, type(num3))
num4 = 100 > 50
print(num4, type(num4))


 #string ;- collection of character in single , dobule , triple quote 
str1 = 'codedesk'
st2 = "codedesk"
str3 = '''
  hello
   codedesk
'''
print(str3)
 #use type 
print(type(st2))


# #string indexing :- use to get the single charcters 

str4 = "i am a python developer"

# # # for total length :- start counting from 1 
# # # for total indexing - start counting from 0 

print(str4[0])
print(str4[7])

# # #reverse indexing :- 
print(str4[-1])


# #total length :- use len function 
str4 = "i am a python developer dkljvk lxcnvkld snvkld snvkldsn vlkds nvkldfsn vkldsfn vkldsn kvldsn kvlsdlvk dslvn"
print(len(str4))

# string slicing :- use to get the multiple characters
str5 = "i am a python developer"

print(str5[0:5]) 
print(str5[5:11])  
print(str5[11:]) 
print(str5[:11])
print(str5[0::2])
print(str5[0::5])
print(str5[-1::-1])

