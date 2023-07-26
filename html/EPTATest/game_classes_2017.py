"""
ENG PHYS TEXT BASED ADVENTURE
Mitchell Lemieux and Tyler Kashak
Wrote on April 14,2018: Icemageddon
Maybe this is dumb but before final update I added 2 extra elements to each class for anticipated future use/compatibility.
"""
import operator
from random import *
from printT import *  # import it all
from Colour import *
try:
    import pickle as pickle
except ImportError:  # python 3.x
    import pickle


# adds 6 tuples element-wise, used to calculate stats of character. If only need n elements added put (0,0,0) for 6-n arguments
def six_tuple_add(a, b, c, d, e, f):
    i = tuple(map(operator.add, a, b))
    j = tuple(map(operator.add, c, d))
    k = tuple(map(operator.add, e, f))
    ij = tuple(map(operator.add, i, j))
    return tuple(map(operator.add, ij, k))


def two_tuple_add(a, b):  # adds 2 tuples element-wise
    return tuple(map(operator.add, a, b))


# WHEN UPDATING ANY CLASS ATRIBUTE WILL NEED TO UPDATE IN CSVSaver to Reflect it!
#       Unless someone does something fancy to automatically update it but I don't feel it's necessary.

class Equipment:
    def __init__(self, name, location, image, info, worn, stats, health):
        self.name = str(name)
        self.colouredname = "" + itemcolour + name + textcolour + ""
        # This is an obsolete field from when the game was going to have pictures
        self.image = str(image)
        self.info = str(info)  # This is the base description that is read
        self.worn = str(worn)  # Which inventory slot the item_object takes up
        # These are the stats the item_object gives you that adds to the base stats
        self.stats = stats
        self.location = location
        # this is a health into for healed amount for eating. If no eating it should be a ""
        self.health = health
        self.quest = False  # This is a inspected flag if it's been picked up or inspected


