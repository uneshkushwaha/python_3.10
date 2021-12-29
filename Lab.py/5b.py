str1="SVEC"
str2="ACSDIKSESKVFIVSEKCDJFSC"
x=[]
for ch1 in str1:
    i=0
    for ch2 in str2:
        if(ch1==ch2):
            i+=1
    x.append(i)
print("The string1 is:",str1)
print("The string2 is:",str2)
print("The string1 is:",str1,'can be formed',min(x),'times from string2')