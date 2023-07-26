# ENG PHYS TEXT  ADVENTURE
# Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
# First written on Mar  21,2019 by Brendan Fallon:
"""
This game_scripts_2017.py file is used to write the story, quests, and events of the game by changing objects based on conditions.
EngPhysStory() is the main Eng Phys storyline  and returns once its finished
Quests generally only happen once and are sidequests unrelated to the storyline that do something special
Events are reoccurring based on the condition for the game.
    This also includes PORTALS which is teliportation using interacts
"""


# importing the global dictionaries/values, do we need this? or can we just import gameclasses?
from GameFunctions import *
import time
# import os  # used to put files in the cache folder and locate audio files
import AsciiArt
from Colour import *
from printT import *
# import playsound

global QUESTS

# List of quests and storylines that then get's built into a dictionary
# This dictionary is just flags to keep track of quest completion to advance or end quests
# it's defined here for convience of working but is dealing with a global variable defined in gamefunctions

questlist = [
    # sidequests
    'secret spaces',
    'rules sign',
    'EPTA all the way down',
    'national treasure',
    'open the trees',
    'open the cabin',
    'open the forest',
    'power of the forest',
    # Events
    'completionist',
    'kill brendan fallon',
    'PAP',
    # Talk to hooded man
    "talk to devan",
    "talk to mysterious man",
    # Nuke
    "preston get dumbbell",
    "buijs kill chris",
    "dan fix reactor",
    "novog get donut",
    "feynman mirror",
    # Optics
    "kitai get silicon substrate",
    "knights get book",
    "haugen kill soleymani",
    "einstein fridge",
    # Semiconductor
    "lapierre get coffee",
    "kleimann get solar cell",
    "minnick get oscilloscope",
    "get key to display case",
    "maxwell portal",
    # endgame stuff
    'end game start',
    'the dark lord',
    'university man',
    'restored order',
    'create chaos',
    'neutral balance'
    # PHILpocalypse  # After you give Phil is braces he sobers up and becomes tired Phil.
    # After he asks for a coffee "Man I could really use a coffee but I don't want to spend the money
    # if you give him coffee he gives you a free wish "OH YEAH I AM CAFFINATED. I feel like I can do anyhing!"
    # If you give him a cappuccino the PHILpocalypse storyline begins:
    # You see his eyes dilate "OH YEAH I"M FEELING GREAT", He snaps his fingers and there's a flash.
    # You wake in JHE field "Not again" and everyone on the map is gone. Eventually you meet a Phil clone
]

# building the quest dictionary because you can't just overwrite the dumb dictionaries for some dumb reason
for quest in questlist:
    QUESTS.update({quest: 1})


def Opening():  # Scripted openning. Needs to defined before can be called in EPTA all the way down.
    DELAY = 1.5
    # IT WORKS!
    # points to the eddited star wars theme
    # audiopath = os.path.join(os.getcwd(), "MediaAssets",
    #                         "", "StarWarsOpenningFadeOut.mp3")
    # plays the sound with 'multithreading'
    # playsound.playsound(audiopath, False)
    time.sleep(0.5)
    print(CLEARSCREEN)
    print("                " + magenta + "A" + textcolour + "____ ________")
    print("                /_  H|\_____  \ ")
    print("                 |  O|  ___|  |")
    print("                 |  L| /___   <")
    print("                 |  L|  ___\   |")
    print("                 |  Y| /W O O D|")
    print("                 |___|/________/")
    print("                      " + magenta + "Production." + textcolour + "")
    time.sleep(3.5)  # 4 seconds
    print(CLEARSCREEN)
    print("")
    print("         A short time ago on a campus not so far,")
    print("         far away....\n")
    time.sleep(3)  # 5.5 seconds
    print(CLEARSCREEN)
    print()
    print("___________                __________.__")
    print("\_   _____/ " + red + "THE_GREAT" + textcolour +
          "_____ \______   \  |__ ___.__. ______")
    print(" |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/")
    print(" |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ ")
    print("/_______  /___|  /\___  /   |____|   |___|  / ____/____  >")
    print("        \/     \//_____/  " + red +
          "TEXT ADVENTURE" + textcolour + "  \/\/ (v4.20) \/ ")
    time.sleep(7.5)
    print("")
    print("T h e  c a m p u s  i s  i n  a  s t a t e  o f  u n r e s t.")
    time.sleep(DELAY)
    print("A n  " + indicatecolour + "a n c i e n t  f o r c e" +
          textcolour + "  h a s  b e e n  a w o k e n")
    time.sleep(DELAY)
    print("a f t e r  t h e  e v e n t s  o f  a  d e b a u c h e r o u s")
    time.sleep(DELAY)
    print("e v e n i n g  a t  t h e  " + mapcolour +
          "P h o e n i x" + textcolour + ".\n")
    time.sleep(DELAY*2)
    print("T h e  h e r o  a w a k e n s  i n  " +
          mapcolour + "f r o n t  o f  J H E" + textcolour + "")
    time.sleep(DELAY)
    print("w i t h  a  c o n s i d e r a b l e  h e a d a c h e  b u t")
    time.sleep(DELAY)
    print("w i t h o u t  t h e i r  " + itemcolour +
          "I R O N  R I N G" + textcolour + ".\n")
    time.sleep(DELAY*2)
    print("C l u e s  a b o u t  l a s t  n i g h t  l i t t e r  t h e")
    time.sleep(DELAY)
    print("c a m p u s.  N o  s t o n e  c a n  b e  l e f t  u n t u r n e d.")
    time.sleep(DELAY)
    print("I t  w i l l  t r u l y  b e  a  t e s t  o f  s k i l l  a s")
    time.sleep(DELAY)
    print("w e l l  a s  w i t s  t o  s o l v e  t h i s  m y s t e r y.\n")
    time.sleep(DELAY*2)
    print("T h e  h e r o  m u s t  u n c o v e r  t h e  t r u t h")
    time.sleep(DELAY)
    print("a b o u t  l a s t  n i g h t  i f  t h e y  a r e  t o")
    time.sleep(DELAY)
    print("h a v e  a n y  h o p e  o f  r e t r i e v i n g  t h e i r")
    time.sleep(DELAY)
    print("" + itemcolour + "I R O N  R I N G" + textcolour +
          "  a n d  r e t u r n i n g  b a l a n c e")
    time.sleep(DELAY)
    print("t o  t h e  f a c u l t y.\n")
    time.sleep(DELAY)
    # print CLEARSCREEN  #Don't clearscreen at end so people can read!
    # for i in range(14):
    #     print "\n"
    #     time.sleep(DELAY/2)


