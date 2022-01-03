started = False
while str != "quit":
    str = input(">")
    if str == "start":
        if started:
            print("car is already started")
        else:
            started= True
            print("start the car")
    elif str == "stop":
        if not started:
            print("car is already stoped")
        else:
            started = False
            print("stop the car")
    elif str == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif str =="":
        print("i dont understand..!")
    elif str =="quit":
        print("exit the game")
        break
    else:
        print("i dont under stand")

