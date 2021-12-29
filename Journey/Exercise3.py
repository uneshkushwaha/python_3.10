#Guess the number
#9 attempts only
#no.of steps taken to solve
n=67
number_of_guesses=1
print("***you have only 9 attempts***")

while(number_of_guesses<=9):
 guess=int(input("guess the number:"))

 if(guess<67):
    print("less")
 elif(guess>67):
        print("more")
 else: 
    print("you  cracked it")
    print(number_of_guesses,"the number of guesses he took to finish")
    break
 print(9-number_of_guesses," number of guesses left")
 #write the code below the else not according to break
 number_of_guesses =number_of_guesses+1 #updation
if(number_of_guesses>9):
 print("game over") 
