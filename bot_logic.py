import random


def gen_faction():
    factions = [
        "Chechya!Force(Tim Russia!)",
        "Osiris!Force(Tim Amerika!)",
        "Invertion!Force(Tim Indonesia!)",
        "Duty!Force(Tim China!)",
        "Centum!Force(Tim Spanyol!)",
        "Renegades!Force(Tim Inggris!)",
        "Federal!Force(Tim Ukraina!)",
        "Atlantic!Force(Tim Kanada!)",
        "National!Force(Tim India!)",
        "Cerberus!Force(Tim Filipina!)"
    ]
    return random.choice(factions)

def gen_pass(join_faction):
    summon = ""
    for i in range(join_faction):
        faction = gen_faction()
        summon += faction + "\n"
    return summon


def gen_emodji():
    emodji = [":joy:", ":heart:", ":smile:", ":astonished:", ":angry:"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "You Win!"
    else:
        return "You Lose"
 
