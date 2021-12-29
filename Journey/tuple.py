#   #tuples

# #tuples  uses small brackets
# #ordered i.e defined order which will not change
# #unchangable i.e can't remove or add items once tupled is created
# #allow duplicates
# thistuple =("bitcoin","pi","BAT","UpcoinDx")
# print(thistuple)

# #accesing of the elements
# print(thistuple[2])

# #range of indexes
# print(thistuple[2:5])
# print(thistuple[-3:-2])
# print(thistuple[-1:-3])

# #updating of tuples 
# #since we can't add or remove in tuple so we convert tuple into lists 
# #and make change their and again convert into tuple

# x=list(thistuple)
# x.append("Ethereum")
# print (tuple(x))

# #adding of tuple to tuple 
# y=("Litecoin",)
# x+=y
# x.remove("BAT")
# print(tuple(x))


# #deletion of tuple using "del" keyword
# del thistuple

# #show error i.e" this tuple is not defined" bcz the tuple is deleted


# #packing and unpacking of tuple
# #creating a tuple is packing bcz values are assigned
# #when values are assigned back to variable is unpacking
# fruits=("apple","banana","cherry","strawberry","rasphberry")
# print(fruits)

# #unpacking
# (green,yellow,*red)=fruits
# print(green)
# print(yellow)
# #we use asterisk when vairable is less than values where excess values are assigned to tha variable
# #in the form of list
# print(red)

# fruits=("apple","banana","mango","papaya","cherry")
# print(fruits)

# (green,*yellow,red)=fruits
# print(green)
# print(yellow)
# #it means that when put asterisk in the except last variable ,it will assign all value 
# #which associates with its characters
# print(red)
#               #Loop Tuples
# fruits=("apple","banana","cherry","strawberry","rasphberry")
# for x in fruits:
#   print(fruits)
#                  #for loop
#   fruits2=("apple","banana","mango","papaya","cherry")
#   for i in range(len(fruits)):
# #using range()and len()functions to create suitable iterable
#      print(fruits2[i])
        
#        #while loop

animals=("lion","tiger","leopard","elephant")
i=0
while i<len(animals):    
  print(animals[i])     
  i=i+1#not supported in visual code

#      #join tuples by '+' and '*'
# tuple_animals=("cow","tiger","leopard","elephant")
# tuple_country=("Nepal","India","America","South Africa")
# tuple3= tuple_animals+tuple_country
# tuple3= tuple_animals*tuple_country
#                               #tuples methods
# stationary=("pen","pencil","books","copy","register","books")  
# print(stationary.count("books"))  
# print(stationary.index(4))                           
