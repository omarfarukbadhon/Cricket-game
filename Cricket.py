# Omar Faruk Badhon 
# Mail: omarfarukbadhon@gmail.com

# Its a number match cricket game that is quite propular in my area. When I was in school all of my friends try to spend our gap time to play this game with our fingure to match number with other


from random import randint, choice
from time import sleep
Toss_selection = ["H", "T"]
bat_ball_selection = ["bat", "ball"]
over = [1, 2]
your_net_run = 0
computer_net_run = 0


def my_bating():
        print("You have 3 wickets!!!")
        wicket = 0
        over_decision = int(input("How many over do you want to play?\n1 or 2\n"))
        print(f"Now let's start to play")
        sleep(2)
        ball = 0
        your_run = 0
        global your_net_run
        if over_decision == 1:
            while ball < 6:
                computer = [1, 2, 3, 4, 5, 6]
                computer_number = choice(computer)
                run = int(input("Enter your number between 0 to 6: "))
                # print(f"Computer pick {computer_number}")
                if computer_number == run:
                    wicket = wicket + 1
                    print(f"You loose your {wicket} wicket and your run is {your_run} and over 0.{ball}\n")
                    if wicket == 3:
                        print("You lost your all wickets\n")
                        computer_bating_over1()
                else:
                    your_run = your_run + run
                    print(f"Your total run is {your_run} and over 0.{ball}\n")
                ball = ball + 1
            print(f"Your total score is {your_run}\n")
            your_net_run = your_run
            computer_bating_over1()
        elif over_decision == 2:
            while ball < 12:
                computer = [1, 2, 3, 4, 5, 6]
                computer_number = choice(computer)
                run = int(input("Enter your number between 0 to 6: "))
                # print(f"Computer pick {computer_number}")
                if computer_number == run:
                    wicket = wicket + 1
                    print(f"You loose your {wicket} wicket and your run is {your_run}\n")
                    if wicket == 3:
                        print("You lost your all wickets\n")
                        computer_bating_over2()
                else:
                    your_run = your_run + run
                    print(f"Your total run is {your_run}\n")
                ball = ball + 1
            print(f"Your total score is {your_run}\n")
            your_net_run = your_run
            computer_bating_over2()
        else:
            print("Please select over 1 or 2")


def computer_bating_over1():
        print("Now Computer's to bat.....\n")
        print("Preparing for bating..........\n")
        sleep(3)
        wicket = 0
        ball = 0
        computer_run = 0
        while ball < 6:
            computer = [1, 2, 3, 4, 5, 6]
            computer_number = choice(computer)
            run = int(input("Enter your number between 0 to 6: "))
            # print(f"Computer pick {computer_number}")
            if computer_number == run:
                wicket = wicket + 1
                print(f"Computer loose it's {wicket} wicket and computer run is {computer_run}\n")
                if wicket == 3:
                    print("Computer lost it's all wickets\n")
            else:
                computer_run = computer_run + computer_number
                print(f"Computer total run is {computer_run}\n")
            ball = ball + 1
        print(f"Computer total score is {computer_run}\n")
        if computer_run > your_net_run:
            print("Computer won the match\n")
        else:
            print("You won the match!!!\n")
        play_loop()


def computer_bating_over2():
        print("Now Computer's to bat....\n")
        print("Preparing for bating..........\n")
        sleep(3)
        wicket = 0
        ball = 0
        computer_run = 0
        while ball < 12:
            computer = [1, 2, 3, 4, 5, 6]
            computer_number = choice(computer)
            run = int(input("Enter your number between 0 to 6: "))
            # print(f"Computer pick {computer_number}")
            if computer_number == run:
                wicket = wicket + 1
                print(f"Computer loose it's {wicket} wicket and computer run is {computer_run}\n")
                if wicket == 3:
                    print("Computer lost it's all wickets\n")
            else:
                computer_run = computer_run + computer_number
                print(f"Computer total run is {computer_run}\n")
            ball = ball + 1
        print(f"Computer total score is {computer_run}\n")
        if computer_run > your_net_run:
            print("Computer won the match\n")
        else:
            print("You won the match!!!\n")
        play_loop()


def computer_bating():
        print("Computer have 3 wickets!!!")
        print(f"Now let's start to play")
        sleep(2)
        wicket = 0
        over_decision = choice(over)
        ball = 0
        computer_run = 0
        global computer_net_run
        if over_decision == 1:
            while ball < 6:
                computer = [1, 2, 3, 4, 5, 6]
                computer_number = choice(computer)
                run = int(input("Enter your number between 0 to 6: "))
                # print(f"Computer pick {computer_number}")
                if computer_number == run:
                    wicket = wicket + 1
                    print(f"Computer loose it's {wicket} wicket and computer run is {computer_run}\n")
                    if wicket == 3:
                        print("Computer lost it's all wickets\n")
                        my_bating_over1()
                else:
                    computer_run = computer_run + computer_number
                    print(f"Computer total run is {computer_run}")
                ball = ball + 1
            print(f"Computer total score is {computer_run}")
            computer_net_run = computer_run
            my_bating_over1()
        elif over_decision == 2:
            while ball < 12:
                computer = [1, 2, 3, 4, 5, 6]
                computer_number = choice(computer)
                run = int(input("Enter your number between 0 to 6: "))
                # print(f"Computer pick {computer_number}")
                if computer_number == run:
                    wicket = wicket + 1
                    print(f"Computer loose it's {wicket} wicket and computer run is {computer_run}\n")
                    if wicket == 3:
                        print("Computer lost it's all wickets\n")
                        my_bating_over2()
                else:
                    computer_run = computer_run + computer_number
                    print(f"Computer total run is {computer_run}")
                ball = ball + 1
            print(f"Computer total score is {computer_run}")
            computer_net_run = computer_run
            my_bating_over2()


