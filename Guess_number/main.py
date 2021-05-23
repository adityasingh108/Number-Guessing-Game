"""
Author = aditya
Date = 18-05-2021
purpose : programing solution   
"""



def gusser(): 
    """
    This function return the the number if the number is same or the number is diffrent 
    and same time the function return the no of the guess the number   
     """
    import random
    try:
        a = int(input("Enter the range of number :")) #input the value of range
        b = int(input("Enter the range of number :"))# input the value of range
    except:
        print("Enetr the number only !") #if the value  of a is not integer the the program exit 
        exit()
    try:
        random_number = random.randint(a, b) # if the vaue of a is greater than b te program return with error
    except:
        print("This is Not a valid range")
        exit()
    no_turns = 1 # it start from 1
    print("you have 9 attempt to finish  tha game \n") # print the user guess
    while (no_turns < 9): # run a while loop for the nine time 
        try:
            user_input = int(input("Guess  the number:\n")) #takes the number of guess
        except:
            print("Please enter number only")
            exit()
        if user_input > random_number: 
            print("oho ! Guess the lesser number :\n")
        elif user_input < random_number:
            print("oho ! Guess the heighest number :\n")
        else:
            print(f"congrats ! you Guess the correct number \n ")
            global number # create a global variable  
            number = no_turns # and this variable is acces by  the outside the function 

            break
        # print(f"No of guess yo have to lef is {9 -no_turns}\n")
        no_turns += 1

if __name__ == "__main__":
    while True:
        print("player 1 turn")## olayer 1 play the  game 
        palyer1 = gusser()
        player1_number = number


        print("player 2 turn")# palyer 2 play tha game 
        player2 = gusser()
        player2_number = number

        if int(player1_number) > int(player2_number):
            print("player 2 won the game !")
        elif int(player1_number) < int(player2_number):
            print("player 1 won the game ")
        else:
            print("game draw ") 
        print("Press q to quit Game and c to continue with Game :>")  # stooping the program  fro user input 
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"): 
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue   