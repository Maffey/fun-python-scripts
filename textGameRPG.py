# ASSIGNED VALUES
hp = 100
enemy_hp = 100

vit = 1
agi = 1
wis = 1
# Counter of how many times player upgraded his stats (vit, agi, wis).
n = 0


# DEFINED FUNCTIONS
def count_stats():
    global n
    n += 1
    return n

# Function for adding stats for your character.


def start_stats(func):
    while True:
        stat = input("Choose your " + str(func()) + ". attribute to increase.")
        global vit
        global agi
        global wis
        global n
        if stat == "str":
            vit += 1
            print ("One point was added to strength. \n")
            return vit
        elif stat == "agi":
            agi += 1
            print ("One point was added to agility. \n")
            return agi
        elif stat == "int":
            wis += 1
            print ("One point was added to intelligence. \n")
            return wis
        else:
            print ("Uups, something went wrong. Try again.")
            n -= 1

# This function shows your current stats.


def show_stats():
    print("Your current statistics look like this:")
    global vit
    global agi
    global wis
    print("Strength: " + str(vit))
    print("Agility: " + str(agi))
    print("Intelligence:  " + str(wis))

# This function takes enemy's weaknesses (based on a, b and c) and calculate,
#  based also on your stats, how much damage you deal.
#  Also, "a", "b" and "c" means respectively "weakness against strength",
#  "weakness against agility" and "weakness against intelligence".


def fight(a, b, c):
    global vit
    global agi
    global wis
    global enemy_hp

    while True:
        option = input("What you want to do? Type 'a', 'b' or 'c'.")
        if option == "a":
            enemy_hp -= (vit * 10 * a)
            print ("Your hit causes the enemy's health to drop to " + str(enemy_hp) + " points!")
            return enemy_hp

        elif option == "b":
            enemy_hp -= (agi * 10 * b)
            print ("Your hit causes the enemy's health to drop to " + str(enemy_hp) + " points!")
            return enemy_hp

        elif option == "c":
            enemy_hp -= (wis * 10 * c)
            print ("Your hit causes the enemy's health to drop to " + str(enemy_hp) + " points!")
            return enemy_hp

        else:
            print ("Uups, something went wrong. Try again.")

# This function is making sure that your enemy also hits you, based on fixed value for each enemy.


def fight_back(dmg):
    global hp
    hp -= (dmg * 10)
    print ("The enemy dealt you some damage. You have now " + str(hp) + " health points!")
    if hp <= 0:
        print ("You died!")
        input("Press ENTER to close the game.")
        raise SystemExit


# GAME INSTRUCTIONS
print (
    "Welcome, young warrior.\nYour mission is to defeat the enemies each day. "
    "You will do that by selecting the right choices. The attributes will also help you in fights. "
    "\nGood luck!\nYou have 100 hp, 1 strength, 1 agility and 1 intelligence point in the beginning. "
    "You will be able to increase those attributes later in the game.\n"
    "Let's start with selecting few attributes. By typing down 'str', 'agi' or 'int' and pressing ENTER. "
    "\n\nYou get 5 points to spend for now.")
# CHOOSING 5  ATTRIBUTES
(start_stats(count_stats))
(start_stats(count_stats))
(start_stats(count_stats))
(start_stats(count_stats))
(start_stats(count_stats))
show_stats()
# CLOSING INSTRUCTIONS, INTRODUCTION TO STORY
print("Now, after you created your character, it's time to begin the journey!\n\n")
print(
    "Day 1\nYou've just entered local tavern to find out about a fighting tournament that should start soon."
    " When you are asking people in the tavern about this, you get to meet some drunk asshole, who seems pretty stupid."
    " The guys is aggressive, even though you try to avoid the conflict."
    " You decide to test your skills on him, to warm up the muscles before great tournament.\n"
    "What do you do?\n")
# FIRST ENEMY
# TURN 1
print(
    "a) You hit him in the head with great amount of force.\nb)You attack rapidly from below.\nc) You take a bottle lying nearby and hit him with it in the head.\n")
fight(5, 7, 8)

if enemy_hp > 0:
    print (
        "The drunk man fights back, dealing some minor damage.")
    fight_back(1)
    # TURN 2
    print (
        "Now:\na) You hit him in the belly.\nb) You grab his head quickly and hit the table with it.\nc)  You grab his body smartly and take him down.")
    fight(6, 8, 9)

print (
    "The enemy has been defeated!\nYou got healed.")
# STORY
hp = 100
enemy_hp = 100
print("Your attributes were increased!\n")
(start_stats(count_stats))
show_stats()

# SECOND ENEMY



# CLOSING APP
input("Press ENTER to close the game.")
