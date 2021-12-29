
#python lists and 
''' List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.

Dictionary is a collection which is ordered* and changeable. No duplicate members.
'''


#list functions
'''
mylist=["Mohan babu","Vishnu","laxmi","Kushwaha","male and female","laxmi"]
print(mylist)

mylist.append("Unesh")
#it adds elments to the last str,int,bool whatever
#we cannot add it into print ,need to write separetly

print(mylist)





mylist.remove("Vishnu")#removes the specified element or value
print(mylist)

print(mylist.pop(5))# it removes the elements with specified position on basis of index
#it returns the remove value

mylist.extend("manchu")#adds elements in the interable form
print(mylist)

mylist.insert(5,"Banana")
print(mylist)
#insert the elements in the specific position

mylist.reverse()
print(mylist)

mylist.sort(reverse=True)
#by default false i.e ascending
#sorting is error between int and str
#first sort by uppercase and then lowercase
print(mylist)
#it can also by length ,year or whatever criteria it has given
#key function to specify certain criteria

mylist.clear()#removes all the items
print(mylist)

print(len(mylist))#length of the list'''

       