def Closing():  # Closing Scripted event
    DELAY = 1.5
    print("\nAnd so, the "+wincolour+"fate" + textcolour + " of " +
          mapcolour+"McMaster" + textcolour + " has been decided...")
    time.sleep(DELAY)
    print("Our hero has unlocked the "+wincolour+"secrets" + textcolour +
          " of "+mapcolour+"McMaster University" + textcolour + "")
    time.sleep(DELAY)
    print("and "+wincolour+"lived" + textcolour + " to tell the tale.\n")
    time.sleep(DELAY)
    print("___________                __________.__")
    print("\_   _____/ " + red + "THE_GREAT" + textcolour +
          "_____ \______   \  |__ ___.__. ______")
    print(" |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/")
    print(" |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ ")
    print("/_______  /___|  /\___  /   |____|   |___|  / ____/____  >")
    print("        \/     \//_____/  " + red +
          "TEXT ADVENTURE" + textcolour + "  \/\/ (v4.20) \/ \n")
    time.sleep(DELAY)
    print("Created by:\n"+red+"Brendan Fallon" + textcolour + ", " + white + "Tyler Kashak" +
          textcolour + ", and " + lightblue + "Mitchell Lemieux" + textcolour + ".  \n")
    time.sleep(DELAY)
    printT("" + lightmagenta + "Special Thanks:" + textcolour + "\n" + personcolour + "Erik" + textcolour + " and " + personcolour + "Phil" + textcolour +
           " our best " + indicatecolour + "playtesters" + textcolour + "! There are no " + wincolour + "better quality checkers" + textcolour + " than you guys. (\S)")
    time.sleep(DELAY/2)
    print("Also thanks to Eric, Brian, Liam, and Megan.\n")
    time.sleep(DELAY)
    print("                " + red + "A" + textcolour + "____ ________")
    print("                /_  H|\_____  \ ")
    print("                 |  O|  ___|  |")
    print("                 |  L| /___   <")
    print("                 |  L|  ___\   |")
    print("                 |  Y| /W O O D|")
    print("                 |___|/________/")
    print("                      " + red + "Production." + textcolour + "")
    time.sleep(2)
    printT("This is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are "
           "either the products of the author's imagination or used in a fictitious manner. Any resemblance to actual "
           "persons, living or dead, or actual events is purely coincidental. (\S)", 72, 0)
    time.sleep(DELAY)
    AsciiArt.ThanksForPlaying()
    time.sleep(DELAY)


