import random

freunde = ["Kevin","Julia", "Martin", "Michi", "Andrea", "Rene"]
orte = ["im Auto", "auf der Straße", "am Schulhof", "im Flugzeug"]
verben = ["küsst", "schlägt", "verfolgt", "beleidigt", "spielt mit", "beisst"]
adverben = ["leidenschaftlich", "bösartig", "lachend", "angestrengt","gelangweilt"]

for x in range(5):
    freund1 = random.choice(freunde)
    freund2 = random.choice(freunde)
    ort = random.choice(orte)
    verb = random.choice(verben)
    adverb = random.choice(adverben)
    print(freund1, verb, freund2,  adverb, ort)
    
