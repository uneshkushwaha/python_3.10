#Dictionary stores data in key:value pairs in curly braces
#it is ordered ,changeable,doesnot allow duplicates
cars={"brand":"ford","model":"mustang","year":"1964"}
print(cars)


#duplicates values overide the existing values
cars={"brand":"ford","model":"mustang","year":"1964","year":"2015"}
print(cars)

print(len(cars))#length

#data types
cars={"brand":"ford","model":"mustang","year":"1964","year":"2015","electric": False,

"colors": ["red", "white", "blue"]
#either list or set or tuples any datatypes are allowed
}
print(cars)

#Accesing dictionary items
print(cars["brand"])

print(cars.get("brand"))

#keys()methods will return all  a list of the keys in the dicitiionary
print(cars.keys())
cars["engine"]="average"

print(cars.keys())#dictionary keys get updated

#values()methods will return all  a list of the values in the dicitiionary
print(cars.values())
cars["engine"]="excellent"
print(cars.values())#values keys get updated

#checks if keys exists
if "model" in cars:
 print("yes,there is  such keys")

cars.update({"year":2021})#update()
print(cars)

cars.pop("electric")#it delete the specified item

cars.popitem()#it delete the last inserted item
print(cars)
 
 #looping
 #by default it returns keys only
for x in cars:
  print(x)
#but we can returns values also
for x in cars:
      print(cars[x])
#or we can also do this way
for x in cars.values():
      print(x)

#we can return both keys and values
for x,y in cars.items():
      print(x,y)

   #copy dictionary
mycollection=cars.copy()
print(mycollection)

#or we can apply the built in function dict()

mycollection= dict(cars)
print(mycollection)

#python nested dictionaries
wild_animals={
"lion":"king",
"tiger":"president",
"elephant":"treasurer"
}

pet_animals={
"dog":"loyal", 
"cat":"cute", 
"rabbit":"adorable" 
}
insects={
    "mosquito":"typhoid",
    "cockroach":"in corner",
    "dragonfly":"funny"
}

Animals={
"wild_animals":wild_animals,
"pet_animals":pet_animals,
"insects":insects
}

print(Animals)
print(dict.fromkeys(insects))#!!!