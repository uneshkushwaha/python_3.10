def my_function(tup1):
    for i in range(0,len(tup1)-1):
        next=-1
        if(tup1[i]>tup1[i+1]):
            next=tup1[i+1]
        print(next)
    print(-1)
#driver code
tup1=(4,2,1,5,3)
my_function(tup1)