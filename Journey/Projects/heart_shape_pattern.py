for i in range(6):
      #take as much row and column you want ,draw it into that row  and column in graph
 for j in range(7):
   if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
         #relate row and column where you want to print star
    print('*',end="")
   else:
    print(' ', end='')
    #print space where no relation exists in row and column
 print()