# The Great Engineering Text Adventure
# Authors: Mitchell Lemieux, Tyler Kashak
# Music: Brian, Erik What music do we have lol?
# Start Date: April 14th, 2018
# Library of Items and Locations
# Latest Edit 22/2/2019
"""
Rules for Writing Objects in the Eng Phys Text Adventure
0. ALWAYS check the paramaters of the object. If unsure check game_classes_2017.py for the constructor
1. Use " (\S)" instead of "\n" for newline characters
2. If using ANY quotes (" or ') ONLY use ' inside strings.
The " quote is used to define the string boundry and any in the sentence will break the string.
ex) "You think to yourself 'Gee, do I like quotes'! 'Lets go somewhere!' "
not) "You think to yourself "Gee, do I like quotes"! "Lets go somewhere"! "
3. When an attribute is "None" it needs to be capitalized as such: "None"
4. When Naming a MAP

Obsolete: 5. When puting a needed or dropped object.name in an interact it MUST be lowercase.
All object keys in the game are stored lowercase and used to throw a key error but are now changed in the constructor
"""


from game_classes_2017 import *
import csv
from Colour import *

# these define bounds of the list constructor MAPS1, they control this main loop
# TODO Get rid of these ranges and make them dimension specific with dimension dictionary
XRANGE = 10  # when changing these also change the values in the CreativeMode.load() function
YRANGE = 10
ZRANGE = 5
DRANGE = 6  # Dimensional range of the map, i.e. number of different buildings/dimensions with interiors + overworld
# TODO IF game starts to slow down due to size of MAPS1 empty spaces in this definition:
#  we'll have to define some funky magic to define different map dictionaries
#  OR Redefine how the constructor works so don't have to loop through huge empty space to define an new map location

dimension_names = ["OverWorld", "BSB", "Capstone Room", "Green Lake"]


def PlayableCharacters(ITEMS):
    # --- Character Setup ---

    EMPTYHEAD = Equipment('EMPTY', (None, None, None), 'EMPTY.png',
                          'Nothing is Equipped', 'head', (0, 0, 0), -101)
    EMPTYBODY = Equipment('EMPTY', (None, None, None), 'EMPTY.png',
                          'Nothing is Equipped', 'body', (0, 0, 0), -101)
    EMPTYHAND = Equipment('EMPTY', (None, None, None), 'EMPTY.png',
                          'Nothing is Equipped', 'hand', (0, 0, 0), -101)
    EMPTYOFFHAND = Equipment('EMPTY', (None, None, None), 'EMPTY.png',
                             'Nothing is Equipped', 'off-hand', (0, 0, 0), -101)
    EMPTYINV = {'head': EMPTYHEAD, 'body': EMPTYBODY,
                'hand': EMPTYHAND, 'off-hand': EMPTYOFFHAND}

    # TODO Make PLAYER into PLAYERS a dictionary of playable characters objects
    STARTLOCATION = (0, 0, 0, 2)
    STARTHEALTH = 100
    STARTINV = {'head': EMPTYHEAD, 'body': EMPTYBODY,
                'hand': EMPTYHAND, 'off-hand': EMPTYOFFHAND}
    PLAYER = Character('Minnick', list(STARTLOCATION),
                       STARTHEALTH, STARTINV, EMPTYINV)

    BRENSTARTLOCATION = (0, 0, 0, 2)  # Dev start location
    # (4,0,0,4)  haunted forest
    # (2,3,1,0)  default location
    # EACH INVENTORY HAS TO BE UNIQUE
    # BRENINV = EMPTYINV  # THIS CAUSED GHOSTING AND DUPLICATION I THINK BECAUSE OF same referenced object
    BRENINV = {'head': EMPTYHEAD, 'body': EMPTYBODY, 'hand': EMPTYHAND,
               'off-hand': EMPTYOFFHAND}  # needs to be unique or else ghosting
    # BRENINV = {'head':ITEMS["tyler's visor glasses"],'body':ITEMS["tyler's big hits shirt"],'hand':ITEMS["tyler's hulk hands"],'off-hand':ITEMS["tyler's green bang bong"]} #gets to have the Iron Ring when he graduates
    DEVPLAYER = Character('Brendan Fallon', list(
        BRENSTARTLOCATION), 999, BRENINV, EMPTYINV)

    return PLAYER, DEVPLAYER


def Reset():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    global INTERACT1

    # Using List comprehensions to define the null map space of the game for objects to be put into
    # TODO make a more memory effecient space constructor (maybe based on size of dimension so they're resizable)
    # Ineffecient due to number of empty spaces and each dimension being 10x10x5 but whatever for now. They're just nonetypes so probably not a lot of bits.
    MAPS1 = [[[[None for dim in range(DRANGE)] for z in range(
        ZRANGE)] for y in range(YRANGE)] for x in range(XRANGE)]

    LOCATIONS1 = [
        # --- OVERWORLD: Dimension 0 ---

        # --- BSB: Dimension 1 ---
        Map("BSB Basement Hallway", (0, 0, 0, 1), "~BSB Basement Hallway~:\n",
            "This endless hallway seems to go on forever. No matter how far you run in each direction you seem to go nowhere.", ('l', 'r', 'f', 'u', 'd'), True, 1, [("b", 1, 2, 0, 2)]),

        # --- CAPSTONE ROOM: Dimension 2 ---
        Map("THE ECLIPSE", (0, 0, 0, 2), "THE ECLIPSE~:\n",
            "AW DANG The Eclipse! But yeah this windshield is a bit much", ('l', 'b', 'd', 'u'), True),
        Map("ZebraShark", (0, 1, 0, 2), "ZebraShark~:\n",
            "Where are they? O.m.g. is that a pool downstairs?", ('l', 'd', 'u'), True),
        Map("T.A. Area", (0, 2, 0, 2), "T.A. Area~:\n",
            "Is this where the PSRs get lost? Also just storage space for STARS", ('f', 'l', 'd', 'u'), True),

        Map("S.T.A.R.S.", (1, 0, 0, 2), "S.T.A.R.S.~:\n",
            "S.T.A.R.S. PLEASE WORK.\nYou see a man wearing a pink shirt and a giant robot point a cannon where ever he goes.\nIs this how the world ends?",
            ('b', 'd', 'u'), True),  # S.T.A.R.S. System T69
        Map("FRAS", (1, 1, 0, 2), "FRAS~:\n",
            "Yeah that's a tank. This is a 3D printed Tank.", ('d', 'u'), True),
        Map("Capstone Doorway", (1, 2, 0, 2), "Capstone Doorway~:\n",
            "This beeping door is the bane of your existance on late nights", ('d', 'u'), True, 1, [("f", 0, 0, 0, 1)]),

        Map("NANOrims", (2, 0, 0, 2), "NANOrims~:\n",
            "NANNNOOORYMMSS.", ('r', 'd', 'u'), True),
        Map("Milli", (2, 1, 0, 2), "Milli~:\n",
            "Great Job Mili!", ('r', 'd', 'u'), True),
        Map("Circuit Smart", (2, 2, 0, 2), "Circuit Smart~:\n",
            "(Print text of spagetti)\nIf you unplugged one wire of this these people would go insane.", ('f', 'r', 'u', 'd'), True),

        # Map("Electronics Lab", (0, 1, 0, 1), "Peter's Lab~:\n", "I'm just glad to not have to be in here anymore.",( 'l','f','u','d'), True),
        # Map("Peter Jonasson's Office", (0, 1, 0, 1), "Peter Johnason's Office~:\n", "The grand sorcerer's mystic place",('b', 'l','r','u','d'), True),

        # --- GREEN LAKE: Dimension 3 ---
        Map("Green Lake", (0, 0, 0, 3), "~~", "You wake up in a peaceful place. The water is rushing by down on a nearby like. The leaves are blowing in the wind casting shadows in the green clearing. You feel the warm sun kissing your skin. (\S)Standing just in front of log house you see an old black lab. Sitting patiently waiting for you to throw his ball. He sits beside a sign that reads: Freds' Place.", ('f', 'b', 'l', 'r', 'u', 'd'), True)

    ]

    # TODO Sort items back into "Head", "Body", "Hand", "Off-hand", "Special" (quest items). Via CSVs is the easiest way
    # On the one hand CSVs or at least some form of abstract class manipulation makes sense to deal with scale of objects.
    # But having a dynamic script does allow more flexibility (but you don't need that flexibity in standard objects)
    # Other flexibility and new behaviour is done in defining new types, scripting,  etc.
    ITEMS1 = [

        # --- CAPSTONE ROOM: Dimension 2 ---

        Equipment("Old Car Keys", (1, 0, 0, 2), "CarKeys.jpg",
                  "Fun for babies. Not for Batman.", "off-hand", (7, 0, 15), ""),
        Equipment("Dirty Needle", (2, 2, 0, 2), "Needle.jpg",
                  "This isn't clean. Someone find me a SharpXchange!", "hand", (7, 0, 5), ""),
        Equipment("Clean Needle", (None), "CleanNeedle.jpg",
                  "No more spreadin' disease!", "hand", (25, 0, 9), ""),
        Equipment("Pizza Box", (2, 1, 0, 2), "PizzaBox.jpg",
                  "Fully equipped with crusted cheese.", "body", (1, 5, 1), 3),
        Equipment("Eng Phys USB Pen", (None), "PhysPen.jpg",
                  "It would be amazing if this thing actually worked. If I had a laptop I could plug it in and find all of 2P04.", "hand", (5, 0, 5), ""),


        # Green Lake Items
        Equipment("Tennis Ball", (0, 0, 0, 3), "TennisBall.jpg",
                  "The slobery wet ball that belongs to Fred. He's probably looking for it.", "hand", (1, 1, 1), ""),
        Equipment("Dog biscuit", (0, 0, 0, 3), "DogBiscuit.jpg",
                  "Probably better known as a cookie. One of Fred's favourite snacks.", "off-hand", (1, 1, 1), 3),
        Equipment("Softwood 2x4 Stud", (0, 0, 0, 3), "Soft2x3Stud.jpg",
                  "A prime peice of Douglas Fir. Useful to be made into whatever you can imagine", "off-hand", (1, 1, 1), ""),

    ]  # DON"T FORGET TO REMOVE THE LAST COMA!

    ENEMIES1 = [

        # --- CAPSTONE ROOM: Dimension 2 ---
        Enemy("Dr. Minnick",
              "'Hello and welcome to " + deadpersoncolour + \
              "8 months of HELL" + textcolour + "! MUAHAHAHA.",
              (1, 1, 0, 2), (400, 400, 400), 200, "eng phys usb pen", None,
              "Oh, somehow you have pleased me?",
              "I'm jealous of stupid people, they have more opportunities to learn!", False),

        # --- Green Lake People ---
        Animal("Fred the Good Boy", "You talk to Fred. His wise eyes stare at you. It's almost as if he understands what you're saying but he'd rather have have you play with the ball.", (0, 0, 0, 3), (9999, 9999, 9999), 9999,
               "tennis ball", "tennis ball", "Fred barks happily. He chews on it for a second and then kicks it back happily to you.", "", "He smiles at you happily! His tail wags but you can tell he just wants to play with the ball.", True)

    ]

    INTERACT1 = [

        # --- CAPSTONE ROOM: Dimension 2 ---
        Interact("Rules Sign", (2, 2, 0, 2),
                 "It reads: (\S)THERE ARE NO RULES", "", "", "", False),
        Interact("Lenovo Laptop", (0, 0, 0, 2), "This heap of computing majesty could block bullets... I think...",
                 "You plug in the Eng Phs USB Pen.\nYou find all of 2P04 files, who uses FlexPDE anymore? You also find a \nweird exe called the Eng Phys Text Adventure! That sounds like fun.\nYou hear a drumming in your ears, is that coming from the pen?",
                 "eng phys usb pen", "", False),

        # Green Lake Interactables
        Interact("SharpXChange", (None), "Would you like to exchange a needle?", "Needle Accepted!",
                 "dirty needle", "clean needle", False),
        Interact("Lake Painting", (0, 2, 0, 2), "A painting of a beautiful lake. It brings you peace.",
                 "You feel a pull. All of a sudden you're being pulled into the painting and all around you it's getting bright. (\S)You wake up to the sound of birds chirping and a soft breeze.", "old car keys", None, True),
        Interact("Portkey", (0, 0, 0, 3), "This portkey looks like the way back. Whatever magic brought you here must be related to this lake.",
                 "Your world compresses as you're pulled violently into something. (\S)You're back in the Art Museum. Were you ever gone?", None, None, True),
        Interact("Rick's Crafting Bench", (0, 0, 0, 3), "This bench can create anything made of wood or diamond.",
                 "You spend hours crafting the device to the precision you need. It's perfect.", "softwood 2x4 stud", "sharpxchange", True),
    ]


