# var1=5
# var2=65  
# var3=int(input())
# if var3>var2:
#    print("greater")
# #if var3==var2:
# #if we use 'if' here then even it is correct in first condition 
# #it will check the all other  conditions and print else part also ...not for its neearest 'if'
# #so 'elif'is used which directly comes out of the else-if loop when any condition get matched
# elif var3==var2:
#    print("equal")
# else:
#     print("lesser")


#eg:2 
# tablets=["paracetamol","relief","flexon","dolopar"]
# print("flexon" in tablets)
# if "flexn" in tablets:
#       print("yes,present")
# else:
#       print("No,not present")


# #eg:3
# animals=("lion","tiger","leopard","elephant")
# if "lion" in animals:
#       print("yes,present")
# else:
#       print("No,not present")


#    #eg:4
# cars={"brand":"ford","model":"mustang","year":"1964"}
# if "lion" in cars:
#       print("yes,present")
# else:
#       print("No,not present")


#  #eg:5
# city={"kathmandu","delhi","dhaka","washington DC"}
# if "delhi" in city:
#       print("yes,present")
# else:
#       print("No,not present")


      #if else have only one statement
a=100
b=200
#we can write in single line.This technique is called coditional expressions
print("sum") if a>b else print("difference")

#AND
#it is a keyword used to combine conditional statements where both are true
a=45
b=65
c=32
if a<b and c<b:
      print("both the conditions are true")


#OR
#it is a keyword used to combine conditional statements where at least one is  true
a=45
b=65
c=325
if a<b or c<b:
      print("only first conditions is true")