def sidequests(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item_object.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class interact_object keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class enemy_object keyed by their lowcase equipment name (item_object.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope

    # --- Side Quests ---
    # -- Secret Spaces --
    # Unlocks the secret space once you get the scroll
    if INTERACT['coat of arms'].quest and QUESTS["secret spaces"]:
        # DON'T FORGET to make wall a list instead of a tuple in the object!
        MAPS[0][2][1][0].remove_wall("d")
        QUESTS["secret spaces"] = 0

    # -- Rules Sign --
    if INTERACT["rules sign"].quest and QUESTS['rules sign']:  # Once the sign is read
        MAPS[2][3][1][0].remove_interact(INTERACT["rules sign"])
        INTERACT["rules sign"].location = (None, None, None, None)
        printT("The sign " + indicatecolour + "disappears" + textcolour + " in a flash of " +
               indicatecolour + "smoke" + textcolour + ". You look around. Are you still dreaming?")
        QUESTS["rules sign"] = 0

    # -- EBTA All the way Down --
    # when you put the pen in the laptop it opens the thing
    if INTERACT["lenovo laptop"].quest and QUESTS['EPTA all the way down']:
        # TODO as homework see if there's a way to do this with recursion instead of simulating it
        # Would put drums if there was sound effect
        playgame = input(
            '========================================================================\nWould you like to play? \n').lower()
        if playgame == "yes" or playgame == "y":
            printT("You click on the game and it begins in the terminal. The " + red +
                   "drumming intensifies" + textcolour + ". You're not sure if you made the right choice.")
            printT(
                "======================================================================== (\S) (\S)")
            # this is imported here not at the top to avoid recursive import errors (show up as global names not being defined in the compiler)
            import CreativeMode
            # Truns off the quest, has to be before the game saves so the quest is ended when you come back
            QUESTS['EPTA all the way down'] = 0
            # saving game to be reloaded after death or won the game
            save_game(str(GAMEINFO['layersdeep']))
            # keeps the log as a temporary variable to keep a running log in the nested game
            log = GAMEINFO['log']
            Opening()
            newplayername = input("First, what is your name?\n")
            # saves layersdeep to a temporary variable for after the load
            layers = GAMEINFO['layersdeep']
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game(
                "basegame")  # should display the exact start
            # increments the global layers deep because you're now in a lower level, using the memory of the local variable
            GAMEINFO['layersdeep'] = layers + 1

            # this is done for the log
            GAMEINFO['playername'] = PLAYER.name = newplayername
            # Settign the game and timestart for for this layer
            GAMEINFO['gamestart'] = time.time()
            GAMEINFO['timestart'] = GAMEINFO['gamestart']
            # Passes the log and adds onto it to keep a HUGE running log (TODO Make this more effecient with log appending)
            GAMEINFO['log'] = log + [str(playgame), "--NESTED GAME--", GAMEINFO['layersdeep'], GAMEINFO['versionname'],
                                     GAMEINFO['playername'], time.ctime(
                                         GAMEINFO['timestart']),
                                     "--LOG START--"]  # log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
        elif playgame == "no" or playgame == "n":
            printT("You " + indicatecolour + "decide against it" + textcolour + ", fearing the worst. You safely edject the pen, drop it on the floor, and " +
                   red + "smash" + textcolour + " it to pieces. Better safe than sorry. (\S)" + lightblue + "The drumming stops" + textcolour + ".)")
            printT(
                "========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log
        else:
            printT("" + losecolour + "It was a yes or no question" + textcolour + ". When you look back the files are " +
                   losecolour + "gone" + textcolour + ". (\S)Even the FlexPDE code. Good riddance.")
            printT(
                "========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log

    # National Treasure
    if INTERACT["tri-coloured glasses"].quest and QUESTS['national treasure']:  # Once the sign is read
        # DON'T FORGET to make wall a list instead of a tuple in the object!
        MAPS[1][0][1][0].remove_wall("u")
        QUESTS["national treasure"] = 0

    if INTERACT["red book"].quest and QUESTS['open the trees']:  # Once the sign is read
        printT("You feel like you've " + indicatecolour +
               "gained" + textcolour + " some knowledge!")
        MAPS[3][7][1][0].remove_interact(INTERACT['gap in the trees'])
        INTERACT['gap in the trees'].location = (None, None, None, None)
        INTERACT['gap in the trees'].location = None
        MAPS[3][7][1][0].place_interact(INTERACT['opening in the trees'])
        INTERACT['opening in the trees'].location = (3, 7, 1, 0)
        QUESTS['open the trees'] = 0
        # return INTERACT,MAPS  # don't need to return this scope because reasons?

    if INTERACT["lit firepit"].quest and QUESTS['open the cabin']:
        # DON'T FORGET to make wall a list instead of a tuple in the object!
        MAPS[8][9][0][4].remove_wall("r")
        QUESTS['open the cabin'] = 0

    if INTERACT['gate of the forest'].quest and QUESTS['open the forest']:
        # DON'T FORGET to make wall a list instead of a tuple in the object!
        MAPS[0][7][0][4].remove_wall("b")
        QUESTS['open the forest'] = 0

    if INTERACT['stone pedestal'].quest and QUESTS['power of the forest']:
        PLAYER.maxhealth = 200
        PLAYER.health = 200
        PLAYER.basestats = [100, 100, 100]
        PLAYER.update_stats()
        printT(" (\S) (\S)You see a " + indicatecolour + "flash of light" +
               textcolour + " and " + wincolour + "feel stronger" + textcolour + ".")
        AsciiArt.HauntedForest()
        QUESTS['power of the forest'] = 0

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def story(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item_object.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class interact_object keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class enemy_object keyed by their lowcase equipment name (item_object.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope

    # Talk to devan
    if ENEMIES["devan the most unhelpful"].spoke and QUESTS["talk to devan"]:
        # removes him from infront of hatch
        MAPS[1][3][1][0].remove_enemy(ENEMIES["devan the most unhelpful"])
        ENEMIES["devan the most unhelpful"].location = (2, 4, 0, 0)
        MAPS[2][4][0][0].place_enemy(ENEMIES["devan the most unhelpful"])
        ENEMIES["devan the most unhelpful"].info = "We can talk in here. I've heard about you seeking your " + itemcolour + "iron ring" + textcolour + ". Turns out this thing goes deeper than I could have imagined, way deeper. It seems last night you got really drunk at the " + \
            mapcolour + "Phoenix" + textcolour + \
            " and did something to piss off somebody very bad. I'd say if you're trying to get your ring, you should start there."
        ENEMIES["devan the most unhelpful"].spoke = False
        QUESTS["talk to devan"] = 0

    # Talk to hooded man
    if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
        MAPS[4][4][1][0].place_enemy(ENEMIES["dr. kitai"])
        MAPS[2][4][2][0].place_enemy(ENEMIES["dr. preston"])
        MAPS[1][6][2][0].place_enemy(ENEMIES["dr. lapierre"])
        MAPS[5][4][1][0].remove_enemy(ENEMIES["hooded man"])
        # the location should be set to none but for some reason it's fine
        ENEMIES["hooded man"].location = (None, None, None, None)
        ENEMIES['hooded man'].spoke = False
        QUESTS["talk to mysterious man"] = 0

    # Nuke quests
    if ENEMIES['dr. preston'].quest and QUESTS["preston get dumbbell"]:
        MAPS[2][5][1][0].place_enemy(ENEMIES["dr. buijs"])
        QUESTS["preston get dumbbell"] = 0

    if ENEMIES['dr. buijs'].quest and QUESTS['buijs kill chris']:
        MAPS[2][5][0][0].place_enemy(ENEMIES['dan fitzgreen'])
        ENEMIES['dan fitzgreen'].quest = True
        QUESTS['buijs kill chris'] = 0

    if INTERACT['broken reactor'].quest and QUESTS["dan fix reactor"]:
        MAPS[2][6][0][0].place_enemy(ENEMIES['dr. novog'])
        MAPS[4][5][0][0].place_enemy(ENEMIES['stefan boltzmann'])
        QUESTS["dan fix reactor"] = 0

    if ENEMIES['dr. novog'].quest and QUESTS["novog get donut"]:
        QUESTS['novog get donut'] = 0

    if INTERACT['ancient mirror'].quest and QUESTS["feynman mirror"]:
        QUESTS["feynman mirror"] = 0

    # Optics quests
    if ENEMIES['dr. lapierre'].quest and QUESTS["lapierre get coffee"]:
        MAPS[5][4][1][0].place_enemy(ENEMIES['dr. knights'])
        QUESTS["lapierre get coffee"] = 0

    if ENEMIES['dr. knights'].quest and QUESTS["knights get book"] and ITEMS["3w textbook"].location == (3, 4, 0, 0):
        MAPS[1][6][0][0].place_enemy(ENEMIES['dr. haugen'])
        QUESTS["knights get book"] = 0

    if ENEMIES['dr. haugen'].quest and QUESTS['haugen kill soleymani']:
        QUESTS['haugen kill soleymani'] = 0
        ENEMIES['dr. haugen'].alive = False
        MAPS[1][6][0][0].remove_enemy(ENEMIES['dr. haugen'])
        ENEMIES['dr. haugen'].location = (None, None, None, None)
        MAPS[1][6][0][0].place_item(ITEMS["haugen's clothes"])

    if INTERACT['fridge'].quest and QUESTS['einstein fridge']:
        QUESTS['einstein fridge'] = 0

    # Semiconductor quests
    if ENEMIES['dr. kitai'].quest and QUESTS['kitai get silicon substrate']:
        MAPS[1][5][2][0].place_enemy(ENEMIES['dr. kleimann'])
        QUESTS['kitai get silicon substrate'] = 0

    if ENEMIES['dr. kleimann'].quest and QUESTS["kleimann get solar cell"]:
        MAPS[3][4][1][0].place_enemy(ENEMIES['dr. minnick'])
        QUESTS["kleimann get solar cell"] = 0

    # Minnick's Glasses activate the need quest in all further items. So quest is driven by interacts from here
    if ENEMIES['dr. minnick'].quest and QUESTS["minnick get oscilloscope"]:
        # DON'T FORGET to make wall a list instead of a tuple in the object!
        MAPS[6][1][1][0].remove_wall("d")
        ENEMIES['dr. minnick'].quest = False
        # this has to be lowercase or it throws a key error - All items are defined as lower case when stored
        ENEMIES['dr. minnick'].drop = 'gauss eye'
        # this has to be lowercase or it throws a key error
        ENEMIES['dr. minnick'].need = "faraday's cage"
        ENEMIES['dr. minnick'].info = "I need to complete " + deadpersoncolour+"Kenrick's" + \
            textcolour+" design... use my "+itemcolour + \
            "glasses "+textcolour+"to find what we need!"
        ENEMIES['dr. minnick'].Sinfo = "'" + indicatecolour + "Great" + textcolour + "! Now we can open the window to the " + mapcolour + "electronics world" + textcolour + "!'\nYou step back and watch as " + personcolour + "Dr. Minnick" + textcolour + " adds " + itemcolour+"Faraday's Cage "+textcolour+"to the " + itemcolour + "oscilloscope" + textcolour + ".\n'I do not know what this " + personcolour + "oracle" + textcolour + " will have to say.'\n'It is just my responsibility to give you access to their knowledge.'\nYour vision begins to go blurry as you hear a low whirr grow louder and " + itemcolour + "Kenrick's oscilloscope" + red + " glows" + textcolour + \
            " with\nconsiderable intensity!\nYou are shocked as you open your eyes. It seems as if you were dropped into the set of 'Tron'.\nA figure approaches as your vision slowly returns.\nThe figure is revealed to be " + personcolour + "James Clerk Maxwell" + textcolour + "!\n'We have waited many years for your coming.'\n'You will be the one to determine the fate of this faculty.'\n'My " + \
            wincolour+"quantum relic "+textcolour+"along with the two others will give you the power to have your " + itemcolour + "ring" + textcolour + " returned to you.'\n'"+indicatecolour + \
            "Once you have all three you" + textcolour + " will be able to access your " + itemcolour + \
            "ring" + textcolour + " from the "+mapcolour + \
            "statue of McMaster."+textcolour+"'\n'Good luck.'"
        MAPS[3][4][1][0].remove_enemy(ENEMIES['dr. minnick'])
        ENEMIES['dr. minnick'].location = (None, None, None, None)
        MAPS[1][7][0][0].place_enemy(ENEMIES['dr. minnick'])
        QUESTS["minnick get oscilloscope"] = 0

    if INTERACT['display case'] and QUESTS["get key to display case"]:
        QUESTS["get key to display case"] = 0

    if ENEMIES['dr. minnick'].quest and QUESTS["maxwell portal"]:
        QUESTS['maxwell portal'] = 0

    # endgame

    if QUESTS['end game start'] and not (QUESTS["maxwell portal"] or QUESTS['einstein fridge'] or QUESTS["feynman mirror"]):
        MAPS[5][2][1][0].place_enemy(ENEMIES['hooded man'])
        printT(" (\S)You feel a strange " + indicatecolour + "pull" + textcolour +
               " towards the " + mapcolour + "McMaster Statue" + textcolour + ". (\S)")
        MAPS[5][2][1][0].lore = "You approach the " + interactcolour + "statue" + textcolour + " and notice the mysterious "+personcolour+"Hooded Man " + \
            textcolour+"beneath the tree.\nHe notices you approach and stops the incantation he was reciting.\nHe motions for you to come closer to speak."
        MAPS[5][2][1][0].travelled = 1
        ENEMIES['hooded man'].info = "'I knew you could do it.'\n'I knew you were the one the prophecy spoke of.'\n'For too long the " + indicatecolour + "Quantum Order" + textcolour + " has kept me in isolation...'\n'They thought I was poisoning the minds of students and did not agree\nwith my methods.'\n'But now you have brought the " + \
            wincolour+"Quantum Relics "+textcolour+"which will give me the power\nto shape the faculty as I see fit!'\nThe " + personcolour + "Hooded Man" + \
            textcolour + " pulls back his hood to reveal the familiar face you only recall from legend!\nIt is " + \
            personcolour+"Dr. Cassidy himself"+textcolour+"!"
        QUESTS['end game start'] = 0

    if not QUESTS['end game start'] and ENEMIES['hooded man'].spoke and QUESTS['the dark lord']:
        MAPS[5][2][1][0].remove_enemy(ENEMIES['hooded man'])
        ENEMIES['hooded man'].location = (None, None, None, None)
        MAPS[5][2][1][0].place_enemy(ENEMIES['dr. cassidy'])
        QUESTS['the dark lord'] = 0

    if ENEMIES['dr. cassidy'].spoke and QUESTS['university man']:
        MAPS[5][2][1][0].place_enemy(ENEMIES['sir william mcmaster'])
        ENEMIES['dr. cassidy'].info = "Destroy "+personcolour + \
            "Sir William McMaster "+textcolour+"and we can rule this university together!"
        QUESTS['university man'] = 0

    # Neutral Ending, kill both
    if not ENEMIES['dr. cassidy'].alive and not ENEMIES['sir william mcmaster'].alive and QUESTS['neutral balance']:
        PLAYER.alive = False  # does this so you can get out of the main loop
        GAMEINFO['winner'] = 3
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    # # Brian did this
    # booty = 1
    # bitches = 6*9 + 6 + 9
    # big = booty*bitches
    # print str(big)

    if not ENEMIES['sir william mcmaster'].alive and QUESTS['create chaos']:
        ENEMIES['dr. cassidy'].Dinfo = "NO WAIT? WHY? "+personcolour+"Dr. Cassidy "+textcolour+"falls, slain beside "+personcolour + \
            "Sir William McMaster "+textcolour + \
            ". (\S)You see the "+wincolour+"Deed to McMaster" + \
            textcolour+"drop from his pocket."
        ENEMIES['dr. cassidy'].drop = None
        ENEMIES['dr. cassidy'].info = "Take the power you hold in your " + itemcolour + "Iron Ring" + textcolour + " and destroy the rest of the " \
                                      "" + indicatecolour + "Quantum Order" + textcolour + "! (\S)This includes "+personcolour+"Dr. Minnick, "+personcolour+"Dr. Novog"+textcolour+", "+personcolour+"Dr. Kitai"+textcolour+", "+personcolour+"Dr. knights"+textcolour+", " \
                                      ""+personcolour+"Dr. Preston"+textcolour+", "+personcolour+"Dr. Kleimann"+textcolour+", "+personcolour+"Dr. Buijs" + \
            textcolour+", "+personcolour+"Dr. Lapierre"+textcolour + \
            ", and "+personcolour+"Dr. Nagasaki"+textcolour+"."
        DEATHS = [ENEMIES[i].alive for i in
                  ['dr. minnick', 'dr. novog', 'dr. kitai', 'dr. knights', 'dr. preston', 'dr. kleimann', 'dr. buijs',
                   'dr. lapierre', 'dr. nagasaki']]
        if True in DEATHS:
            pass
        else:
            PLAYER.alive = False
            GAMEINFO['winner'] = 1
            # Dark ending, kill McMaster and all Quantum Order
            return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    # Light Ending, kill Cassidy
    elif not ENEMIES['dr. cassidy'].alive and QUESTS['restored order']:
        ENEMIES['sir william mcmaster'].Dinfo = "NO WAIT? WHY? "+personcolour+"Sir William McMaster "+textcolour+" falls, slain beside " + \
            personcolour+"Dr. Cassidy "+textcolour + \
            ". (\S)You see the "+wincolour+"Deed to McMaster" + \
            textcolour+" drop from his pocket."
        ENEMIES['sir william mcmaster'].drop = None
        PLAYER.alive = False  # does this so you can get out of the main loop
        GAMEINFO['winner'] = 2
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    # say if you kill the hooded man, say bit hits him, the game ends
    if not ENEMIES['hooded man'].alive:
        PLAYER.alive = False  # does this so you can get out of the main loop
        GAMEINFO['winner'] = 2
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    else:
        if not GAMEINFO['winner']:
            GAMEINFO['winner'] = 0
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


# If Events list gets to long can make it its own file
def events(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item_object.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class interact_object keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class enemy_object keyed by their lowcase equipment name (item_object.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope

    # PAP Event
    # TODO Make time not GMT so it doesn't matter which time zone you're in
    # TODO Make sure this isn't set so it's not always 420
    # insttime = time.gmtime(time.time() - 4 * 60 * 60)  # Used to debug and test the time based events by adding timer
    # print time.asctime(insttime)  # Prints out the ascci time to debug (Also nice to see but breaks immersion)
    if QUESTS['completionist']:
        # Instantaneous struct_time object at the time of reading if you haven't beaten everything
        insttime = time.localtime()
    else:
        # Sets time to constantly 4:20pm time object
        insttime = time.gmtime(1562765901.005 + 24240 - 141 - (4 * 60 * 60))
    # print insttime  # for debugging time
    # Thunder, cowboys, Bell, PAP sound

    # Simulated times to trigger the event, based on seconds from Epoch

    # gmtenthirty = gmfourtwenty + 6 * 60 * 60 + 10 * 60  # 10:30pm
    # insttime = time.gmtime(gmtenthirty)     # 10:30pm time object
    # TODO Make it so if you Do all intractables + (even empty ones) + Quests after winning the game you unlock PAP
    # if INTERACT['red book'].quest == True:
    #     gmfourtwenty = 1562765901.005 + 24240 - 141 - (4 * 60 * 60)  # 4:20pm, Subtracting the 4 hours for gm time
    #     insttime = time.gmtime(gmfourtwenty)  # 4:20pm time object
    # if INTERACT['blue book'].quest == True:
    #     insttime = time.localtime()  # Instantaneous struct_time object at the time of reading

    # LINEBREAK = "========================================================================"  # standard display with 72 characters
    # standard display with 72 characters
    LINEBREAK = "=======================The=Eng=Phys=Text=Adventure======================="

    #  -- Acheivement: 100 % the game --
    if GAMEINFO['winner'] and QUESTS['completionist']:
        enemycompletion = [ENEMIES[i].quest for i in
                           ['rod the bowler', 'brian the weeb', 'erik the sk8r', 'brendan fallon', 'liam the gamer',
                            'steven the first-year', 'paul the janitor', 'phil the drunk', 'zack the snack', 'connor the biologist',
                            'danya the daniel']]
        interactcompletion = [INTERACT[i].quest for i in
                              ['garbage can', 'rca tv', 'sharpxchange', 'rules sign', 'lenovo laptop', 'coat of arms',
                               'mouse', 'gate of the forest']]

        # print "status " + str(GAMEINFO['winner'])
        # enemycompletion = [ENEMIES[i].quest for i in ['erik the sk8r']]
        # interactcompletion = [INTERACT[i].quest for i in
        #               ['garbage can']]

        if (False in enemycompletion) or (False in interactcompletion):
            # print enemycompletion
            # print interactcompletion
            pass
        else:
            printT("(\S) YOU DID IT!!!! YOU " + wincolour +
                   "100% THE GAME" + textcolour + "! Type anything to continue:")
            input("")
            AsciiArt.Acheivement()
            # appends they won at the end of the log file to make it easier find
            GAMEINFO['log'].append("---THEY 100% the game!---")
            # saves all data to later be submited, different from the main save file
            save_game(GAMEINFO['playername'] + " 100 Percent")
            # 4:20pm, Subtracting the 4 hours for gm time
            gmfourtwenty = 1562765901.005 + 24240 - 141 - (4 * 60 * 60)
            # Sets time to constantly 4:20pm time object
            insttime = time.gmtime(gmfourtwenty)
            QUESTS['completionist'] = 0

    # -- Acheivement: Killing Brendan Fallon
    # Speedruners and people don't like things that are random but here we are
    if not ENEMIES['brendan fallon'].alive and QUESTS['kill brendan fallon']:
        printT("(\S) YOU DID IT!!!! YOU " + wincolour +
               "KILLED BRENDAN FALLON" + textcolour + "! Type anything to continue:")
        input("")
        AsciiArt.Acheivement()
        # adds to log file for the clout
        GAMEINFO['log'].append("---THEY KILLED BRENDAN FALLON!---")
        # save to be submitted
        save_game(GAMEINFO['playername'] + " killed bf")
        # 4:20pm, Subtracting the 4 hours for gm time
        gmfourtwenty = 1562765901.005 + 24240 - 141 - (4 * 60 * 60)
        # Sets time to constantly 4:20pm time object, opens PAP
        insttime = time.gmtime(gmfourtwenty)
        QUESTS['kill brendan fallon'] = 0

    # Setting up the Event
    # If time object hour is 4am or 4pm and the minute is 20 (so lasting 1 minute)
    if (insttime.tm_hour == 4 or insttime.tm_hour == 16) and insttime.tm_min == 20 and QUESTS["PAP"]:
        QUESTS["PAP"] = 0
        # Signaling Event, depends whether you're inside or outside
        printT("A Bolt of lightening strikes the top of JHE")
        # TODO make this an interior after so you decide to go in
        MAPS[2][4][3][0].info = "~?~:\nYou can only go back down the stairs."
        MAPS[2][4][3][0].lore = "As you reach the top of the stairs you can feel the " + red + "heat" + textcolour + " intensify. " \
                                "Where the way was blocked before is a " + red + "melted hole" + textcolour + " just big enough for you to fit through. You expect to enter the " \
                                "hallway but see all the interior walls have been removed. All that remains are stone walls and boarded up windows. " \
                                "Textbooks and broken lab equipment litter the ground. You turn the corner to the lecture hall where you would " \
                                "fall asleep in the 8:30 1D04 lecture. Glowing red hot in the centre of the room is the " + interactcolour + "Pack-a-Punch Machine" + textcolour + "! " \
                                "(\S) (\S) Enscribed on the side in graffiti is 'BLAZE IT'."
        MAPS[2][4][3][0].travelled = 1
        MAPS[2][4][3][0].place_interact(INTERACT["pack-a-punch"])
    # Event Main Activity "Pack-a-Punching" when you inspect the machine
    elif (PLAYER.location == list(INTERACT["pack-a-punch"].location)) and INTERACT["pack-a-punch"].quest:
        PAPScreen = True
        upgradechoice = 0
        sacrificechoice = 0
        while PAPScreen:
            printT(LINEBREAK)
            # AsciiArt.PackScreen() # TODO Enable once Dynamic Ascii Art
            # Displaying Options
            if upgradechoice == 0:
                printT("Item 1: Choose an " + itemcolour + "Item" +
                       textcolour + " to " + wincolour + "Upgrade" + textcolour + "")
            else:
                printT("Item 2: Choose an " + textcolour + "Item" + textcolour +
                       " to " + losecolour + "Sacrifice" + textcolour + "")
            k = 0
            for i in PLAYER.inv:
                if PLAYER.inv[i].name == 'EMPTY':  # skips empty items if empty name
                    # print "THIS B**** EMPTY - YEET"
                    continue  # advance to the next i

                k += 1
                if (k != int(upgradechoice)):
                    printT("[" + str(k) + "]" + PLAYER.inv[i].name +
                           " " + str(PLAYER.inv[i].stats))
            printT("[" + str(k + 1) + "]Back\n")
            # Input and Check Input
            try:
                if upgradechoice == 0:
                    printT("Choose the number of the " + itemcolour + "item" + textcolour +
                           " you want to " + interactcolour + "Pack-a-Punch" + textcolour + ": ")
                    upgradechoice = eval(input(""))
                    if upgradechoice <= 0 or upgradechoice > k + 1:
                        printT("" + losecolour +
                               "Please enter a valid option!" + textcolour + "")
                        upgradechoice = 0
                else:
                    printT("Choose the number of the " + itemcolour + "item" + textcolour +
                           " you want to " + losecolour + "sacrifice" + textcolour + ": ")
                    sacrificechoice = eval(input(""))
                    if sacrificechoice <= 0 or sacrificechoice > k + 1:
                        printT("Please enter a valid option!")
                        sacrificechoice = 0
                    elif upgradechoice == sacrificechoice:
                        printT("" + losecolour +
                               "Please enter a valid option!" + textcolour + "")
                        sacrificechoice = 0

            except:
                printT("" + losecolour +
                       "Please input a number selection!" + textcolour + "")

            # Back Options Options
            if upgradechoice == k + 1:  # if you choose back on upgrade choice screen the loop exits
                PAPScreen = False  # Break the loop to exit it
            elif sacrificechoice == k + 1:  # if you choice back on sacrifice screen it resets to screen 1
                upgradechoice = 0
                sacrificechoice = 0

            # PAP Operation
            if (0 < upgradechoice < k + 1) and (0 < sacrificechoice < k + 1):
                PAPScreen = False

                # Getting the item_object objects
                k = 0
                for i in PLAYER.inv:
                    # skips empty items by naming. Making assumption that no item_object is named 'EMPTY'
                    if PLAYER.inv[i].name == 'EMPTY':
                        # print "THIS B**** EMPTY - YEET"
                        continue  # advance to the next i
                    k += 1
                    if k == upgradechoice:
                        # Objecst are first-class so can create them dynamically in Python
                        upgrade_object = PLAYER.inv[i]
                    elif k == sacrificechoice:
                        # copying object to a temp variable
                        sacrifice_object = PLAYER.inv[i]

                printT("Upgrading: " + upgrade_object.colouredname + "\nSacrificing: " +
                       sacrifice_object.colouredname + "\n\nThis cannot be undone. \nType Y if this is correct:")
                if input("").lower() in ["y", 'yes', '1']:
                    pass  # if they're sure they want to do something go foward
# The pass statement in Python is used when a statement is required syntactically but you do not want code to execute.
                else:  # goes back to the loop and start again
                    break
                    upgradechoice = 0
                    sacrificechoice = 0
                # Dropping the items (removing them)
                # setting object location to none. Does this need to be done? I don't think so but just to be safe
                ITEMS[upgrade_object.name.lower()].location = (
                    None, None, None, None)
                # NONE has to be this format or else not comparible to other locations and will break
                ITEMS[sacrifice_object.name.lower()].location = (
                    None, None, None, None)
                # Set item to empty so item is removed from the player inventory but not placed in the world so not recoverable.
                PLAYER.inv[upgrade_object.worn] = PLAYER.emptyinv[upgrade_object.worn]
                # Set item to empty so item is removed from the player inventory but not placed in the world so not recoverable.
                PLAYER.inv[sacrifice_object.worn] = PLAYER.emptyinv[sacrifice_object.worn]
                # del ITEMS[upgrade.name.lower()]  # deleting from the items dictionary, don't want to do this, might run into key errors
                # del ITEMS[sacrifice.name.lower()]  # deleting from the items dictionary, don't want to do this, might run into key errors

                # Upgrading the one item_object based on the sacrifice
                printT("The Machine Reads: " + wincolour + "'Pack-a-Punching" +
                       indicatecolour + " Please Wait" + textcolour + "'")
                upgrade_object.colouredname = "" + wincolour+"Better " + itemcolour + upgrade_object.name + \
                    textcolour+""  # Adding Better to left side of name each time it's upgraded
                # Adding Better to left side of name each time it's upgraded
                upgrade_object.name = "Better " + upgrade_object.name
                # taking the sum of the stats of each item_object
                sumUStats = upgrade_object.stats[0] + \
                    upgrade_object.stats[1] + upgrade_object.stats[2]
                sumSStats = sacrifice_object.stats[0] + \
                    sacrifice_object.stats[1] + sacrifice_object.stats[2]
                # Sum of item_object stats of sacrifice has to be 1/10th that of the PAP item_object to double or add (whichever is better), or else they just add
                if sumUStats / 10 <= sumSStats:
                    # Doubling stats of the item_object
                    if sumUStats + sumSStats > sumUStats * 2:
                        upgrade_object.stats = (upgrade_object.stats[0] + sacrifice_object.stats[0], upgrade_object.stats[1] + sacrifice_object.stats[1],
                                                upgrade_object.stats[2] + sacrifice_object.stats[2])  # replacing stats tuple with sum
                    else:
                        upgrade_object.stats = (upgrade_object.stats[0] * 2, upgrade_object.stats[1] * 2,
                                                upgrade_object.stats[2] * 2)  # replacing stats tuple with doubling them
                else:
                    # Adding the Stats
                    upgrade_object.stats = (upgrade_object.stats[0] + sacrifice_object.stats[0], upgrade_object.stats[1] + sacrifice_object.stats[1],
                                            upgrade_object.stats[2] + sacrifice_object.stats[2])  # replacing stats tuple

                upgrade_object.location = (2, 4, 3, 0)
                # writing it to the ITEMS dictionary
                ITEMS[upgrade_object.name.lower()] = upgrade_object
                # Placing the Upgraded Item on the ground
                MAPS[2][4][3][0].place_item(upgrade_object)

                # TODO problem is that allkeys are not updated for spellchecking

                printT("The "+interactcolour+"Pack-a-Punch "+textcolour +
                       "wirls and screaches, glowing bright, before spitting out the " + upgrade_object.colouredname + " onto the ground!")
                # TODO add pack-a-punch sound

        # Resetting quest flag so you don't always inspect it once you enter the room
        INTERACT["pack-a-punch"].quest = False

    # Resetting the Event
    elif (QUESTS["PAP"] == 0) and (not (PLAYER.location == (2, 4, 3, 0))) and (not (insttime.tm_min == 20)):
        QUESTS["PAP"] = 1

        # print "DONT BLAZE IT"
        MAPS[2][4][3][0].info = "~3RD FLOOR JHE Stairs~:\nYou can only go back down the stairs."
        MAPS[2][4][3][0].lore = "You see solid block of sheet metal covering the door. Was it " + \
            indicatecolour + "always" + textcolour + " this way?"
        MAPS[2][4][3][0].travelled = 1
        MAPS[2][4][3][0].remove_interact(INTERACT["pack-a-punch"])
        INTERACT["pack-a-punch"].location = (None, None, None, None)

    # TENThirty Event
    # If time object hour is 4am or 4pm and the minute is 20 (so lasting 1 minute)
    if (insttime.tm_hour == 10 or insttime.tm_hour == 22) and insttime.tm_min == 30:
        if not (PLAYER.inv['body'] == EMPTYBODY):  # If  your body isn't empty
            printT("" + wincolour+"10:30 "+textcolour+"NO SHIRTY")
            printT("You feel compelled to take your "+itemcolour+"shirt " +
                   losecolour+"off "+textcolour+"and drop it on the ground")
            # Drops the item_object you have on you, don't forget it has to be name of the item_object and lowercase.
            # Also can't be PLAYER.drop function because then it doesn't go onto the ground
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = PLAYER.drop_object(PLAYER.inv['body'].name.lower(
            ), MAPS, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)  # drops your shirt on the ground

    # Killcount counter in player will trigger the police eventually

    # --- Portals ---
    # TODO Build in this portal fucntionality into INTERACTS or maybe just places with doors

    # To Green Lake
    if INTERACT["lake painting"].quest:
        # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        PLAYER.location = [0, 0, 0, 3]
        CurrentPlace = MAPS[0][0][0][3]
        CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)
        INTERACT["lake painting"].need = None
        printT("(\S)You no longer need the keys to get into this place.")
        INTERACT["lake painting"].quest = False

    # Back to Art Museum
    if INTERACT["portkey"].quest:
        # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        PLAYER.location = [3, 0, 1, 0]
        CurrentPlace = MAPS[3][0][1][0]
        CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)
        INTERACT["portkey"].quest = False

    # To Haunted forest from COOTES DRIVE

    if INTERACT['opening in the trees'].quest:
        # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        PLAYER.location = [4, 0, 0, 4]
        CurrentPlace = MAPS[4][0][0][4]
        if CurrentPlace.travelled:
            printT("You enter... (\S)")
            AsciiArt.HauntedForest()
        CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)
        INTERACT['opening in the trees'].quest = False

    # To COOTES DRIVE from Haunted Forest Start
    if INTERACT['trail to cootes drive'].quest:
        # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        PLAYER.location = [3, 7, 1, 0]
        CurrentPlace = MAPS[3][7][1][0]
        CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)
        INTERACT['trail to cootes drive'].quest = False

    # To COOTES DRIVE from escape rope
    if INTERACT['escape rope'].quest:
        # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        PLAYER.location = [3, 7, 1, 0]
        CurrentPlace = MAPS[3][7][1][0]
        CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)
        INTERACT['escape rope'].quest = False

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    # Rory Companion Event
    # if chicken in inventory Rory will follow you
    # add to attack script that if you attack with chicken in hand Rory will aid you


# --- Game Function Scripts  ---
"""
These scripts are used to encapsulate game-specific functionality.
These Scripts Extend the functionality of the in-game functions at the point they are called in GameFunction.
These are only called when the parent function is called. U
Usually located after the action conditions but before the actions are executed
They work by accepting the game state from the game function call and then returning it. Anything modified in the
    script will be modified at the point in the game fucntion.
Could use a decorator wrapper but this is a simpler function call.
"""
# TODO make this into a scripting class when I'm not lazy


def equip_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def drop_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def move_script(place, MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    # place is the new current map_object you just moved into
    x = place.location[0]
    y = place.location[1]
    z = place.location[2]
    dim = place.location[3]

    # -- Brendan Fallon Function --
    bf = ENEMIES['brendan fallon']
    bfchance = 0.003
    if GAMEINFO['devmode']:
        bfchance += 0.25
    elif PLAYER.inv['body'] == ITEMS['tony hawk shirt']:
        bfchance += 0.007
    if bf.location != (None, None, None, None):
        MAPS[bf.location[0]][bf.location[1]][bf.location[2]
                                             ][bf.location[3]].remove_enemy(bf)
    if random() <= bfchance:
        printT(" (\S)You see A " + wincolour +
               "BRENDAN FALLON" + textcolour + ".")
        MAPS[x][y][z][dim].place_enemy(bf)
        # AsciiArt.Hero()  # TODO Enable once Dynamic Ascii Art
    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def combat_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def attack_script(enemy, MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]
    CurrentPlace = MAPS[x][y][z][dim]

    # -- Big Hits function --
    bhchance = 0.01
    if PLAYER.inv['head'] == ITEMS['helm of orin bearclaw']:
        bhchance += 0.10
    if PLAYER.inv['body'] == ITEMS['big hits shirt']:
        bhchance += 0.05
    if PLAYER.name == "Big Hits Twofer":  # This is for testing big hits events
        bhchance = 0.20
    if GAMEINFO['devmode']:
        bhchance = 0.5

    if type(enemy) is Animal:  # if you try to attack an animal BH comes and punches you
        printT(" (\S)An oblivion gate opens and a " + lightmagenta + "purple faced hero" + textcolour + " in " +
               lightblack + "ebony armour" + losecolour + "punches you" + textcolour + " for attempting to attack an animal.")
        PLAYER.health -= 25

    elif random() <= bhchance:  # bigHits feature TODO have oblivion sound effects if enabled
        # AsciiArt.BigHits()  # TODO Enable once Dynamic Ascii Art
        printT(" (\S)An oblivion gate opens and a " + lightmagenta + "purple faced hero" + textcolour + " in " +
               lightblack + "ebony armour" + wincolour + " punches " + personcolour + enemy.name + textcolour + " to death.")
        printT(enemy.Dinfo)  # slow version
        enemy.alive = False
        if enemy.drop:
            printT(" (\S)" + enemy.colouredname + " dropped the " +
                   ITEMS[enemy.drop].colouredname + ".")
            CurrentPlace.place_item(ITEMS[enemy.drop])
    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def talk_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def stats_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def inspect_examine_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def inspect_use_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def inventory_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def eat_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def setup_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def ending_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS
