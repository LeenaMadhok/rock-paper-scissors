import random
import art
rock=art.rock
paper=art.paper
scissors=art.scissors
parts = [rock, paper, scissors]
print("\nWelcome to the game of ROCK - PAPER - SCISSORS")
i=1
countOfComp=0
count=0
while(i!=0):
    number = int(input("\nType:-\n\t0 ==> Rock\n\t1 ==> Paper\n\t2 ==> Scissors.\n\tAny other number to exit game.\n\nWhat do you choose? "))
    if(number<3):
        choice = parts[number]
        print(choice)

        print("Computer chose:")
        number2 = random.randint(0, 2)
        comp_choice = parts[number2]
        print(comp_choice)

        print("And the result is :-->")
        if number == 0 and number2 == 1 or number == 1 and number2 == 2 or number == 2 and number2 == 0:
            print("Computer wins the game.")
            countOfComp+=1
        elif number == number2:
            print("It's a DRAW!")
        else:
            print("You won the game.")
            count+=1
    else:
        print("Ending game!\nBYE.")
        if(countOfComp>count):
            print("\n\tOverall Winner is COMPUTER. AS:-->")
        elif(countOfComp==count):
            print("\n\tIt's a TIE! AS:-->")
        else:
            print("\n\tYou are the overall winnner of the game. AS:-->")
        i=0
    print(f"\tComputer Score : {countOfComp}\n\tYour Score : {count}\n")
