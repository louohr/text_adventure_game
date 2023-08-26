# Lost in the Woods made by Louise 2022-09-03/04

def main():
    print("-----------------------------------------------------------------------------------------------------------")
    print("""WELCOME TO THE GAME: Lost in the Woods! 
    This is a text based survival adventure game where it is up to you to escape the forest and return home. 
    There will be two choices that will be presented to you
    and the outcome will be different depending on your answer. 
    
    But before we begin, what is your name? """)

    name = input()
    print(f"Good luck, {name}. Now time to start the game...")
    print("You woke up in the woods with no memory of how you got there, and suddenly you hear a loud sound.")
    choice = input("Should you stay and wait for help or go and explore? (STAY / GO)")

    if choice == 'go':
        print("-------------------------------------------------------------------------------------------------------")
        print("\nYou decided to go and explore and you found a bridge.")
        response = input("Will you cross the bridge? (YES / NO)\n")
        if response == 'yes':
            print("---------------------------------------------------------------------------------------------------")
            print("You decided to cross the bridge and suddenly a cracking noise was heard"
                  " and the bridge started to fall to pieces.")
            print("You ended up drowning and died. GAME OVER! (Ending 2/5 was found)")
            print("---------------------------------------------------------------------------------------------------")
            restart = input("Would you like to play again?").lower()
            if restart == "yes":
                main()
            else:
                print("Thank you for playing. GOOD BYE!")
                quit()

        if response == 'no':
            print("---------------------------------------------------------------------------------------------------")
            print("You decided not to cross the bridge and instead walk around the river.")
            print("On the other side of the river you see a cave.")
        response2 = input("Should you enter the cave or not? (YES / NO)")
        if response2 == 'yes':
            print("---------------------------------------------------------------------------------------------------")
            print("You decided to enter the cave and inside you see a big and scary dragon.")
            print("But fortunately for you, there is a sword lying on the ground.")
        if response2 == 'no':
            print("---------------------------------------------------------------------------------------------------")
            print("You decided not to enter the cave. ")
            print("But it starts to rain and you could hear a thunderstorm. "
                  "Suddenly a lightning struck you down and you died. GAME OVER! (Ending 3/5 was found)")
            print("---------------------------------------------------------------------------------------------------")
            restart = input("Would you like to play again?").lower()
            if restart == "yes":
                main()
            else:
                print("Thank you for playing. GOOD BYE!")
                quit()

        response3 = input("Should you grab the sword and defend yourself or not? (GRAB / GRAB NOT)")
        if response3 == 'grab':
            print("---------------------------------------------------------------------------------------------------")
            print("You decided to grab the sword and fight the dragon.")
            print("Lucky for you, you managed to strike the dragon down and you survived.")
            print("You caught your breath and suddenly you saw a flashlight shining at you. "
                  "There was man coming right at you.")
        if response3 == 'grab not':
            print("---------------------------------------------------------------------------------------------------")
            print("You decided not to grab the sword, "
                  "but that was a bad idea since the dragon attacked you and you died. GAME OVER! (Ending 3/5)")
            print("---------------------------------------------------------------------------------------------------")
            restart = input("Would you like to play again?").lower()
            if restart == "yes":
                main()
            else:
                print("Thank you for playing. GOOD BYE!")
                quit()

        response4 = input(f'"Are you {name}?" (YES / NO)')
        if response4 == 'yes':
            print(
                "The man said he was here to save you and that they had been searching for you for hours.")
            print("Together you walked out from the cave and you could return home safely."
                  "CONGRATULATIONS, YOU FOUND THE TRUE ENDING! (Ending 5/5 was found)")
            print("---------------------------------------------------------------------------------------------------")
            restart = input("Would you like to play again?").lower()
            if restart == "yes":
                main()
            else:
                print("Thanks for playing. GOOD BYE!")
                quit()

        if response4 == 'no':
            print("The man looked confused "
                  "and left you there alone in the dark and eventually you starved to death."
                  " GAME OVER! (Ending 4/5)")
            print("---------------------------------------------------------------------------------------------------")
            restart = input("Would you like to play again?").lower()
            if restart == "yes":
                main()
            else:
                print("Thank you for playing. GOOD BYE!")
                quit()

    elif choice == 'stay':
        print(
            "---------------------------------------------------------------------------------------------------------")
        print(
            "\nYou decided to wait for help, "
            "but no one seems to come and help you, "
            "and you eventually freeze to death. GAME OVER! (Ending 1/4 was found)")
        restart = input("Would you like to play again?").lower()
        if restart == "yes":
            main()
        else:
            print("Thank you for playing. GOOD BYE!")
            quit()

    else:
        print("\nYou typed the wrong input.")
        restart = input("Would you like to play again?").lower()
        if restart == "yes":
            main()
        else:
            print("Thank you for playing. GOOD BYE!")
            quit()

main()