def my_bating_over1():
        print("Now Your's turn to bat.....")
        print("Preparing for bating..........")
        sleep(3)
        wicket = 0
        ball = 0
        your_run = 0
        while ball < 6:
            computer = [1, 2, 3, 4, 5, 6]
            computer_number = choice(computer)
            run = int(input("Enter your number between 0 to 6: "))
            # print(f"Computer pick {computer_number}")
            if computer_number == run:
                wicket = wicket + 1
                print(f"You loose your {wicket} wicket and your run is {your_run}\n")
                if wicket == 3:
                    print("you lost your all wickets\n")
            else:
                your_run = your_run + run
                print(f"Your total run is {your_run}\n")
            ball = ball + 1
        print(f"Your total score is {your_run}\n")
        if computer_net_run > your_run:
            print("Computer won the match\n")
        else:
            print("You won the match!!!\n")
        play_loop()


def my_bating_over2():
        print("Now Your's turn to bat.....")
        print("Preparing for bating..........")
        sleep(3)
        wicket = 0
        ball = 0
        your_run = 0
        while ball < 12:
            computer = [1, 2, 3, 4, 5, 6]
            computer_number = choice(computer)
            run = int(input("Enter your number between 0 to 6: "))
            # print(f"Computer pick {computer_number}")
            if computer_number == run:
                wicket = wicket + 1
                print(f"You loose your {wicket} wicket and your run is {your_run}\n")
                if wicket == 3:
                    print("you lost your all wickets\n")
            else:
                your_run = your_run + run
                print(f"Your total run is {your_run}\n")
            ball = ball + 1
        print(f"Your total score is {your_run}\n")
        if computer_net_run > your_run:
            print("Computer won the match\n")
        else:
            print("You won the match!!!\n")
        play_loop()


def toss():
    choose = str(input("Are you want to toss(y = yes or n = Not): "))
    if choose == "n":
        try:
            toss_your_selection = str(input("Head(H) or Tail(T): "))
            if toss_your_selection == choice(Toss_selection):
                print("You won the toss!!!!\n")
                bat_ball = str(input("Your turn to decide bat or ball: "))
                if bat_ball == "bat":
                    print("Preparing for bating..........")
                    sleep(3)
                    my_bating()
                else:
                    print("Preparing for balling..........")
                    sleep(3)
                    computer_bating()
            else:
                print("You loose the toss.....\nComputer won\nComputer turns to decide Bat or Ball\n")
                print("Decision pending.........")
                sleep(3)
                bat_ball = choice(bat_ball_selection)
                if bat_ball == "bat":
                    print("Computer has decided to bat first")
                    print("Preparing for bating..........")
                    sleep(3)
                    computer_bating()
                else:
                    print("Computer has decided to ball first")
                    print("Preparing for balling..........")
                    sleep(3)
                    my_bating()
        except Exception as e:
            print("Please select H or Y")
    elif choose == "y":
        print("Computer selecting(H or T).......")
        sleep(3)
        toss_computer_selection = choice(Toss_selection)
        print(f"Computer select {toss_computer_selection}")
        if toss_computer_selection == choice(Toss_selection):
            print("Computer Won the toss!!!!!\nComputer turns to decide Bat or Ball\n")
            print("Decision pending.........")
            sleep(3)
            bat_ball = choice(bat_ball_selection)
            if bat_ball == "bat":
                print("Computer has decided to bat first")
                print("Preparing for bating..........")
                sleep(3)
                computer_bating()
            else:
                print("Computer has decided to ball first")
                print("Preparing for balling..........")
                sleep(3)
                my_bating()
        else:
            print("Computer loose the toss.....\nYou won\nYour turn to decide Bat or Ball\n")
            bat_ball = str(input("Your turn to decide bat or ball: "))
            if bat_ball == "bat":
                print("Preparing for bating..........")
                sleep(3)
                my_bating()
            else:
                print("Preparing for balling..........")
                sleep(3)
                computer_bating()

    else:
        print("Select y or n")


# for looping the game
def play_loop():
    ques_again = str(input("Would you like to play again? (y/n)\n").lower())
    if ques_again == 'y':
        toss()

    elif ques_again == 'n':
        print("Thanks for play!")

    else:
        print("What was that?/n")
        play_loop()


if __name__ == "__main__":  # Only run this if run from commandline
    toss()




