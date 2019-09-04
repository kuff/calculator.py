import os

def drawHelpScreen():
    os.system("clear")
    print("So far, these are the available commands for this calculator:\n\n   + help   Shows this page\n   + clear  Clears the console\n   + quit   Quits the program\n\n")
    input("Press ENTER to return")
    return False

def drawCalculatorScreen():
    os.system("clear")
    previous_value = 0 # used for carrying over result from previous calculation
    while True:
        # ask the user for an expression to evaluate
        user_input = input("> ")
        # handle "quit" and "clear" command by user
        if (user_input == "quit"):
            quit()
        elif (user_input == "clear"):
            os.system("clear")
        elif (user_input == "help"):
            return True
        else:
            # carry over the result from previous calculation if the user begins the line with an operand
            if (user_input[0] == "+" or user_input[0] == "-" or user_input[0] == "*" or user_input[0] == "/"):
                carried_over = previous_value
            else:
                carried_over = 0
            # try to parse user input as a mathematical expression
            try:
                if (carried_over != 0):
                    output = eval(str(carried_over) + user_input)
                else:
                    output = eval(user_input)
                previous_value = output
            except:
                output = ">> Invalid input"
            # draw to the screen
            print(output)

if __name__ == "__main__":
    os.system("clear")
    # TODO: draw landing screen
    input("Press ENTER to begin crunching numbers")

    show_help_screen = False
    while True:    
        if (show_help_screen):
            show_help_screen = drawHelpScreen()
        else:
            show_help_screen = drawCalculatorScreen()