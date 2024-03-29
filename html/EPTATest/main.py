"""
###Notes###
This is the main entrance file for the Nevada game engine and Eng Phys Text Adventure (EPTA). This game utilizes some poorly done OOP (sorry Mitch), it has it's strengths though!
The comments, organization, and optimization are bad but generally:
this file = the setup, main loop, and ending. Run this to run the game.
GameFunctions.py = The main mechanics of the game and the quests. All non-class functions. 
game_classes_2017.py = Class definitions and their coresponding functions.
game_objects_x.py = All the map locations, items, npcs (called enemies), and interactables. Also creates the dictionaries of them.
Setup.py = Py2exe file used to compile into an exe. Run using "python setup.py py2exe" in command prompt.

In general try to keep this structure and put any other long ascii or modules into another file.
"""

# --- Import Screen where you choose which version of the game to import ---
# don't import * from these b.c. these pull global variables from game functions and doing a recursive import creates errors
import game_objects_2017 as game_objects
import game_scripts_2017 as game_scripts
import start_screen
# this imports the code and all the code dependancies (functions imported in that)
from GameFunctions import *
# import MapDisplay  # Used to separate minim-ap display
import AsciiArt
import interpreter  # Used to separate text interpretation and commands
import importlib
from Colour import *


print(CLEARSCREEN)

# version_screen = 1
# while (version_screen):
#     try:
#         game_choice = input(
#             "What version would you like to play? \n\n[1] ( 2017 - 2018 ) The Eng Phys Text Adventure \n[2] ( 2018 - 2019 ) The Capstone Adventure \n\n")
#         # game_choice = input("What version would you like to play? \n\n[1] ( 2017 - 2018 ) The Eng Phys Text Adventure \n[2] ( 2018 - 2019 ) The Capstone Adventure \n[3] ? \n[4] ( 2020 - 2021 ) The COVID Text 1Adventure \n\n")

#         game_choice = int(game_choice)
#         game_object_modules = ["game_objects_2017", "game_objects_2018"]
#         game_script_modules = ["game_scripts_2017", "game_scripts_2018"]
#         game_objects = importlib.import_module(
#             game_object_modules[game_choice - 1])
#         game_scripts = importlib.import_module(
#             game_script_modules[game_choice - 1])
#         version_screen = 0
#     except:
#         print(CLEARSCREEN)
#         print("" + losecolour + "Please enter a valid number." + textcolour + "")


print("BLARG")
# import game_scripts_2017 as game_scripts  # Used to separate quest/event functions

# from TextParser import *  got rid of this to reduce import tracing tracking problems but may break everything
# import game_objects_2017
# import CreativeMode #don't import * from these b.c. these pull global variables from game functions and doing a recursive import creates errors


# TODO Make sure to change BOTH versions and release date are correct
# If there was a title screen it would go here
GAMEINFO['version'] = "0.31.XX"
GAMEINFO['versionname'] = lightblue + "Beta " + red + "v" + white + "0.30.01 - " + blue + 'T' + cyan + 'H' + red + 'E ' \
    + green + 'F' + lightgreen + 'I' + lightblue + 'N' + lightcyan + 'A' + lightgreen + 'L ' \
    + lightmagenta + 'E' + lightred + 'P' + lightwhite + 'T' + lightyellow + 'A ' + magenta \
    + 'U' + red + 'P' + white + 'D' + yellow + \
    'A' + blue + 'T' + red + 'E' + textcolour
GAMEINFO['releasedate'] = "Nov 21, 2020"


# LINEBREAK = "========================================================================" #standard display width breaker, 72 characters
# standard display with 72 characters
LINEBREAK = "=======================The=Eng=Phys=Text=Adventure======================="

# Begining section of the game (not in the main loop), Seperated for nested game