class Character:
    def __init__(self, name, location, health, inv, emptyinv):
        self.name = str(name)
        self.colouredname = "" + personcolour + name + textcolour + ""
        self.location = location
        self.inv = inv
        self.emptyinv = emptyinv
        self.health = health
        self.maxhealth = 100
        self.basestats = [0, 0, 0]
        self.stats = six_tuple_add(self.inv['head'].stats, self.inv['body'].stats, self.inv['hand'].stats, self.inv['off-hand'].stats, tuple(
            self.basestats), (0, 0, 0))  # adds tuples together to new stats to make actual stats
        self.alive = True
        self.spoke = False  # What is this used for?

        for i in inv:
            inv[i].location = self.location

    def update_stats(self):  # updates stats based on changing equipment
        self.stats = six_tuple_add(self.inv['head'].stats, self.inv['body'].stats,
                                   self.inv['hand'].stats, self.inv['off-hand'].stats, tuple(self.basestats), (0, 0, 0))

    def equip_object(self, item_string, MAPS, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
        x = self.location[0]
        y = self.location[1]
        z = self.location[2]
        dim = self.location[3]
        place = MAPS[x][y][z][dim]
        # if name of item_string asked for in parser is in ITEMS dictionary
        if item_string in ITEMS and list(ITEMS[item_string].location) == self.location:

            # this is different than the equip method in the Character class for some reason
            # Makes sure the item_object is dropped at the current location
            # TODO Redo this drop and equip structure. Is dumb and can cause duplicates/ghosting

            equip_item_object = ITEMS[item_string]
            drop = 0
            # You're already wearing the thing
            if self.inv[equip_item_object.worn] == equip_item_object:
                printT(" (\S)You realize this you already have a " + equip_item_object.colouredname +
                       " on you. It's okay, we all have tough days. (\S)", 72, 0.25)

            # if your inventory is empty
            elif (self.location == list(equip_item_object.location) and self.inv[equip_item_object.worn] ==
                  self.emptyinv[equip_item_object.worn]):
                self.inv[equip_item_object.worn] = equip_item_object
                equip_item_object.location = self.location
                printT(" (\S)" + equip_item_object.info + " (\S)", 72, 0.25)
                printT(
                    "You've equipped the " + equip_item_object.colouredname +
                    ' to your ' + equip_item_object.worn + ".",
                    72, 0.25)
            # If you have something on you that you're replacing
            elif (self.location == list(equip_item_object.location)):
                drop = self.inv[equip_item_object.worn]
                self.inv[equip_item_object.worn] = equip_item_object
                equip_item_object.location = self.location
                printT(" (\S)" + equip_item_object.info + " (\S)")
                printT("You've equipped the " + equip_item_object.colouredname + ' to your ' +
                       equip_item_object.worn + ', the ' + drop.colouredname + ' has been dropped.')
            else:
                printT(
                    " (\S)You can't find a " + equip_item_object.colouredname + " around here. Maybe it's your hungover brain.")
            self.update_stats()

            # removes that item_object from the invoirnment
            place.remove_item(ITEMS[item_string])
            # places the drop if there's something to drop
            place.place_item(drop)
            ITEMS[item_string].quest = True  # quest/inspect flag is true

        # other acceptations for weird requests
        # Interacts
        elif item_string in INTERACT and list(INTERACT[item_string].location) == self.location:
            printT("Maybe if you were at your peak you could carry a " +
                   str(INTERACT[item_string].colouredname) + " but not with this migraine.")
        # People
        elif item_string in ENEMIES and list(ENEMIES[item_string].location) == self.location and ENEMIES[item_string].alive:
            printT("You attempt to pick up " + ENEMIES[item_string].colouredname +
                   " but you're not that close... (\S)And now you're both really uncomfortable.")
        # Dead People
        elif item_string in ENEMIES and list(ENEMIES[item_string].location) == self.location and not ENEMIES[item_string].alive:
            printT("That's pretty messed up. You probably shouldn't pick up " +
                   deadpersoncolour + ENEMIES[item_string].name + textcolour + "'s dead body.")
        else:
            printT(" (\S)You can't find a " + itemcolour + item_string +
                   textcolour + " around here. Maybe it's your hungover brain.")

        # returning the game state
        return MAPS, self, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    # Equip is an object not a name

    def drop_object(self, item_string, MAPS, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
        x = self.location[0]
        y = self.location[1]
        z = self.location[2]
        dim = self.location[3]
        Place = MAPS[x][y][z][dim]
        if item_string in ITEMS and list(ITEMS[item_string].location) == self.location:
            drop_item_object = ITEMS[item_string]
            if (drop_item_object.name == self.inv[drop_item_object.worn].name):
                self.inv[drop_item_object.worn] = self.emptyinv[drop_item_object.worn]
                printT(" (\S)You've dropped the " +
                       drop_item_object.colouredname + ".")
                # places the drop on the ground
                Place.place_item(drop_item_object)
            else:
                printT("Maybe you're still drunk?. You aren't carrying " +
                       drop_item_object.colouredname + ".")
            self.update_stats()

        # other acceptations for weird requests
        # Interacts
        elif item_string in INTERACT and list(INTERACT[item_string].location) == self.location:
            printT("You probably shouldn't drop the " +
                   str(INTERACT[item_string].colouredname) + ". Something might break.")
        # People
        elif item_string in ENEMIES and list(ENEMIES[item_string].location) == self.location and ENEMIES[item_string].alive:
            printT("You drop " + ENEMIES[item_string].colouredname +
                   " but they were never yours, to begin with. (\S)Now you just have one less friend...")
        # Dead People
        elif item_string in ENEMIES and list(ENEMIES[item_string].location) == self.location and not ENEMIES[item_string].alive:
            printT("You pick up " + deadpersoncolour +
                   ENEMIES[item_string].name + textcolour + "'s body and drop it. Do you get a kick out of this?")
        else:
            printT("Maybe you're still drunk?. You aren't carrying a " +
                   itemcolour + item_string + textcolour + ".")

        # returning the game state
        return MAPS, self, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    def show_inventory(self):  # User display

        Head = "head\t\t"+self.inv['head'].name + \
            "\t"+str(self.inv['head'].stats)+"\n"
        Body = "body\t\t"+self.inv['body'].name + \
            "\t"+str(self.inv['body'].stats)+"\n"
        Hand = "hand\t\t"+self.inv['hand'].name + \
            "\t"+str(self.inv['hand'].stats)+"\n"
        OffHand = "off-hand\t" + \
            self.inv['off-hand'].name+"\t"+str(self.inv['off-hand'].stats)+"\n"
        printT("INVENTORY: (\S)" + Head + Body + Hand + OffHand)

    def show_attributes(self):  # Devmode display showing the stats
        print("name: " + str(self.name))
        print("location: " + str(self.location))
        self.show_inventory()
        print("emptyinv: " + str(self.emptyinv))
        print("health: " + str(self.health))
        print("maxhealth: " + str(self.maxhealth))
        print("basestats: " + str(self.basestats))
        print("stats: " + str(self.stats))
        print("alive: " + str(self.alive))
        print("spoke: " + str(self.spoke))


# TODO Switch order of drop and need AND sinfo for defining to be consistant with interacts
class Enemy:
    def __init__(self, name, info, location, stats, health, drop, need, Sinfo, Dinfo, aesthetic):
        self.name = str(name)
        self.colouredname = "" + personcolour + name + textcolour + ""
        self.info = str(info)
        self.location = location
        self.stats = stats
        self.health = health
        self.Sinfo = Sinfo  # special info displayed if you give them what they need
        self.Dinfo = Dinfo  # death info displayed if they need
        self.need = need  # what the need, if you talk to them with this item_object you'll get the drop and it will set the quest flag to True
        self.drop = drop
        # If the enemy is not for anything aesthetic = True for a couple diff. uses
        self.aesthetic = aesthetic
        self.alive = True
        self.quest = False
        self.spoke = False


class Animal(Enemy):  # this is an inhertance of enemy class. NICE.
    # Constructor
    def __init__(self, name, info, location, stats, health, drop, need, Sinfo, Dinfo, pinfo, aesthetic):
        self.pinfo = pinfo

        # invoking the __init__ of the parent class
        Enemy.__init__(self, name, info, location, stats,
                       health, drop, need, Sinfo, Dinfo, aesthetic)

        # printT(self.name  # can totally do commands in the init)

    # Methods
    def pet_me(self):
        return self.pinfo


class Interact:
    def __init__(self, name, location, info, Sinfo, need, drop, aesthetic):
        self.name = name
        self.colouredname = "" + interactcolour + name + textcolour + ""
        self.location = location
        self.info = info
        self.Sinfo = Sinfo
        self.need = need
        self.drop = drop
        self.quest = False
        # If the enemy is not for anything aesthetic = True for a couple diff uses
        self.aesthetic = aesthetic

    # this is a general method to drop objects
    def drop_objects(self, Item, x, y, z, dim, MAPS, ITEMS, INTERACT, ENEMIES):
        # THIS PARSING ONLY Works if all item_object keys are unique
        # if it's an ITEM (in the item_object keys)
        if INTERACT[Item].drop in list(ITEMS.keys()):
            MAPS[x][y][z][dim].place_item(ITEMS[INTERACT[Item].drop])
            printT("You see " +
                   ITEMS[INTERACT[Item].drop].colouredname + ". (\S)")
        # if it's an enemy_object
        elif INTERACT[Item].drop in list(ENEMIES.keys()):
            MAPS[x][y][z][dim].place_enemy(ENEMIES[INTERACT[Item].drop])
            printT("You see " +
                   ENEMIES[INTERACT[Item].drop].colouredname + ". (\S)")
        # if it's an Interactable
        elif INTERACT[Item].drop in list(INTERACT.keys()):
            MAPS[x][y][z][dim].place_interact(INTERACT[INTERACT[Item].drop])
            printT("You see " +
                   INTERACT[INTERACT[Item].drop].colouredname + ". (\S)")
            # TODO Make this an option maybe so it doesn't have to remove itself
            # If it's an interactable place it's an upgrade/transform
            MAPS[x][y][z][dim].remove_interact(INTERACT[Item])

# TODO GET RID OF location checking in GAMEFUNCTIONS AND location attribute entirely and just use storage lists in each map location
# Should get rid of duplicate problems AND will go better with adjacency lists probably.
# Player list
# Item list
# Interactables list
# Enemies list (rename enemies to NPCs)


class Map:  # Map Location Storage
    # size = (None) means default is none object unless otherwise defined
    def __init__(self, name, location, info, lore, walls, inside, size=None, links=[]):
        self.name = str(name)       # Name of location
        self.colouredname = "" + mapcolour + name + textcolour + ""
        # Dim is the dimension/ building number associated with the place, by default Overworld is 0, Bsb is 1, etc
        # Map coordinates tuple (X,Y,Z,Dim) TODO Make make ground level 0 and basements -1
        self.location = location
        # A more detailed description of the suroundings than the search function
        self.info = str(info)
        # A monologue of the area and what you do when you get there
        self.lore = str(lore)
        self.items = []  # list of equipment objects at that location
        self.ENEMY = []  # list of enermy objects at that location
        self.walls = walls
        # This defines if you've been there before TODO Name should be changed to untravlled
        self.travelled = 1
        # Boolean that says if it's indoors for interriors and seeing the time
        self.inside = inside
        self.mapped = 0  # TODO make consistent flag convention for 0 as default and 1 as activated
        # TODO Interriors rewarding at end
        # There is probably a better way to do this building stuff, maybe having an inherited ininterior class
        #   BUT This is what I'm going with!
        # size of interior (xRange,yRange, zRange). This tuple also flags it has/is an interior
        self.size = size
        # When you go into the building from the side it enters the doorway on that size
        # If there's not doors on all sides have exterior outer area with links down (see diagram)
        # This is a list containing tuple coordinate pointers (direction, X, Y, Z, Building)
        self.links = links
        # for doorways and Portals. A link will activate when moving the specified direction out of that space
        # ex) BSBDoor.links = [("l",2,4,1,0)], if exiting BSB player moves left to (3,3,3) in Overworld (building 0)
        # More complicated example would have multiple links depending on the direction. This creates a distorted spaces
        # ex) BSBLawn.links = [("f",0,6,0,1),("l",2,4,1,0), ("b",0,0,0,1)] this means depending on where the player
        #   moves they will will go to a different spot on the interior (so you don't have to step around BSB) or JHE
        # Walls can be used to close and open links as they won't let the player move into it and are mutable
        # Using tuples here because they're faster but if want to be changed can use nested lists (mutable)

        # self.interrior = interrior #interrior is a list of inner map objects (so infinite nesting)
        # self.exits = exits #pairs of coordinates coresponding to interrior entrance/exit and their coresponding exterirrior exits/entrances

        # OR Make another coordinate d, dimension to specify interriors, but I'm leaning away from this
        #   although it would look cleaner on a spreadsheet

    # the item_object object, works with the drop method in the character class
    def place_item(self, item_object):
        if item_object:
            self.items.append(item_object)
            item_object.location = self.location

    def place_enemy(self, enemy_object):
        self.ENEMY.append(enemy_object)
        enemy_object.location = self.location

    def place_interact(self, interact_object):
        if interact_object:
            self.items.append(interact_object)
            interact_object.location = self.location

    # this is used to remove walls of rooms given the wall. WALLS have to be a lisst not a tuple to be mutable
    def remove_wall(self, wall_string):
        if wall_string in self.walls:
            # removes the wall from the list. wall attribute is direction it's blocking such as 'l'. HOWEVER The walls have to be in square [] not circle brackets () so its a list instead of a tuple. Lists are mutable, tuples are not
            self.walls.remove(wall_string)

    # had to be rewritted with load or else load function would create duplciate glitch
    def remove_item(self, item_object):
        for i in self.items:  # weird way to write it but loops through the items in that lcoation and if the name matches it removes it
            if i.name == item_object.name:
                self.items.remove(i)

    def remove_enemy(self, enemy_object):
        if enemy_object in self.ENEMY:
            self.ENEMY.remove(enemy_object)
            # removes the enemy location so they can't be talked to. Has to be a tuple of Nones or else not itterable in compares
            enemy_object.location = (None, None, None, None)

    # had to be rewritted with load or else load function would create duplciate glitch
    def remove_interact(self, interact_object):
        for i in self.items:  # weird way to write it but loops through the items in that lcoation and if the name matches it removes it
            if i.name == interact_object.name:
                self.items.remove(i)

    # This method that displays what's in the area.
    # Is passed MAPS dictionary so it can search area around it
    def search(self, MAPS, DIMENSIONS, GAMESETTINGS, Spawn=False):
        # also test the displays of things. [People], ~Places~, <Things>, /Interactables/ (put these next to descriptions)

        # this is the printout if you wake up in a location (say for example a load)
        if Spawn:
            printT("You wake up in " + self.colouredname + ". (\S)")
            printT(self.lore)
        elif self.travelled:
            printT("You enter " + self.colouredname + ". (\S)")
            printT(self.lore)

        description = ""  # the main text description accumulator

        # setting the title
        description += " (\S)" + mapcolour + "~" + \
            self.name.upper() + "~" + textcolour + " (\S)"

        length = len(self.items)
        # (\S) used for printT newline
        # Initialize the {shortkey} used with object,interact,enemy for quick commands.
        # Disabling shortkey printing for now but still exists in the game
        # shortkey = 5  # Starts at 5 because 1-4 are reserved for inventory quick commands
        shortkey = ""
        # This big if statement basically does a printout to account for single object/enemy in the area grammer
        if length:
            description += "You see"
            if length > 1:  # If there's more than one item_object/interact in the area
                for i in range(length):
                    if (i == length-1):
                        if isinstance(self.items[i], Equipment):
                            # item_object highlight, checks to see if object is of class equipment and if not it's an interactable
                            description = description + textcolour+" and a " + \
                                str(shortkey) + "" + "" + \
                                self.items[i].colouredname + "" + ".\n"
                            # shortkey += 1  # increments the shortkey
                        else:
                            description = description + textcolour+" and a " + \
                                str(shortkey) + "" + "" + \
                                self.items[i].colouredname + "" + \
                                ".\n"  # inspectable highlight
                            # shortkey += 1  # increments the shortkey
                    else:
                        if isinstance(self.items[i], Equipment):
                            description = description + textcolour + " a " + \
                                str(shortkey) + "" + "" + \
                                self.items[i].colouredname + "" + ","
                            # shortkey += 1  # increments the shortkey
                        else:
                            description = description + textcolour + " a " + \
                                str(shortkey) + "" + "" + \
                                self.items[i].colouredname + "" + ","
                            # shortkey += 1  # increments the shortkey
            else:  # if there's only 1 item_object/interact in the area
                if isinstance(self.items[0], Equipment):
                    description = description + textcolour + " a " + \
                        str(shortkey) + "" + "" + \
                        self.items[0].colouredname + "" + \
                        ".\n"  # equipment highlight
                    # shortkey += 1  # increments the shortkey
                else:
                    description = description + textcolour + " a " + \
                        str(shortkey) + "" + "" + \
                        self.items[0].colouredname + "" + \
                        ".\n"  # inspectable highlight
                    # shortkey += 1  # increments the shortkey

        if self.ENEMY:
            for enemy in self.ENEMY:
                # if enermy is in JHE lobby they are playing eng phys text adventure lol (including yourself)
                if enemy.alive and enemy.location == (2, 4, 1, 0):
                    description = description + textcolour + \
                        " (\S)" + str(shortkey) + "" + "" + enemy.colouredname + "" + \
                        " is playing the Eng Phys Text Based Adventure. WAIT What!?"
                    # shortkey += 1  # increments the shortkey
                elif enemy.alive:
                    description = description + textcolour + " (\S)" + str(shortkey) + "" + "" + enemy.colouredname + "" + " is " \
                        + choice(["standing in the corner", "wandering around", "reading a book", "creating a grand unified field theory",
                                  "eating a frighteningly large burrito", "playing RuneScape", "browsing math memes",
                                  "taking a hit from a laser bong", "laying down crying", "watching the Big Lez show on full volume",
                                  "eating a Big Mac", "eating too much Lava Pizza", "contemplating how much Mayo is too much",
                                  "bathing in Mayonnaise", "in a sushi coma", "phasing in and out of this dimension", "drinking spicy Pho broth",
                                  "reading a book under a tree", "wondering how you can read their thoughts?", "playing 4D chess",
                                  "pondering necromancy", "unsuccessfully painting their Warhammer 40k miniature with milli",
                                  "Synthesizing Gold Nanoparticles", "creating an AI Dog", "petting a cat", "carrying a soccer ball",
                                  "playing football by themself", "balancing a tennis racket on their nose", "digging down in Minecraft",
                                  "catching a shiny Pikachu", "checking their Hearthstone Bot", "solving time travel", "watching Gilmore Girls",
                                  "computing the eigenvalue of the inverse Mobius strip", "watching Little House on the Prairie",
                                  "getting shot by an auto-turret in Rust", "trying to think of a capstone idea", "being watched", "taking 3 mayo jars"]) + "."
                    # shortkey += 1  # increments the shortkey

                else:
                    description = description + textcolour + "(\S)Oh look, its the " \
                        + choice(["decaying ", "broken ", "bloodied ", "mutilated ", "scrambled ", "soulless ", "degraded ", "decrepit ", "blank empty stare of the ", "mouldy "]) \
                        + choice(["corpse of ", "body of ", "cadaver of ", "hunk of meat that used to be ", "remains of ", "chalk outline of ", "snack that used to be "]) \
                        + "" + str(shortkey) + "" + deadpersoncolour + \
                        "" + enemy.name + "" + textcolour + "."
                    # shortkey += 1  # increments the shortkey

        # if self.interact:
        #     for item_object in self.interact:
        #         description = description + "/" + item_object.info + "/\n"

        if not self.ENEMY and not self.items:  # if there's nothing in the location
            description += textcolour + " (\S)There isn't a whole lot to see."

        # if in hardcore mode it skips the auto descriptions
        if GAMESETTINGS['HardcoreMode']:
            pass
        else:
            # --- Auto Surrounding Descriptions ---
            # -- Finding the locations around current location --
            location = self.location  # gets coordinates tuple
            # letter based list of directions to check against walls
            letterdirections = ['u', 'd', 'f', 'b', 'l', 'r']
            lettersthere = ""
            # tuple based list of directions to add to current location
            tupledirections = [(0, 0, 1, 0), (0, 0, -1, 0), (0, 1, 0, 0),
                               (0, -1, 0, 0), (-1, 0, 0, 0), (1, 0, 0, 0)]
            # Name storage, defaulted to none. Order of: Left, right, Front, Back, Up, Down
            surroundings = [""] * 6
            i = 0  # Counter for direction indexing
            for direction in letterdirections:  # Looping through all the directions
                if direction not in self.walls:  # seeing if the way you can go is in the walls
                    # Gets tuple of requested adjacent spot by adding the direction in the right order
                    dx, dy, dz, dim = tuple(
                        map(operator.add, location, tupledirections[i]))
                    if MAPS[dx][dy][dz][dim]:  # if the map location exists
                        # store the name into the surroundings variable
                        surroundings[i] = MAPS[dx][dy][dz][dim].name
                        lettersthere += direction + ","
                i += 1

                # - Finding Interriors Via Links -
            if self.links:  # if there's a link and therefore it links to an interrior
                for link in self.links:  # loping through all links
                    if link[4] != self.location[3]:
                        # if you're not in the same dimension as the linked dimension displays the dimension name
                        surroundings[letterdirections.index(
                            link[0])] = DIMENSIONS[link[4]]
                        lettersthere += link[0] + ","
                    else:
                        # this magic line replaces the surrounding name with the link name of the area
                        surroundings[letterdirections.index(
                            link[0])] = MAPS[link[1]][link[2]][link[3]][link[4]].name
                        lettersthere += link[0] + ","

                # -- Reading out the Surroundings --
            # TODO Add discovery mechanic where it prints locations as you see them
                    # - Short Description -
            worddirections = ['[U] ', '[D] ', '[F] ', '[B] ', '[L] ', '[R] ']
            description += "(\S) (\S)There are " + str(6 -
                                                       surroundings.count("")) + " obvious exits: (\S)"
            # old description having letters in there
            #description += "(\S) (\S)There are " + str(6 - surroundings.count(None)) + " obvious exits: " + lettersthere + "(\S)"

            # TODO for even shorter/harder list only directions
            # - Aligning the Words by adding spaces -
            maxnamelength = max(len(x) for x in surroundings)
            for i in range(6):  # Equalization of the spacing to the max spacing
                surroundings[i] = surroundings[i] + " " * \
                    (maxnamelength - len(surroundings[i]))

            for i in range(6):  # use index to reference direction
                # if the direction is seen in there and it's not empty
                if surroundings[i].strip():
                    # print the word direction + name
                    description += worddirections[i] + mapcolour + \
                        surroundings[i] + textcolour + "\t"
                # if there's no U but D
                if worddirections[i] == '[U] ' and not surroundings[i].strip() and surroundings[i+1].strip():
                    # adding correct spacing
                    description += "[U] " + " "*(maxnamelength) + "\t"
                # if there's U but no D
                elif worddirections[i] == '[U] ' and surroundings[i].strip() and not surroundings[i+1].strip():
                    description += "[D]  (\S) "  # adding newline
                # if there's no F but B
                if worddirections[i] == '[F] ' and not surroundings[i].strip() and surroundings[i+1].strip():
                    # adding correct spacing
                    description += "[F] "+" "*(maxnamelength) + "\t"
                # if there's F but no B
                elif worddirections[i] == '[F] ' and surroundings[i].strip() and not surroundings[i+1].strip():
                    description += "[B]  (\S) "  # adding newline
                # if there's no L but R
                if (worddirections[i] == '[L] ') and (not surroundings[i].strip()) and surroundings[i+1].strip():
                    # Makes a hidden peroid there so spacing is correct because I'm a monkey and can't figure it out what's wrong
                    # description += Style.DIM+backcolour+ "." +Style.RESET_ALL+textcolour+ " "  # I DON"T KNOW WHY THIS WORKS BUT ITS 2:21 AM DAY OF RELEASE SO WERE GOIN WITH IT
                    # adding correct spacing
                    description += "[L] "+" "*(maxnamelength) + "\t"
                # if there's L but no R
                elif worddirections[i] == '[L] ' and surroundings[i].strip() and not surroundings[i+1].strip():
                    description += "[R]  (\S) "  # adding newline
                # If there's all spaces
                elif worddirections[i] in ['[D] ', '[B] '] and surroundings[i].strip():
                    description += " (\S) "

                    # TODO Add wordy description

        if self.travelled:  # if haven't been here before
            printT(description, 72, 0.75)  # prints the final descripton
            self.travelled = 0
        else:  # normal fast print
            printT(description, 72, 0)  # prints final description fast

        # Don't need to return the 'Global' objects from function as affecting scope outside the function


# The pickler needs to be in the same level as the defined classes

def pickle_game(DATA, savegamepath):

    with open(savegamepath, 'wb') as fp:
        pickle.dump(DATA, fp, protocol=pickle.HIGHEST_PROTOCOL)

    return


def unpickle_game(loadgamepath):

    with open(loadgamepath, 'rb') as fp:
        DATA = pickle.load(fp)

    return DATA
