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


from GameFunctions import *  # importing the global dictionaries/values
import time
import start_screen  # used for the EPTA all the way down quest
import os  # used to put files in the cache folder
import AsciiArt
from Colour import *
import playsound

global QUESTS

# List of quests and storylines that then get's built into a dictionary
# This dictionary is just flags to keep track of quest completion to advance or end quests
# it's defined here for convience of working but is dealing with a global variable defined in gamefunctions

questlist = [
    # story
    'hooded man',
    # sidequests
    'rules sign',
    'EPTA all the way down'
    # events


    ]

    # PHILpocalypse  # After you give Phil is braces he sobers up and becomes tired Phil.
    # After he asks for a coffee "Man I could really use a coffee but I don't want to spend the money
    # if you give him coffee he gives you a free wish "OH YEAH I AM CAFFINATED. I feel like I can do anyhing!"
    # If you give him a cappuccino the PHILpocalypse storyline begins:
    # You see his eyes dilate "OH YEAH I"M FEELING GREAT", He snaps his fingers and there's a flash.
    # You wake in JHE field "Not again" and everyone on the map is gone. Eventually you meet a Phil clone

# building the quest dictionary because you can't just overwrite the dumb dictionaries for some dumb reason
for quest in questlist:
    QUESTS.update({quest: 1})


def Opening():  # Scripted openning. Needs to defined before can be called in EPTA all the way down.
    DELAY = 1.5
    #IT WORKS!
    audiopath = os.path.join(os.getcwd(), "MediaAssets","","StarWarsOpenningFadeOut.mp3") #points to the eddited star wars theme
    playsound.playsound(audiopath, False) #plays the sound with 'multithreading'
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
    time.sleep(3.5) #4 seconds
    print(CLEARSCREEN)
    print("")
    print("         A short time ago on a campus not so far,")
    print("         far away....\n")
    time.sleep(3) #5.5 seconds
    print(CLEARSCREEN)
    print()
    print("___________                __________.__")
    print("\_   _____/ " +red+ "THE_GREAT" +textcolour+ "_____ \______   \  |__ ___.__. ______")
    print(" |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/")
    print(" |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ ")
    print("/_______  /___|  /\___  /   |____|   |___|  / ____/____  >")
    print("        \/     \//_____/  " +red+ "TEXT ADVENTURE" +textcolour+ "  \/\/ (v4.20) \/ ")
    time.sleep(7.5)
    print("")
    print("T h e  c a m p u s  i s  i n  a  s t a t e  o f  u n r e s t.")
    time.sleep(DELAY)
    print("A n  " +indicatecolour+ "a n c i e n t  f o r c e" +textcolour+ "  h a s  b e e n  a w o k e n")
    time.sleep(DELAY)
    print("a f t e r  t h e  e v e n t s  o f  a  d e b a u c h e r o u s")
    time.sleep(DELAY)
    print("e v e n i n g  a t  t h e  " +mapcolour+ "P h o e n i x" +textcolour+ ".\n")
    time.sleep(DELAY*2)
    print("T h e  h e r o  a w a k e n s  i n  " +mapcolour+ "f r o n t  o f  J H E" +textcolour+ "")
    time.sleep(DELAY)
    print("w i t h  a  c o n s i d e r a b l e  h e a d a c h e  b u t")
    time.sleep(DELAY)
    print("w i t h o u t  t h e i r  " +itemcolour+ "I R O N  R I N G" +textcolour+ ".\n")
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
    print("" +itemcolour+ "I R O N  R I N G" +textcolour+ "  a n d  r e t u r n i n g  b a l a n c e")
    time.sleep(DELAY)
    print("t o  t h e  f a c u l t y.\n")
    time.sleep(DELAY)
    #print CLEARSCREEN  #Don't clearscreen at end so people can read!
    # for i in range(14):
    #     print "\n"
    #     time.sleep(DELAY/2)

def Closing():  # Closing Scripted event
    DELAY = 1.5
    print("\nAnd so, the "+wincolour+"fate" +textcolour+ " of "+mapcolour+"McMaster" +textcolour+ " has been decided...")
    time.sleep(DELAY)
    print("Our hero has unlocked the "+wincolour+"secrets" +textcolour+ " of "+mapcolour+"McMaster University" +textcolour+ "")
    time.sleep(DELAY)
    print("and "+wincolour+"lived" +textcolour+ " to tell the tale.\n")
    time.sleep(DELAY)
    print("___________                __________.__")
    print("\_   _____/ " +red+ "THE_GREAT" +textcolour+ "_____ \______   \  |__ ___.__. ______")
    print(" |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/")
    print(" |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ ")
    print("/_______  /___|  /\___  /   |____|   |___|  / ____/____  >")
    print("        \/     \//_____/  " +red+ "TEXT ADVENTURE" +textcolour+ "  \/\/ (v4.20) \/ \n")
    time.sleep(DELAY)
    print("Created by:\n"+red+"Brendan Fallon" +textcolour+ ", " +white+ "Tyler Kashak" +textcolour+ ", and " +lightblue+ "Mitchell Lemieux" +textcolour+ ".  \n")
    time.sleep(DELAY)
    printT("" +lightmagenta+ "Special Thanks:" +textcolour+ "\n" +personcolour+ "Erik" +textcolour+ " and " +personcolour+ "Phil" +textcolour+ " our best " +indicatecolour+ "playtesters" +textcolour+ "! There are no " +wincolour+ "better quality checkers" +textcolour+ " than you guys. (\S)")
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
           "persons, living or dead, or actual events is purely coincidental. (\S)",72,0)
    time.sleep(DELAY)
    AsciiArt.ThanksForPlaying()
    time.sleep(DELAY)


