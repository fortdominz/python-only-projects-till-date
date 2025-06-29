# CAR GAME


while True:
    command = input("> ").lower()   # with .lower() whatever the user input, whether capital or small, it automatically converts to all small letters. This is to prevent an error as all commands have been written in small caps.
    if command == "start":
        print("Car is started... ")
    elif command == "stop":
        print("Car is stopped... ")
    elif command == "drive":
        print("where is your destination?... ")
    elif command == "quit":
        break
    elif command == "help":
        print("""
        YOU HAVE REACHED THE HELP CENTRE.
        MANUAL: AVAILABLE COMMANDS FOR THE CAR ARE AS FOLLOWS:
        (1.) start = to start the car
        (2.) stop = to stop the car
        (3.) drive = to ask for destination before moving
        (4.) quit = to exit the whole process
        (5.) help = to reach out to help centre and have access to available commands in the manual
        """)
    else:
        print("Sorry, Command not available, input 'help' to access manual for all available commands.")