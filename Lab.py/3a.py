
pr=int(input("Enter the previous reading:"))
cr=int(input("Enter the current reading:"))
cu=pr-cr
print("The consumed unit is:",cu)

if (cu>=0 and cu<=100):
 total_bill=4*cu
elif(cu>=101 and cu<=150):
 total_bill=4.6*cu
elif (cu>=151 and cu<=200):
 total_bill=5.2*cu
elif (cu>=201 and cu<=300):
 total_bill=6.3*cu
elif 300>cu:
 total_bill=8*cu
else:
    print("faulty calculation")

print("The total electricity bill is:",total_bill)