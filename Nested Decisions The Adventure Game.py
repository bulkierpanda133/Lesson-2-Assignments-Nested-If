#Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


#Task 2: Setting the Scene
place = input("Choose a place: forest or cave?\n")

if place == "forest":
    action = input("climb a tree or cross a river?\n")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    
elif place == "cave":
    action = input("want to light a torch or proceed in the dark?\n")
    if action == "light a torch":
        print("the cave is now visible because of the torch's light and you found hidden treasure")
    elif action == "proceed in the dark":
        print("you fell into a pit ypu are now trapped")


#Task 3: Default Path
place = input("Choose a place: forest or cave?\n")

if place == "forest":
    action = input("climb a tree or cross a river?\n")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("want to light a torch or proceed in the dark?\n")
    if action == "light a torch":
        print("the cave is now visible because of the torch's light and you found hidden treasure")
    elif action == "proceed in the dark":
        print("you fell into a pit ypu are now trapped")
    else:
        pass
else:
    pass