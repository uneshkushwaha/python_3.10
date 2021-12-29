import time
time_taken=time.time()
print(time_taken)

for i in range(5):
    print('Do you have gutts in your ball?',time.time())#for every iteration execution time is different
 
time_taken2=time.time()#this is the time taken for execution till this line of code
print('time_taken2=',time_taken2)

print('execution time for for loop=',time_taken2-time_taken)
# #but only for ,for loop we have to subtract (current-previous)
i=0
while(i<5):
    print('yes,I have gutts in my ball')
    i+=1
time_taken3=time.time()
print('time_taken3=',time_taken3)#this is till this line of code

print('execution for while loop=',time_taken3-time_taken2)


#In this way ,we can calculate the execution time for different lines of code and here we can see that the 
#execution time for both for and while loop are almost same


localtime=(time.localtime(time.time()))
print(localtime)
#time.asctime()= gives the time format to the string or tuple
#time.localtime()=it converts into local time and returns as tuple
#time.time() =it counts the number of ticks  



