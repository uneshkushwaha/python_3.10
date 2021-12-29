#printing star

row=int(input("how many row you want to print:"))
new=int(input("Enter 1 or 0:"))
bool_var=bool(new)
if (bool_var==1):
 for i in range(1,row):
    for j in range(1,i+1):
        print("*")
      
if (bool_var==0): 
 for i in range(row,0,-1):
  for j in range(1,i+1):
        print("*")   
 