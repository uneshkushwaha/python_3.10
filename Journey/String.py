"""str1="hello sanorita"
print(str1)

str2='Have a great day'
print(str2)

str3=input("Enter the first name:")
str4=input("Enter the last name:")

print("Enter the Full name:",str3,str4)"""

"""
He is the
 best
 player 
 in the world
 This is the comment syntax for multiple lines 
"""
"""
***to check String whether certain phrase is present or not
print("kushwaha"in str4)
if"last" not in str1:
    print(" yes,'last'  in str1")

"""
#methods of string
'''
mystr="moneyHeisthashehighestimbdrating75"
print(mystr)


print(len(mystr))

del mystring[1]#string doesnt support item deletion

mystring[3]="a"#stirng are immutable i.e not changable


print(mystr.capitalize())
#it capitalize the first letter!!!

print(mystr.endswith("rating"))
#it checks whether it is ending with the given key or not

print(mystr.count("h"))
#it counts the number of times it appears

print(mystr.replace("imbd","views"))
#string cant be changed but replaced
print(mystr.format("he",'she'))

print(mystr.index("imbd"))
#it represents the index of the string
# it doesnt represent string of the index 

print(mystr.index("i"))
#it always represents the first occurence of the string unless it is parameterized
print(mystr.index("i",18,25))
#first occurence and returns exception while not found
print(mystr.isalnum())
#it checks characters must be either alphabets or numberic
#except that like spaces,!,#,@,% etc returns false and also no parameters
print(mystr.isalpha())
#it checks whether  all the characters are alphabet or not otherwise  returns false even it  is numbers
print(mystr.isdecimal())
#it checks the characters unicode is decimal or not !!!
print(mystr.isdigit())
#it checks the characters unicode is digits or not !!!
print(mystr.join("unesh"))
#unesh is an iterable i.e an object whose each element is used and makes  a single string like in for loop

myDict={"name":"tony starks","profession":"actor","civil war":"infinity war"}
#while using dictionary only key names are used not their values
print(mystr.join(myDict))


print(mystr.expandtabs(5))
#it sets the tabsize by specifying tab spaces i.e \t


#string slicing
#we can return a range of characters using slice syntax
print(mystr[0:4])

#it starts with index with zero 
#even the index[4] will be on 'y'but it shows upto 'e' only bcz 4 is excluded

print(mystr[0:4:2])
# :2 result into the leaving of one character

print(mystr[:])
#by default it will take whole
print(mystr[0:])

#it starts from zero to last character

print(mystr[2:4])

#it starts from two to four index

print(mystr[-1:-5:-2])
#negative slicing starts from last

print(mystr[-5:0:-3])
#starts from -5 with 3 missing
print(mystr[0:84])
#it prints whole and aur kahega bass itna hi lele 
'''


#modify strings
mystr1="By the order of the fucking peaky blinders"
print(mystr1)
print(mystr1.upper())
#convert into capital letters
print(mystr1.lower())
#convert into small letters
print(mystr1.split())
#splits the string
print(mystr1.strip())
#removes the white spaces from the begining and end onlly

#string concatenation(to combine two strings)
a="Tommy"
b="shelby"
c=a+b #combine two string
c=a+"                "+b #to add spaces between strings
print(c)

#format strings
''' as we know we can't add strings and integers but with the help of format it is possible
format method receives the arguments which is passed to the placeholders {}of  the string '''

mystr="Polly Gray is finanical manager of Tommy shelby componay and she is {} years old."
age=45
print(mystr.format(age))

#we can use index also
subject="science={2},math={1},python={0}"
science=45
math=89
python=75
print(subject.format(science,math,python))

#Escape characters in strings
'''Escape  characters are used to insert the characters that are illegal in strings
such as \t,\n,','',\b'''
name="covid 19\\n is the worst thing happen\\t in the world"
#here we can see \t,\n are not printed their meanings executes
#so uses backslace(\)to print these all
print(name)

                      




