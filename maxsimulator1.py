# wir simulieren einen Max
# egal was man ihm befiehlt, er sagt: "Nein"
# außer man befiehlt ihm Computer zu spielen, dann sagt er "Ja"

def max_mach(arbeit="Hausaufgaben"):
    print(arbeit+"?")
    if arbeit == "computer spielen" or arbeit == "zocken":
        print("klar, mach ich gerne!")
    else:
        print("nööö, mach ich nicht")
    
# --- Funktionsaufrufe ----
# --- function call ---

max_mach("zocken")