def Setup(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item_object.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class interact_object keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class enemy_object keyed by their lowcase equipment name (item_object.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game

    if GAMEINFO['loadgame']:  # If player loaded the game it returns out of the setup and goes to main
        # reset local variable starttime to current time
        GAMEINFO['timestart'] = time.time()
        # sets the parameter to 0 just so it doesn't accidentally save
        GAMEINFO['loadgame'] = 0
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    if not (GAMESETTINGS['DisableOpening'] or GAMESETTINGS['SpeedRun'] or GAMEINFO['devmode']):
        game_scripts.Opening()  # plays the opening if disable opening is set to False

    print(LINEBREAK)

    if GAMEINFO['devmode']:
        # Skip name step and names your person Doug
        GAMEINFO['playername'] = "Doug Fallon"
    else:
        # - Name Selection -
        name = ""
        # checking for some bad characters that windows files can't have for save files.
        badchar = ["\\", "/", ":", "*", "?", "<", ">", "|", '"']
        while not name:  # name selection can't be empty
            name = input("First, what is your name?\n")
            # TODO instead of pattern matching on certain varaibles just check for empty string
            if name in ["", " ", "  ", "   ", ".", ",", "no"]:  # not accepted names
                printT(""+losecolour+"Please enter a valid name! "+textcolour+"")
                name = ""
            elif [True for e in badchar if e in name]:  # if the bad character is in there
                printT("" + losecolour + "You cannot use \ / : * ? < > |" +
                       ' " in your name!' + textcolour + "")
                name = ""
            else:
                GAMEINFO['playername'] = name

    PLAYER.name = GAMEINFO['playername']
    # changes the name of all name related things in the game
    ENEMIES, MAPS = NameChange(PLAYER.name)

    x, y, z, dim = STARTLOCATION
    if GAMEINFO['devmode']:
        x, y, z, dim = DEVPLAYER.location
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z
    PLAYER.location[3] = dim

    CurrentPlace = MAPS[x][y][z][dim]

    # This prints

    # searches and prints the information with spawn set to true to print "You wake up in"
    CurrentPlace.search(MAPS, dimension_names, GAMESETTINGS, True)

    # Gives the local start date of the game in seconds since epoch of 1970
    GAMEINFO['gamestart'] = time.time()
    # Use this to get a base state newgame, keep it in each time so don't have to worry about updating
    save_game("basegame")
    # This tyler Kashak has to be after the basegame save or else it will always revert the base game to you spawning as Tyler
    # Enables this ULTRA character
    if GAMEINFO['devmode']:  # Obsolete Nov. 20, 2020: or PLAYER.name == "Tyler Kashak" # He realizes he's the main character and can do anything he wants!
        # AsciiArt.One()  # TODO Enable once Dynamic Ascii Art
        print("\nHe is beginning to believe.\n\nYOU are the One.\n")
        # sets him to the initial Tyler character for strating inventory
        PLAYER.__dict__ = DEVPLAYER.__dict__
        PLAYER.maxhealth = 999
        PLAYER.basestats = [420, 420, 420]
        PLAYER.update_stats()
    # so that it says it's been travelled, I moved it down so that it wouldn't effect the basegame save
    CurrentPlace.travelled = 0

    # runtime counter of the start of each main loop session. Needs to be global. Is equal to gamestart at the session start but will change as the user saves, loads, restarts, or does a nested game
    GAMEINFO['timestart'] = GAMEINFO['gamestart']
    if GAMESETTINGS['SpeedRun']:
        print("Your time starts now!")
        # this time.ctime(seconds) converts to a nice readable time to be output to the log
    # log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
    GAMEINFO['log'] = [GAMEINFO['versionname'],  GAMEINFO['playername'],
                       time.ctime(GAMEINFO['gamestart']), "--LOG START--"]

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


def game_loop(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER #The main character. player is an object instance of class character.
    # global ITEMS #All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item_object.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS #All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT #All the interactables (stationary things that need something). This a dictionary of objects of class interact_object keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS #Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES #All the npcs. This a dictionary of objects of class enemy_object keyed by their lowcase equipment name (item_object.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO #Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope

    # Main game loop section that runs while the player is alive (player is killed in story once done)
    # TODO don't have main loop based on player alive but on game being played, e.g. gameExit boolean variable instead
    while (PLAYER.alive):
        # if not(GAMESETTINGS['HardcoreMode']): MapDisplay.mini()  # Minimap display area in game

        # --- Get user Input ---

        # if there's a script loaded carry out those commands! instead of normal
        if GAMEINFO['scriptdata']:
            # pops the first element to go through script until finished
            command = GAMEINFO['scriptdata'].pop(0)
            printT(command)
        else:
            command = input('\nWhat do you want to do?\n')

        print(LINEBREAK)  # This linebreak helps split up each turn
        if GAMESETTINGS['HardcoreMode']:
            print(CLEARSCREEN)

        # --- Update the game world and update graphics (currently coupled) ---
        # Sends the command text to the text parser to be interpreted and action to be done.
        # I made a whole text interpreter for text symantics here? DAMN LOL - BF Nov 20, 2020
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = interpreter.Parser(
            command, MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)

        # increments the command count after every command but doesn't print
        GAMEINFO['commandcount'] += 1
        # print LINEBREAK  # Got rid of this bottom linebreak to hopefully have the current situation more clear
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = game_scripts.story(
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)  # runs through the story quests checks and actions
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = game_scripts.sidequests(
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)  # runs through all the sidequest checks and actions
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = game_scripts.events(
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)  # runs through all the events checks and actions

        # TODO integrate this into game functions with a function, possibly seperate quests from game functions and import all from there to keep things global
        # gets you out of the EPTA all the way down quest and back into the sublayer
        if PLAYER.alive == False and GAMEINFO['layersdeep'] > 0:
            # End(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)
            print(LINEBREAK)
            printT(" (\S)You finish the game and put back the laptop ready to get back to reality.\nHow long did you spend on this game?")
            # sets up a temporary variable to pass the log back up a layer
            log = GAMEINFO['log']
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game(
                str(GAMEINFO['layersdeep']-1))
            # overwrites it to keep a running tab and says what layer we're in
            GAMEINFO['log'] = log + ["--Back in layer: " +
                                     str(GAMEINFO['layersdeep']) + "---"]
            # Doesn't reset the GAMEINFO['timestart'] as the runtime will included the time in the nested function
            # TODO delete the save file you're coming out of

    # calls the end function in main so that the game can continue its loop structure
    MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = End(
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)


def End(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item_object.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class interact_object keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class enemy_object keyed by their lowcase equipment name (item_object.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game

    # saves all data RIGHT away so they can't restart when they die
    save_game(GAMEINFO['playername'])

    # calculates total time you've been playing by adding your loaded runtime to your instance runtime (end time - start time)
    GAMEINFO['runtime'] = GAMEINFO['runtime'] + \
        (time.time()-GAMEINFO['timestart'])
    GAMEINFO['log'] = GAMEINFO['log'] + ["--END OF LOG--", "Stepcount: "+str(GAMEINFO['stepcount']), "Command Count: " + str(GAMEINFO['commandcount']),
                                         "Run Time: " + str(GAMEINFO['runtime']), "--Character STATS--", str(
                                             (PLAYER.location[0], PLAYER.location[1], PLAYER.location[2], PLAYER.location[3])),
                                         str((PLAYER.stats[0], PLAYER.stats[1], PLAYER.stats[2])), str(
                                             PLAYER.health), "HEAD: " + str(PLAYER.inv["head"].name),
                                         "BODY: " + str(PLAYER.inv["body"].name), "HAND: " + str(
        PLAYER.inv["hand"].name), "OFF-HAND: " + str(PLAYER.inv["off-hand"].name)
    ]  # adds the final info to the log leger

    if GAMEINFO['winner'] == 0:  # player died and that's how they're out of the loop
        print(LINEBREAK)
        if GAMESETTINGS['SpeedRun']:
            # displays the runtime for speed running
            DisplayTime(GAMEINFO['runtime'])
        if GAMESETTINGS['SpeedRun']:
            printT("Total Step Count: " + str(GAMEINFO['stepcount']) +
                   " (\S)Total Command Count: " + str(GAMEINFO['commandcount']))
        logGame(GAMEINFO['log'])  # writes the log file
        # lets the player restart the game
        printT("Thanks for playing!! Better luck next time! (\S)")
    else:
        printT("You've " + wincolour + "won" +
               textcolour + "! Type anything to continue.")
        input("").lower()  # If they beat either of the storylines
        # appends they won at the end of the log file to make it easier find
        GAMEINFO['log'].append("---THEY WON---")
        if GAMEINFO['winner'] == 1:  # The bad storyline ending
            printT("After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice, you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allow you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END  (\S)")
            GAMEINFO['winner'] = 1
        elif GAMEINFO['winner'] == 2:  # The good storyline ending.
            printT("Having defeated Dr. Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END. (\S)")
            GAMEINFO['winner'] = 2
        elif GAMEINFO['winner'] == 3:  # The both storyline ending.
            printT("After defeating both Dr. Cassidy and Sir William McMaster you take a moment to think while the deed to McMaster University lies at your feet fluttering slowly in a gentle breeze. You think about what you were told. Does that piece of paper really give you immense power and control over the school? After a quick smirk and a laugh, you pick up the deed and begin to rip it up. The parchment resists for a moment before giving way in a spectacular display of sparks and disappearing into the wind. You go on knowing that the fate of the University now resides in the hands of no one... it resides in everyone's hands. (\S)THE END  (\S)")
            QUESTS['neutral balance'] = 0
            GAMEINFO['winner'] = 3
        if GAMESETTINGS['SpeedRun']:
            # displays the runtime then all other status
            DisplayTime(GAMEINFO['runtime'])
        if GAMESETTINGS['SpeedRun']:
            printT("Total Step Count: " + str(GAMEINFO['stepcount']) +
                   " (\S)Total Command Count: " + str(GAMEINFO['commandcount']))
        logGame(GAMEINFO['log'])  # logs the data to be submitted
        # saves all data to later be submited, different from the main save file
        save_game(GAMEINFO['playername'] + " Winner")
        game_scripts.Closing()  # plays the closing
        printT("Thanks for playing!!! (\S)")
    endchoice = ""
    while not endchoice:  # death or ending selection screen
        printT(" (\S)Continue Playing[C]   Restart Game[R]  Exit[E]")
        # printT(" (\S)Continue Playing[C]   Restart Game[R]  Main Menu Return[M]  Exit[E]")
        # this input is to hold the screen until the player decides what to do
        endchoice = input("Choose what you want to do: ").lower().strip()
        if (GAMEINFO['winner'] == 0) and (endchoice in ["c", "continue playing", "continue", "play"]):
            printT("You can't continue because you're dead!")
            endchoice = ""
        # elif endchoice not in ["c", "r", "m", "e", "continue playing", "continue", "play", "restart game", "restart","main menu return", "main menu", "menu return", "main", "menu", "return", "exit"]:
        elif endchoice not in ["c", "r", "m", "e", "continue playing", "continue", "play", "restart game", "restart", "exit"]:
            printT(""+losecolour+"Please choice a valid option!"+textcolour+"")
            endchoice = ""
    if endchoice in ["c", "continue playing", "continue", "play"]:
        PLAYER.alive = True
        print(LINEBREAK)
        # turn this off so you can continue playing the game without the quest redoing
        QUESTS['restored order'] = 0
        QUESTS['create chaos'] = 0
        # returns to the main (hopefully in the same state)
        game_loop(MAPS, PLAYER, ITEMS, INTERACT, QUESTS,
                  ENEMIES, GAMEINFO, GAMESETTINGS)
    elif endchoice in ["r", "restart game", "restart"]:
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game(
            "basegame")  # loads in the savefile global variables
        # reset local variable starttime to current time
        GAMEINFO['timestart'] = time.time()
        game_loop(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES,
                  GAMEINFO, GAMESETTINGS)  # re-enters the main loop
    # No return to main menu implemented due to bad looping structure
    # elif endchoice in ["m","main menu return","main menu","menu return","main","menu","return"]:
    #     Opening.StartScreen()  # Startscreen loop where you can play new game, loadgame, choose settings, or exit
    #     Setup()
    #     Main()
    elif endchoice in ["e", "exit"]:
        if input("\n\nAre you sure you want to quit the game?\nType Y if you wish to save and leave,\nanythine else to continue: \n").lower() in ["y", 'yes', 'yeah']:
            # adds the runtime (initilized to zero) to the session runtime to make the total runtime
            GAMEINFO['runtime'] += (time.time() - GAMEINFO['timestart'])
            # resets timestart so it's not doubly added at the end
            GAMEINFO['timestart'] = time.time()
            logGame(GAMEINFO['log'])  # logs the game when you save it
            save_game(GAMEINFO['playername'])  # saves all data
            # print "Your game has been saved! " + GAMEINFO['playername']  # Don't indicate the save file has save file in the name
            AsciiArt.ThanksForPlaying()
            printT("" + indicatecolour + "We're sad to see you go :(" + textcolour +
                   " \nI hope whatever you're doing is more fun.\nPress anything to leave")
            input("")
            exit()
    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


# ---------GAME STARTS HERE  ---------

# TODO Reset settings before release before release

# Reading in game settings, has to be at start of game befor anything so it reads in settings
try:  # In case settings file isn't there
    settingpath = os.path.join(GAMEINFO['datapath'], "settings.ini")
    with open(settingpath, 'r') as f:
        data = f.readlines()  # reads in data seperated by newline into a list
    f.close()
    # removes the \n in each list element wise (very useful for list operations)
    data = [f.strip() for f in data]
    for i in range(0, len(data), 2):
        # Reading in file data in attribute value order, value should be an int
        GAMESETTINGS[data[i]] = int(data[i+1])
except:
    # print "\n\nSomething is Wrong with the Setting.ini file!\n\n"
    printT("\n\nNo Settings Detected!\n\n")

# Reading in DEVMODE.ini file if devmode is set
try:  # IF DEVMODE.ini isn't there in the CWD of the game no beuno
    with open("DEVMODE.ini", 'r') as f:
        data = f.readlines()  # reads in data seperated by newline into a list
    f.close()
    if data[0] == "LOL NO U":  # contents of the dev file needs to be
        # quickly asks you want to not be in dev mode in obfuscated way
        if not input("What would you like? Type in n: ") == "n":
            GAMEINFO['devmode'] = 1
            print(CLEARSCREEN)  # clears the screen

except:  # does nothing if no dev file there
    pass
    # raw_input("HI I'M NOT A DEV!")


if not GAMEINFO['devmode']:
    start_screen.splash_screen()  # runs the splash screen if not in devmode

# Start Screen is after reading in settings so it can skip start screen if enabled
# Startscreen loop where you can play new game, loadgame, choose settings, or exit
MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = start_screen.StartScreen()

# TODO Comment out before release, used to debug loading
# GAMEINFO['devmode'] = 1

# The Actual Start of the game when you hit Play, depending on if in Dev Mode or not
if GAMEINFO['devmode']:  # If Dev mode enabled no error catching
    MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = Setup(
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)
    game_loop(MAPS, PLAYER, ITEMS, INTERACT, QUESTS,
              ENEMIES, GAMEINFO, GAMESETTINGS)
else:  # Dev mode not enabled so error catching
    try:  # runs the main functions (the whole game bassically)
        MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = Setup(
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS)
        game_loop(MAPS, PLAYER, ITEMS, INTERACT, QUESTS,
                  ENEMIES, GAMEINFO, GAMESETTINGS)
    # end function is run at the end of main loop so you can restart the game
    # if keyboard pressed or x out of the game, this is so it doesn't save null data when you press teh keyboard
    except (KeyboardInterrupt, SystemExit):
        raise
        # raise os._exit(0)
    except:
        # AsciiArt.Error()  # TODO Enable once Dynamic Ascii Art
        save_game(GAMEINFO['playername'] + " AutoSave")  # saves all data
        # logs the game when it crashes so it can be recreated
        logGame(GAMEINFO['log'])
        printT("If you are just "+indicatecolour+"exiting"+textcolour +
               " the game and see this error message "+indicatecolour+"please ignore"+textcolour+" it!")
        printT("Your game has been saved!: SaveFile " +
               GAMEINFO['playername'] + " AutoSave")
        printT(" (\S)It looks like your game encountered some kind of bug, we're sorry, and we've saved your game. (\S)Check if your game is up to date: (\S)Your current game version = " +
               GAMEINFO['version']+" (\S)Please check to see if you have the latest version at https://engphystextadventure.wordpress.com/downloads/. (\S)If the bug persists, please contact your nearest developer or use the bug reporting tool on the website. (\S)Thanks :D")
        input("Type anything to exit: ")
