def adventure():
    # do work
    return play_again()

def play_again():
    paths = ["North", "South", "East", "West"]

    life = 5
    moves_1 = 1
    moves_2 = 1
    moves_3 = 1
    wall = "SBAM. You hit a wall and you feint again."
    mud_pond = "PLOP! You are covered in Mud!"
    water = "Splash. Fantastic, you are completely wet now!"
    fire = 'You hear someone singing: "And it buuurns, buuurns, buuurns the ring of fiiiiiiiiiiiire".\nWell, it really burns!'

    while life != 0:
        print("\nYou wake up in a dark room. All directions looks the same to you.")
        print(" - ".join(paths))
        print("life:" + str(life))
        chosen_path_1 = str.casefold(input("\nYou have to take a decision. Where do you go?:"))
        if chosen_path_1 == str.casefold("North") or chosen_path_1 == str.casefold("South"):
            life = life - 1
            print(wall)
            print("life:" + str(life))
        elif chosen_path_1 == str.casefold("West"):
            life = life - 1
            print(mud_pond)
            print("life:" + str(life))
        elif chosen_path_1 == str.casefold("East"):
            print("\nA door cracking opens revealing you another room...")
            print(" - ".join(paths))
            print("life:" + str(life))
            break
        moves_1 += 1
    while life != 0:
        chosen_path_2 = str.casefold(input("\nOnce again you can count only on your instinct. Where do you go?:"))
        print(" - ".join(paths))
        if chosen_path_2 == str.casefold("North") or chosen_path_2 == str.casefold("East"):
            life = life - 1
            print(water)
            print("life:" + str(life))
        elif chosen_path_2 == str.casefold("west"):
            print("The door is locked. You cannot go back")
        elif chosen_path_2 == str.casefold("South"):
            print("\nThe door in front of you disappear revealing you, guess what?! another room...")
            print(" - ".join(paths))
            break
        moves_2 += 1
    while life != 0:
        chosen_path_3 = str.casefold(input("\nWhere do you go this time?:"))
        print(" - ".join(paths))
        if chosen_path_3 == str.casefold("North"):
            print("Oh no, You cannot see any door just... Dust...")
        elif chosen_path_3 == str.casefold("east"):
            life = life - 1
            print(fire)
            print("life:" + str(life))
        elif chosen_path_3 == str.casefold("south"):
            life = life - 1
            print(mud_pond)
            print("life:" + str(life))
        elif chosen_path_3 == str.casefold("west"):
            print("\nWell done you see the light\n")
            print("You made it in {} moves\n".format(moves_1 + moves_2 + moves_3))
            break
        moves_3 += 1

    while life != 0:
        again = str.casefold(input("Do you want to try again?\n \nInsert Coin\n \nPlease type Y for yes or N for no:"))
        if again not in {"y", "n"}:
            print("please enter valid input")
        elif again == "n":
            return "Thank you, bye!"
            #are you sure?
        elif again == "y":
            # call function to start the game again
            return adventure()

    else:
        print("Game Over\n")
        again = str.casefold(input("Do you want to try again?\n \nInsert Coin\n \nPlease type Y for yes or N for no:"))
        if again not in {"y", "n"}:
            print("please enter valid input")
        elif again == "n":
            return "Thank you, bye!"
            #are you sure?
        elif again == "y":
            # call function to start the game again
            return adventure()

adventure()
