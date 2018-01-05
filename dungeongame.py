# max im Dungeon
# dieses Spiel braucht Python3
helptext = """
b = banana
h = healing
# = mauer 
d = door
k = key
< = stiege rauf
> = stiege runter
@ = Kevin the hero
"""
kevin = "@"
keller1 = """
########################################
#..............................##......#
#.............................#.#......#
#..>.........................#..#......#
#...............................#......#
#...............................#......#
#......................................#
########################################
"""
keller2 = """
##############################################
#..........k.......................##........#
#.................................#..#.......#
#..<>............###d####............#.......#
#................#......#...........#........#
#................#......#..........####......#
#................#......#....................#
##############################################
"""
keller3 = """
#################################################
#.....................................###.......#
#.......................................#.......#
#...<..................................##.......#
#.......................................#.......#
#.....................................###.......#
#...............................................#
#################################################
"""



keller = []
for k in [keller1, keller2, keller3]:
    ebene = []
    for line in k.splitlines():
        ebene.append(list(line))
    keller.append(ebene)
        
   
kz = 0
ky = 2
kx = 1
hp = 100
hunger = 0
turn = 0
food = 5
heal = 1
keys = 0


while hp > 0 and hunger < 100:
    # ---- grafik anzeigen ----
    for y, line in enumerate(keller[kz]):
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
    if keller[kz][ky][kx] == "b":
        print("Du findest eine Banane und nimmst sie mit")
        food += 1
        keller[kz][ky][kx] = "."
    if keller[kz][ky][kx] == "h":
        print("du findest ein Medpack und nimmst es mit")
        heal += 1
        keller[kz][ky][kx] = "."
    # ---- stairs ----
    if keller[kz][ky][kx] == ">":
        special += " *stair down* "
    if keller[kz][ky][kx] == "<":
        special += " *stair up* "
    # ---- status ----
    if hunger > 50:
        special += " *hungry* "
    status = "{}\nhp: {} hu: {} food: {} med: {} #: {} ".format(
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
    if keller[kz][ky+dy][kx+dx] == "#":
        print("aua!!")
        hp -= 1
        dx, dy = 0, 0
    # ---- door check ----
    if keller[kz][ky+dy][kx+dx] == "d":
        if keys <= 0:
            print("aua, benutz einen Schlüssel (k)")
            hp -= 1
            dx, dy = 0, 0
        else:
            print("Du öffnest die Türe und verbrauchst einen Schlüssel")
            keys -= 1
            keller[kz][ky+dy][kx+dx] = "."
            
    # --- movement -----
    ky += dy
    kx += dx
    # --- climb stair ----
    if command == "c" or command == "climb":
        if keller[kz][ky][kx] == ">":
            print("you climb down from level {} to level {}".format(
                   kz, kz+1))
            kz += 1
        elif keller[kz][ky][kx] == "<":
            print("you climb up from level {} to level {}".format(
                    kz, kz-1))
            kz -= 1
        else:
            print("you need to find a stair (< or >) to climb")
    if command == "quit":
        print("bye-bye")
        break
    if command == "kevin ist doof":
        print("Gar nicht wahr!")
        print("mit dir spielt Kevin nicht mehr!")
        break
    if command == "?" or command == "help":
        print(helptext)
        input("press Enter")
    if command == "e":
        if food <= 0:
            print("du hast gar keine Banane!")
        else:
            hunger -= 10
            food -= 1
            print("mampf, mampf, hmmm das war gut")
        
print("Game Over")
            
    
    
    
    

