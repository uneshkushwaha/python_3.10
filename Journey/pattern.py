
           #square
# for row in range(1,5):
#     for column in range(1,5):
#         print('*',end=" ")
#         #end is an append for strings and stays on the same line unless'\n' next line is used
#         #end= represents that it should not throw the cursor to the next line after displaying each star.so,all the stars are displayed in the same line.
#         #we can take any variable instead of i,j,rows,column
#     print()# it means nextline
#     #this print()statement doesn't show anything but simply throws cursor to the next line.
    

    #right side traingle
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('* ',end=" ")       
#     print()

#left side traingle
# for i in range(1,5):
#     for j in range(1,5-i):
#         print('* ',end=" ")
#     print()


#Note: to do any pattern break them into decreasing and increasing pattern and then colaborate

     #space right traingle

# for i in range(1,5):
#     for j in range(1,5-i):
#         print(' ',end=" ")
#    #be careful about giving space in end ,in this pattern give space to both end else remove from both ,it can alters pattern
#     for j in range(1,i+1):
#         print('*',end=" ")
            
#     print()

    ##space left traingle

# for i in range(1,5):
#     for j in range(1,1+i):
#         print(' ',end=" ")
   
#     for j in range(5-i):
#         print('*',end=" ")
            
#     print()


# for i in range(1,5):
#     for j in range(1,5-i):
#         print(" ",end=' ')
#     for j in range(1,i+i):
#         print("*",end=' ')
#     print()


           #Hill pattern
# for i in range(1,4):
#     for j in range(1,4-i):
#         print(" ",end=' ')
#         
#     for j in range(1,i+i):
#         if j<=i:
#             k+=1
#         else:
#             k-=1
#         print(k,end=' ')
#     print()

    #Reverse Hill Pattern
# for i in range(1,10):
#     for j in range(1,1+i):
#         print(' ',end='')
#     for j in range(1,10-i):
#         print('*',end=' ')
#     # for j in range(0,5-i):
#     #     print('*',end='')
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(' ',end='')
#     for j in range(i,n-1):
#         print('*',end='')
#     for j in range(i,n):
#             print('*',end='')
    
#     print()
    
    #Diamond Pattern
    
n=5

for i in range(n-1):
    for j in range(i,n):
        print(" ",end='') 

    for j in range(i):
        print("* ",end=' ')

    for j in range(i,n):
       
        print('* ',end='')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for j in range(i,n):
            print('*',end='')
    
    print()
    
    
    
    #heart shaped pattern
    #all alphabets pattern


    