Reset()

# TODO If Rebuild: Make this into a dictionary with an adjacency list (Graph/path). Not sure if in object or not


def WorldMap():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    for i in LOCATIONS1:
        position = i.location
        x = position[0]
        y = position[1]
        z = position[2]
        dim = position[3]
        MAPS1[x][y][z][dim] = i
    for i in ENEMIES1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].place_enemy(i)
        else:
            i.location = (None, None, None, None)
        if i.need:
            # this fixed a key error where it would crash because it looked for the uppercase version of an item_object
            i.need = i.need.lower()
        if i.drop:
            # this fixed a key error where it would crash because it looked for the uppercase version of an item_object
            i.drop = i.drop.lower()
    for i in ITEMS1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].place_item(i)
        else:
            i.location = (None, None, None, None)
    for i in INTERACT1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].place_item(i)
        else:
            i.location = (None, None, None, None)
        if i.need:
            # this fixed a key error where it would crash because it looked for the uppercase version of an item_object
            i.need = i.need.lower()
        if i.drop:
            # this fixed a key error where it would crash because it looked for the uppercase version of an item_object
            i.drop = i.drop.lower()
    return tuple(MAPS1)


def ItemDictionary():
    global ITEMS1
    ItemDictionary = {}
    for item in ITEMS1:
        name = item.name.lower()
        ItemDictionary.update({name: item})
    return ItemDictionary


def EnemyDictionary():
    global ENEMIES1
    EnemyDictionary = {}
    for enemy in ENEMIES1:
        name = enemy.name.lower()
        EnemyDictionary.update({name: enemy})
    return EnemyDictionary


def InteractDictionary():
    global INTERACT1
    InteractDictionary = {}
    for interact in INTERACT1:
        name = interact.name.lower()
        InteractDictionary.update({name: interact})
    return InteractDictionary
