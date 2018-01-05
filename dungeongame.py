# max im Dungeon
# dieses Spiel braucht Python3
# b = banana
# h = healing
# # = mauer 
kevin = "@"
keller1 = """
########################################
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
########################################
"""
keller = []
for line in keller1.splitlines():
    keller.append(list(line))
   

ky = 2
kx = 1
hp = 100
hunger = 0
turn = 0
food = 5
heal = 1



while hp > 0 and hunger < 100:
    # ---- grafik anzeigen ----
    for y, line in enumerate(keller):
        for x, char in enumerate(line):
            if y == ky and x == kx:
                print(kevin, end="")
            else:
                print(char, end="")
        print() # end of line
    # ---- progress ---
    special = ""
    turn += 1
    if turn % 10 == 0:
        hunger += 1  # alle 10 turns einen hunger dazu tun
    # ---- pick up stuff ----
    if keller[ky][kx] == "b":
        print("Du findest eine Banane und nimmst sie mit")
        food += 1
        keller[ky][kx] = "."
    if keller[ky][kx] == "h":
        print("du findest ein Medpack und nimmst es mit")
        heal += 1
        keller[ky][kx] = "."
    # ---- status ----
    if hunger > 50:
        special = "*hungry*"
    status = "{} hp: {} hu: {} food: {} med: {} #: {} ".format(
             special, hp, hunger, food, heal, turn)
    # ---- keyboard control -----
    command = input(status+">>>")
    dx, dy = 0, 0
    if command == "a":
        dx = -1
    if command == "d":
        dx = 1
    if command == "w":
        dy = -1
    if command == "s":
        dy = 1
    # --- wall check ---
    if keller[ky+dy][kx+dx] == "#":
        print("aua!!")
        hp -= 1
        dx, dy = 0, 0
    # --- movement -----
    ky += dy
    kx += dx
    
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
            
    
    
    
    

