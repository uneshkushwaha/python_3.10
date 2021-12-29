# #set is one of the data types in python which stores multiple items in single variable
# #It is a collection which is 
# #unordered
# #unchangable
# #unindexed and donot allow duplicates
# #written in curly braces

#                      #unordered
# city={"kathmandu","delhi","dhaka","washington DC"}
# print(city)
#               #constructor
# city=set(("kathmandu","delhi","dhaka","washington DC"))
# print(city)

# #we cannot access item by index but we can ask that it is present or not by'in'keyword
# print("kathmandu"in city)
# print("lahore"in city)

# #unchangable but items can be added
# city.add("paris")
# print(city)
# flowers={"rose","marigold","orchid","sunflower"}
# #we can add items from one set to another set by update method
# city.update(flowers)
# #we can update set as well as tuple,dicitionary,lists
# #we can also use union() ,it creates new set whereas update()inserts items
# print(city)

# city.pop()
# city.discard("kathmandu")

# # city.clear()
# # del city
#             #for loop
# print(city)
# for x in city:
#     print(x)

company={"google","microsoft","apple"}
college={"Cambridge","Harvard","Austrin","google"}
y=company.intersection(college)
#this method returns a new set and only contains common items
print(y)
company.intersection_update(college)
print(company)

company.symmetric_difference_update(college)
print(company)

x=company.symmetric_difference(college)
#it will create a new set with non common items!!!
print(x)

