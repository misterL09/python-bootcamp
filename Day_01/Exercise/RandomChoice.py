from random import choice
options = ["rock","paper","scissor"]

def result(input_result):
    if input_result==1:
        print("You Win!")
    elif input_result==2:
        print("You Lose!")
    else:
        print("Draw!")

def check_result(user_choice,cpu_choice):
    match user_choice:
        case "rock":
            if cpu_choice=="scissor":
                result(1)
            elif cpu_choice=="paper":
                result(2)
            else:
                result(3)
        case "paper":
            if cpu_choice == "rock":
                result(1)
            elif cpu_choice == "scissor":
                result(2)
            else:
                result(3)
        case "scissor":
            if cpu_choice == "paper":
                result(1)
            elif cpu_choice == "rock":
                result(2)
            else:
                result(3)

try:
    stop_program = False
    while not stop_program:
        user_choice = input("Pick a choice (rock/paper/scissors): ")
        listchoice = ["rock", "scissors", "paper"]
        found = False
        for item in listchoice:
            if item == user_choice:
                found = True
                break
        match found:
            case False:
                print("Your input is not in the choices!")
            case True:
                random_option = choice(options)
                cpu_choice = random_option
                print("cpu choice:", cpu_choice)
                check_result(user_choice, cpu_choice)

        x = input("Try Again? Y/N: ")
        if x == "N":
            stop_program = True

except ValueError:
    print("this is not a number")



