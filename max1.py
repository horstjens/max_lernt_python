# max im Dungeon
# dieses Spiel braucht Python3
# b = banana
# h = healing
kevin = "@"
keller = list("...b....b....b....h...h...h...b..")

kx = 0
hp = 100
hunger = 0
turn = 0
food = 5
heal = 1

while hp > 0 and hunger < 100:
    # ---- grafik anzeigen ----
    for x, tile in enumerate(keller):
        if x == kx:
            print(kevin, end="")
        else:
            print(tile, end="")
    print() # end of line
    # ---- progress ---
    special = ""
    turn += 1
    if turn % 10 == 0:
        hunger += 1  # alle 10 turns einen hunger dazu tun
    # ---- pick up stuff ----
    if keller[kx] == "b":
        print("Du findest eine Banane und nimmst sie mit")
        food += 1
        keller[kx] = "."
    if keller[kx] == "h":
        print("du findest ein Medpack und nimmst es mit")
        heal += 1
        keller[kx] = "."
    # ---- status ----
    if hunger > 50:
        special = "*hungry*"
    status = "{} hp: {} hu: {} food: {} med: {} #: {} ".format(
             special, hp, hunger, food, heal, turn)
    # ---- keyboard control -----
    command = input(status+">>>")
    if command == "a":
        kx -= 1
    if command == "d":
        kx += 1
    if command == "quit":
        print("bye-bye")
        break
    if command == "kevin ist doof":
        print("Gar nicht wahr!")
        print("mit dir spielt Kevin nicht mehr!")
        break
    if command == "e":
        if food <= 0:
            print("du hast gar keine Banane!")
        else:
            hunger -= 10
            food -= 1
            print("mampf, mampf, hmmm das war gut")
        
print("Game Over")
            
    
    
    
    