# --- Game Loop Scripts  ---
# These are called once per loop run. Usually to check conditions to progress things

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



    # Talk to hooded man
    # if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
    #     MAPS[4][4][1][0].place_enemy(ENEMIES["dr. kitai"])
    #     MAPS[2][4][2][0].place_enemy(ENEMIES["dr. preston"])
    #     MAPS[1][6][2][0].place_enemy(ENEMIES["dr. lapierre"])
    #     MAPS[5][4][1][0].removeEnemy(ENEMIES["hooded man"])
    #     ENEMIES["hooded man"].location = (None, None, None, None)  # the location should be set to none but for some reason it's fine
    #     ENEMIES['hooded man'].spoke = False
    #     QUESTS["talk to mysterious man"] = 0

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


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


    # -- Rules Sign --
    if INTERACT["rules sign"].quest and QUESTS['rules sign']:  # Once the sign is read
        MAPS[2][2][0][2].remove_interact(INTERACT["rules sign"])
        INTERACT["rules sign"].location = (None,None,None,None)
        printT( "The sign " +indicatecolour+ "disappears" +textcolour+ " in a flash of " +indicatecolour+ "smoke" +textcolour+ ". You look around. Are you still dreaming?")
        QUESTS["rules sign"] = 0



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



    # Killcount counter in player will trigger the police eventually


    # --- Portals ---
    # TODO Build in this portal fucntionality into INTERACTS or maybe just places with doors

    # To Green Lake
    if INTERACT["lake painting"].quest:
        PLAYER.location = [0,0,0,3]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        CurrentPlace = MAPS[0][0][0][3]
        CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)
        INTERACT["lake painting"].need = None
        printT("(\S)You no longer need the keys to get into this place.")
        INTERACT["lake painting"].quest = False

    # Back to Art Museum
    if INTERACT["portkey"].quest:
        PLAYER.location = [0,2,0,2]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        CurrentPlace = MAPS[0][2][0][2]
        CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)
        INTERACT["portkey"].quest = False

    # -- EBTA All the way Down --
    # when you put the pen in the laptop it opens the thing
    if INTERACT["lenovo laptop"].quest and QUESTS['EPTA all the way down']:
        # TODO as homework see if there's a way to do this with recursion instead of simulating it
        # Would put drums if there was sound effect
        playgame = input('========================================================================\nWould you like to play? \n').lower()
        if playgame == "yes" or playgame == "y":
            printT("You click on the game and it begins in the terminal. The " +red+ "drumming intensifies" +textcolour+ ". You're not sure if you made the right choice.")
            printT("======================================================================== (\S) (\S)")
            import CreativeMode  # this is imported here not at the top to avoid recursive import errors (show up as global names not being defined in the compiler)
            QUESTS['EPTA all the way down'] = 0  # Truns off the quest, has to be before the game saves so the quest is ended when you come back
            save_game(str(GAMEINFO['layersdeep']))  # saving game to be reloaded after death or won the game
            log = GAMEINFO['log']  # keeps the log as a temporary variable to keep a running log in the nested game
            start_screen.Opening()
            newplayername = input("First, what is your name?\n")
            layers = GAMEINFO['layersdeep']  # saves layersdeep to a temporary variable for after the load
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game("basegame")  # should display the exact start
            GAMEINFO['layersdeep'] = layers + 1   # increments the global layers deep because you're now in a lower level, using the memory of the local variable

            GAMEINFO['playername'] = PLAYER.name = newplayername  # this is done for the log
            GAMEINFO['gamestart'] = time.time()  # Settign the game and timestart for for this layer
            GAMEINFO['timestart'] = GAMEINFO['gamestart']
            # Passes the log and adds onto it to keep a HUGE running log (TODO Make this more effecient with log appending)
            GAMEINFO['log'] = log + [str(playgame), "--NESTED GAME--", GAMEINFO['layersdeep'], GAMEINFO['versionname'],
                                     GAMEINFO['playername'], time.ctime(GAMEINFO['timestart']),
                                     "--LOG START--"]  # log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
        elif playgame == "no" or playgame == "n":
            printT("You " +indicatecolour+ "decide against it" +textcolour+ ", fearing the worst. You safely edject the pen, drop it on the floor, and " +red+ "smash" +textcolour+ " it to pieces. Better safe than sorry. (\S)" +lightblue+ "The drumming stops" +textcolour+ ".)")
            printT("========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log
        else:
            printT("" +losecolour+ "It was a yes or no question" +textcolour+ ". When you look back the files are " +losecolour+ "gone" +textcolour+ ". (\S)Even the FlexPDE code. Good riddance.")
            printT("========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log




    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


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

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

def combat_script(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

def attack_script(enemy, MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):

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

