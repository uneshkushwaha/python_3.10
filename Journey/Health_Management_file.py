#Health management system
#def getdate():
    #import datetime
    #return datetime.datetime.now()
    #unesh,suraj,sagun
    #6 files,client name as input
client=input("Enter the name of the client:")

if client=="Unesh":
        f=open("C:\python3,10\Doc\Unesh_Ex.txt")
        print( f.read)
     

elif client=="Suraj":
        f=open("suraj_Ex.txt")
        f=open("suraj_diet.txt")
        
        print( f.read)
      
        
elif client=="Sagun":
        f=open("sagun_Ex.txt")
        f=open("sagun_diet.txt")
        
        print( f.read)
       