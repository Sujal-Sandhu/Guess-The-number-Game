import random

print("-----GUESS THE NUMBER GAME-----")
print()
number=random.randint(1,10)

print("You have to enter a number between 1 to 10")
print()
count=0
game=1
print(f"Starting {game} game")
print()

while (1):
    while(1):
        print()
        try:
            choice=int(input("Enter your choice:"))
            print()
            if choice>10 or choice<1:
                print("Please enter a valid number")
                break
            elif choice != number:
                print("Please enter a number")
                break
            
            if choice==number:
                print("Congratulations You guess it!!!")
                print(f"You took {count+1} attempt to guess it")
                print()
                break

            elif choice>number:
                print("Your number is too high")
                print("Please select lower number")
                count +=1

            elif choice<number:
                print("Your number is too low")
                print("please Select higher number")
                count +=1

            if count==3:
                print()
                print("Sorry Game Over Better Luck next time.")
                print()
                break
        
        except Exception as e:
            print("Please enter a valid number")
            print(e)
            break
            
    print("So the number which is chosen by the computer is:",number)
    print()
    print("Do you want to play more : 0 for Yes and 1 for NO") 
    play=int(input("Please select your choice:"))
    if play==0:
        game+=1
        print()
        print(f"Starting {game} game")
    else:
        break
    
print()    
print("Thank you for Playing my game")
print("Exiting...")