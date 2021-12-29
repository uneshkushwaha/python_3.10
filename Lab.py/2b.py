a='10,20,30,40'
List_num=a.split(',') #it returns into list form

  #print(List_num)#we can do this because it returns explicitly in list form

sum=0
for num in List_num:    #num is the items in the list 
    sum+=int(num)
print("sum=",sum)    