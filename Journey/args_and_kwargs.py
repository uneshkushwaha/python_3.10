#*args and **kwargs
#args is a non keyword arguments with variable length arguments and returns tuple
#**kwrgs is a  keyword arguments with variable length arguments and returns dictionaries

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# def voters(a,b,c):
#     print(a,b,c)
# voters('Narayan','Gopal','Mohan')
# # it runs 
# def voters(a,b,c):
#     print(a,b,c)
# voters('Narayan','Gopal','Mohan',7)
#we have to pass equals no.of arguments ,if we add like '7' it will give error


#so to overcome this problem ,we pass equal argumensts 'd' as well 
#but its not good way for adding large number of data in applications
#we have to give equal no.of arguments for each data in function or methods
# so to overcome this problem ,this args and kwargs are used


#no need to write only args or kwargs ,we can give any variable name but be careful about asterisk


# def prime_ministers(*candidates):
#     print(candidates)
# candidates=['kpoli','modi','putin','obama','imran khan','Bden',100,5.6]
# prime_ministers(*candidates)
# #here we can add as many data we want
# #by default it will give tuple no matter in which data type it is
# #asterisk must be on both function or method

# #we can also call  the normal function or variable like  "person"


# def prime_ministers(person,country,*candidates,**animals):
# #def prime_ministers(*candidates,person):#this is not acceptable,normal data must be before *args
#    print(type(candidates))
#    print(person)
  
#    for items in candidates: 
#     print(items)#always print the word which is after for (not print(candidates))
   
#    for names in country:
#     print(names)
#    print()
#    for key,value in animals.items():
#      print(f'\n {value} is the name of the baby {key}')
#   #Driver code 
# country=['Nepal','India','Spain','America','Pakistan','USA','Japan','Italy','Taliban']
# person=' These are the prime minister of different country'
# candidates=['kpoli','modi','putin','obama','imran khan','Bden',100,5.6,99,'kim jong-un']
# animals={'Dog':'puppy','Cat':'kitten','Rabbit':'kits','Cow':'calf','lion':'cubs'}
# prime_ministers(person,country,*candidates,**animals)



#enumerate function
#basically ,it reduces the some lines of code
#it returns object as tuple along with index


Browsers=['Chrome','Brave','Microsoft Edge','Mozilla Firefox','Internet Explorer']

#suppose someone told to remove brave and Mozilla firefox from my list

i=0
for items in Browsers:
 if  i%2==0:
  print(items)
 i+=1


 #so ,by the help of enumerate function we can reduce some lines of code
 Browsers=['Chrome','Brave','Microsoft Edge','Mozilla Firefox','Internet Explorer']

for index,items in enumerate(Browsers):
     if  i%2==0:
      print(items)
     
