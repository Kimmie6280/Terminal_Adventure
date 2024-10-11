import random
print("--------------------------------------------")

while True:
    character = input(f'Choose your Character| Elf | Swordsman | Wizard |')
    if character.lower() == 'elf':
        print("You are an Elf")
        break
    elif character.lower() == 'swordsman':
        print("You are a Swordsman")
        break
    elif character.lower() == 'wizard':
        print("You are a Wizard")
        break
    else:
        print("Please choose a character")
        break

while True:
    answer = input('You are you ready for your adventure? ')
    if answer.lower() == 'yes':
        print("ok lets continue")
        break
    else:
        print('goodbye')
        break

# hps
currenthp = 100
enemyhp = 150

print("You have encountered an enemy. It is a warlock!")
print("You have 100 hp. To attack, use 1 for magic wand, 2 for direct hit, and 3 for storm attack.")
print("If the enemy hits you, you lose hp. If you hit the enemy, they lose hp.")

while currenthp > 10:
    print("------------------------")
    print("My hp is", currenthp)
    print("Enemy hp is", enemyhp)

    attack = int(input("Which attack are you choosing? 1, 2, or 3: "))
    print("------------------------")

    # Generate new random values for damage and attack hit chance each round
    magicwand = random.randint(1, 9)
    directhit = random.randint(5, 15)
    stormattact = random.randint(10, 30)
    enemyattackhit = random.randint(0, 3)
    enemyhit = random.randint(5, 15)

    if attack == 1 and enemyattackhit <= 1:
        enemyhp -= magicwand
        print("The enemy has taken a hit. They lost hp ", magicwand)
    elif attack == 1 and enemyattackhit > 1:
        currenthp -= enemyhit
        print("Your attack failed, and you lost hp ", currenthp)

    elif attack == 2 and enemyattackhit <= 1:
        enemyhp -= directhit
        print("The enemy has taken a hit. They lost hp ", directhit)
    elif attack == 2 and enemyattackhit > 1:
        currenthp -= enemyhit
        print("Your attack failed, and you lost hp ", currenthp)

    elif attack == 3 and enemyattackhit <= 1:
        enemyhp -= stormattact
        print("The enemy has taken a hit. They lost hp ", stormattact)
    elif attack == 3 and enemyattackhit > 1:
        currenthp -= enemyhit
        print("Your attack failed, and you lost hp ", currenthp)

    else:
        print("You did not choose an attack.")

    if enemyhp <= 0:
        print("You won!")
        break
    elif currenthp <= 0:
        print("You lost!")
        break
