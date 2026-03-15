# #number guessing 

import random

def guess_num():
    computer= random.randint(0, 100)

    attempts = 0

    while True:
        guess = int(input("Enter your guess (0-100):")) 
        attempts =+1       
         
        if guess < computer:
            print("It's Low!! Try again.")
        elif guess > computer:
            print("It's High!! Try again.")

        else:
            print(f"Correct! You guessed the number:{guess}.")
            break
    
    current_atmp=attempts

    with open("pro2_data.txt","r") as f:

        low_atmp=f.readline()
        high_atmp=f.readline()

        if(low_atmp!="" and high_atmp!=""):
            low_atmp=int(low_atmp.split(":")[1])
            high_atmp=int(high_atmp.split(":")[1])

        else:
            low_atmp=current_atmp
            high_atmp=current_atmp

        if(low_atmp > current_atmp):
            low_atmp = current_atmp

        if(high_atmp < current_atmp):
            high_atmp = current_atmp
        
        with open("pro2_data.txt","w") as f:
            f.write("Lowest attempts:" + str(low_atmp) + "\n")
            f.write("Highest attempts:" + str(high_atmp))

        print("Lowest Attempts:", low_atmp)
        print("Highest Attempts:", high_atmp)
        
guess_num()



#-------------Work Flow----------------
'''
1. Player plays Guess the Number
2. Program counts attempts
3. File containing previous stats is opened
4. Program reads highest and lowest attempts
5. Current attempts are compared with both values
6. If attempts greater than highest → update highest
7. If attempts lower than lowest → update lowest
8. File is updated with new values'''