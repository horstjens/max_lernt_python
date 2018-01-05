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
#........WW....................##......#
#.............................#.#......#
#..>.........S...............#..#......#
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

  

class Monster():
    
    zoo = []
    number = 0
    
    def __init__(self, x, y, z):
        self.number = Monster.number
        Monster.number += 1
        Monster.zoo.append(self)
        self.x = x
        self.y = y
        self.z = z
        self.hp = 1
        self.attack = 1
        self.defense = 1
        self.char = "M"
        
class Player(Monster):
    
    def __init__(self, x, y, z, name="Kevin"):
        Monster.__init__(self, x, y, z)
        self.name = name
        self.hp = 100
        self.attack = 7
        self.defense = 5
        self.hunger = 0
        self.food = 5
        self.heal = 1
        self.keys = 0  
        self.char = "@"      
        
class Statue(Monster):
    
    def __init__(self, x, y, z):
        Monster.__init__(self, x, y, z)
        self.hp = 20
        self.defense = 0
        self.attack = 2
        self.char = "S"
            
class Wolf(Monster):
    
    def __init__(self, x, y, z):
        Monster.__init__(self, x, y, z)
        self.hp = 5
        self.defense = 5
        self.attack = 5
        self.char = "W"
        
        
            
# ----- create dungeon ---

keller = []
for z,k in enumerate([keller1, keller2, keller3]):
    ebene = []
    for y, line in enumerate(k.splitlines()):
        line2 = []
        for x, char in enumerate(line):
            if char == "W":
                line2.append(".")
                Wolf(x,y,z)
            elif char == "S":
                line2.append(".")
                Statue(x,y,z)
            else:
                line2.append(char)
        ebene.append(line2)
    keller.append(ebene)
                     
turn = 0

# ---- create player -----
p1 = Player(1,2,0)

while p1.hp > 0 and p1.hunger < 100:
    # ---- grafik anzeigen ----
    for y, line in enumerate(keller[p1.z]):
        for x, char in enumerate(line):
            for m in Monster.zoo:
                if m.z == p1.z and m.y == y and m.x == x:
                    print(m.char, end="")
                    break
            else:   # else in a for loop is only executed if there was no break
                print(char, end="")
        print() # end of line
    # ---- progress ---
    special = ""
    turn += 1
    if turn % 10 == 0:
        p1.hunger += 1  # alle 10 turns einen hunger dazu tun
    # ---- pick up stuff ----
    if keller[p1.z][p1.y][p1.x] == "b":
        print("Du findest eine Banane und nimmst sie mit")
        p1.food += 1
        keller[p1.z][p1.y][p1.x] = "."
    if keller[p1.z][p1.y][p1.x] == "h":
        print("du findest ein Medpack und nimmst es mit")
        p1.heal += 1
        keller[p1.z][p1.y][p1.x] = "."
    # ---- stairs ----
    if keller[p1.z][p1.y][p1.x] == ">":
        special += " *stair down* "
    if keller[p1.z][p1.y][p1.x] == "<":
        special += " *stair up* "
    # ---- status ----
    if p1.hunger > 50:
        special += " *hungry* "
    status = "{}\nhp: {} hu: {} food: {} med: {} #: {} ".format(
             special, p1.hp, p1.hunger, p1.food, p1.heal, turn)
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
    if keller[p1.z][p1.y+dy][p1.x+dx] == "#":
        print("aua!!")
        p1.hp -= 1
        dx, dy = 0, 0
    # ---- door check ----
    if keller[p1.z][p1.y+dy][p1.x+dx] == "d":
        if p1.keys <= 0:
            print("aua, benutz einen Schlüssel (k)")
            p1.hp -= 1
            dx, dy = 0, 0
        else:
            print("Du öffnest die Türe und verbrauchst einen Schlüssel")
            p1.keys -= 1
            keller[p1.z][p1.y+dy][p1.x+dx] = "."
            
    # --- movement -----
    p1.y += dy
    p1.x += dx
    # --- climb stair ----
    if command == "c" or command == "climb":
        if keller[p1.z][p1.y][p1.x] == ">":
            print("you climb down from level {} to level {}".format(
                   p1.z, p1.z+1))
            p1.z += 1
        elif keller[p1.z][p1.y][p1.x] == "<":
            print("you climb up from level {} to level {}".format(
                    p1.z, p1.z-1))
            p1.z -= 1
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
        if p1.food <= 0:
            print("du hast gar keine Banane!")
        else:
            p1.hunger -= 10
            p1.food -= 1
            print("mampf, mampf, hmmm das war gut")
        
print("Game Over")
