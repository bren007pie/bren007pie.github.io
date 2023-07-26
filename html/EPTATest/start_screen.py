import time
#import pygame
#from pygame import mixer
# import playsound  # Used for openning sound and star wars openning
import os
import fnmatch  # Used to fins the savefiles and display them
from GameFunctions import *  # used for save file loading
from printT import *
from Colour import *
import AsciiArt
#from Ascii_Art.Animations.NevadaAnimation import nevada_animation  # This is relative imports using relitive notation <- relative import messing up Pyscript
from NevadaAnimation import nevada_animation


from GameFunctions import GAMESETTINGS, GAMEINFO # imports these global variables to be used in the start screen

# TODO Implement these based on the size of the screen
#LINEBREAK = "========================================================================" #standard display with 72 characters
LINEBREAK = "=======================The=Eng=Phys=Text=Adventure=======================" #standard display with 72 characters


def splash_screen():
    print(CLEARSCREEN)
    print(textcolour)  # This sets all text color just incase it's weird

    # -- 13 Hollywood Productions --
    # audiopath = os.path.join(os.getcwd(), "MediaAssets", "", "EFXstartup.mp3")  # points to the eddited star wars theme
    # playsound.playsound(audiopath, False)  # plays the startup sound with 'multi-threading'
    print("                " + red + "A" + textcolour + "____ ________")
    print("                /_  H|\_____  \ ")
    print("                 |  O|  ___|  |")
    print("                 |  L| /___   <")
    print("                 |  L|  ___\   |")
    print("                 |  Y| /W O O D|")
    print("                 |___|/________/")
    print("                      " + red + "Production." + textcolour + "")
    time.sleep(3)  # Delay for intro sound
    print(CLEARSCREEN)

    # -- Nevada Animation --
    nevada_animation(os.path.join(os.getcwd(), "MediaAssets", "", "ILLUMINATILiMEDcut.mp3"))


#def version_screen():




#Graphics , audio, difficulty, modes, advanced
#screen width, default read speed/On/Off, suggestion for green
#music on/off, sound levels eventually?
#Eventually easy-medium-hardcore
#eventually speed run, hardcore mode, dev mode, iron man eventually
#all of the settings individually not grouped into modes


def StartScreen():
    # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    global PLAYER  # The main character. player is an object instance of class character.
    global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item_object.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class interact_object keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES  # All the npcs. This a dictionary of objects of class enemy_object keyed by their lowcase equipment name (item_object.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    global GAMESETTINGS  # The game settings that are saved in the game
    # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # If not assignment within the function  may lead to changes only in the local scope

    print(textcolour)  # This sets all text color

    startmenu = True  # startmenu is the variable that keeps you in the startmenu screen loop

    if GAMEINFO['devmode']:  # If in DevMode it skips the loading screen
        startmenu = False  # turning off loading screen

    # TODO: Add something where you get special music when you play after beating the game? Idk. After getting acheivements. Really can't make this w.o. music control
    # elif GAMESETTINGS['SpeedRun']:  # if speedrunning the game get some nice music because skipping the credit roll. If not then yeah
    #     NoWorries = os.path.join(os.getcwd(), "MediaAssets","","NoWorries.mp3") #points to the eddited star wars theme
    #     playsound.playsound(NoWorries, False) # plays the startup sound with 'multi-threading'

    while startmenu:
        print("       ___________                __________.__")
        print("       \_   _____/ ____     _____ \______   \  |__ ___.__. ______")
        print("        |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/")
        print("        |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ ")
        print("       /_______  /___|  /\___  /   |____|   |___|  / ____/____  >")
        print("               \/     \//_____/  " + red + "TEXT ADVENTURE" + textcolour +"  \/\/         \/ ")
        #print "                             Now with colour!"
        print("                    Version " +str(GAMEINFO['versionname']))
        print("                    Release Date: " + GAMEINFO['releasedate'] + "                    \n\n")
        print("Play New Game[P]  Load Game[L]   Settings[S]   Disclaimers[D]  Exit[E]")
        choice = input('Choose what you want to do: ').lower()
        # Play new Game
        if choice in ['p', 'play new game','play']:
            startmenu = False
            print(CLEARSCREEN)

        # Loading Screen and Game
        # TODO Maybe add this loading screen to CreativeMode so you can load in-game
        elif choice in ['l', 'load game','load', 'loadgame']:
             loadscreen = True
             print(CLEARSCREEN)
             while loadscreen:
                print("Load Game\n")
                # print os.listdir(path)  # Gives a list of all files in the directory
                # This Gets and save files in the cache and stores in lists
                loadnumber = 0  # The loadfile display incrementer
                loadnumberlist = []  # list to store loadnumbers
                loadnamelist = []  # list to store loadname
                # Iterates through display string which has all files in the directory
                for file in os.listdir(GAMEINFO['savepath']):
                    filepath = os.path.join(GAMEINFO['savepath'], file)  # gets exact file path so can check size
                    # TODO Nice to have would be showing game playtime or progress

                    if file == "SaveFile basegame.plp" or os.stat(filepath).st_size == 0: # ignores the basegame or the file is empty!
                        next
                    # Searches for the keyword in the files of the savefile directory
                    elif fnmatch.fnmatch(file, 'SaveFile*'):  # looks for files that have SaveFile in the Name
                        loadnumber += 1  # Itterates the loadnumber for the next one
                        # Saving load number as string so can compare Lchoice string later
                        loadnumberlist.append(str(loadnumber))
                        # For some reason strip is being dumb and have to strip "SaveFile" and the " " separately
                        loadnamelist.append(file.lstrip("SaveFile").strip().rstrip("plp").rstrip("."))  # strip is dumb and will keep stripping things if it contains the letters so needs to be done in steps
                        # see https://stackoverflow.com/questions/46222645/string-rstrip-is-removing-extra-characters

                # Displays the save files was numbered list starting from 1
                for i in range(loadnumber):
                    print("[" + loadnumberlist[i] + "]" + loadnamelist[i])
                print("[B]Back\n")

                Lchoice = input('Choose which game you want to load: ')
                if Lchoice in ['b', 'back', 'leave', 'exit']:  # if you choose back the loop exits
                    loadscreen = False

                elif Lchoice in loadnamelist:  # if user enters loadname
                    loadscreen = False
                    startmenu = False
                    MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game(Lchoice)  # loads in the savefile global variables
                    GAMEINFO['loadgame'] = 1
                    GAMEINFO['timestart'] = time.time()  # reset local variable starttime to current time
                    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS  # Sets this loadgame flag so the rest of setup is skipped and goes to main
                    print(CLEARSCREEN)
                elif Lchoice in loadnumberlist:  # if user enters loadnumber has to lookup the load name
                    loadscreen = False
                    startmenu = False
                    MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game(loadnamelist[int(Lchoice)-1])  # converts loadnumber to loadgame index
                    GAMEINFO['timestart'] = time.time()  # reset local variable starttime to current time
                    GAMEINFO['loadgame'] = 1
                    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS   # Sets this flag so the rest of setup is skipped and goes to main
                    print(CLEARSCREEN)
                else:
                    print(CLEARSCREEN)
                    printT(" (\S)"+losecolour+"Please choose one of the options." + textcolour+"")

        # Setting Screen
        elif choice in ['s', 'settings','setting']:
            settingscreen = True
            print(CLEARSCREEN)
            while(settingscreen):

                # TODO Make a DEV mode that disables error catching and enables creative

                print("Settings\n*These may change if you load a previous game\n\n")
                print('[0]Disable Opening:  ' + str(GAMESETTINGS['DisableOpening']))
                print('[1]Speed Run:        ' + str(GAMESETTINGS['SpeedRun']))
                print('[2]Hardcore Mode:    ' + str(GAMESETTINGS['HardcoreMode']))
                # print '[3]Turn Colour Off:    ' + str(GAMESETTINGS['ColourOff']) + " (Must restart client and start new game to take effect)"
                print('[B]Back\n ')

                Schoice = input('Choose which settings you want to toggle: ').lower()
                if Schoice in ['b', 'back', 'leave', 'exit']:
                    print(CLEARSCREEN)
                    settingscreen = False
                elif Schoice =='0':
                    print(CLEARSCREEN)
                    # Have to make sure the values toggle to 0 and 1 not true and false for saving
                    GAMESETTINGS['DisableOpening'] = int(not(GAMESETTINGS['DisableOpening']))
                    # print "Hi I'm a dog"
                elif Schoice =='1':
                    print(CLEARSCREEN)
                    GAMESETTINGS['SpeedRun'] = int(not(GAMESETTINGS['SpeedRun']))
                elif Schoice =='2':
                    print(CLEARSCREEN)
                    GAMESETTINGS['HardcoreMode'] = int(not(GAMESETTINGS['HardcoreMode']))
                # elif Schoice == '3':
                #     print CLEARSCREEN
                #     GAMESETTINGS['ColourOff'] = int(not (GAMESETTINGS['ColourOff']))
                elif Schoice == '/420e69':  # Character that enables DevMode
                    print(CLEARSCREEN)
                    GAMEINFO['devmode'] = int(not(GAMEINFO['devmode']))
                    # Prints throw-off style text while still giving the stat
                    print("\nPlease choose " + str(GAMEINFO['devmode']) + "one of the options.")
                else:
                    print(CLEARSCREEN)
                    printT(" (\S)"+losecolour+"Please choose one of the options." + textcolour+"")

            # Saving Settings Once out of the screen, These setting should be readable and changeable by a person
            settingpath = os.path.join(GAMEINFO['datapath'], "settings.ini")
            f = open(settingpath, "w+")
            for setting in GAMESETTINGS:
        # TODO Before release uncomment this line so DevMode isn't saved. DevMode in setting file is not for RELEASE
                #if setting == "DevMode": continue
                f.write(setting + "\n" + str(GAMESETTINGS[setting]) + "\n")
            f.close()

        # Disclaimer screen
        elif choice in ['d', 'disclaimers','disclaimer']:
            print(CLEARSCREEN)

            printT("Disclaimer (\S) (\S) This game is difficult, requires reading and focus on every piece of text, "
                   "and awareness of small details in order to advance the game. We feel here that we're trying to "
                   "provide an experience that's challenging but rewarding, not punishing. That being said we are "
                   "always open to feedback.(\S) This game is a work in progress and there may be bugs. We do our best "
                   "to avoid, catch, and fix errors promptly. If you do come across one however please submit them to "
                   "our bug response form: https://goo.gl/forms/Jo6P7oMj86OiLvE63 (\S) This is a work of fiction. "
                   "Names, characters, businesses, places, events, locales, and incidents are either the products of "
                   "the author's imagination or used in a fictitious manner. Any resemblance to actual persons, living "
                   "or dead, or actual events is purely coincidental. By playing this game you give up the right to"
                   " any information or files uploaded to the developers for benevolent development of the game.",72,0)
            input("\nHit enter to continue")
            print(CLEARSCREEN)
        # Exiting
        elif choice in ['e', 'exit','leave']: 
            exit()
        else:
            print(CLEARSCREEN)
            printT(" (\S)"+losecolour+"Please choose one of the starting options."+textcolour+"")

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS







#This works great but doesn't compile with displaying text. I got it to compile
#   pygame2exe but doesn't show any text in the exe so might need to use pygame
#   which would be dumb. Can get i
####mixer.init()
####mixer.music.load("StarWarsOpenningFadeOut.mp3")
####mixer.music.play()
####time.sleep(0.2) #needs this delay before the next comand?
####Opening()
####mixer.music.stop()
####mixer.music.load("ErikBeepBox-Song.wav")
####mixer.music.play()
####time.sleep(10)
####mixer.music.stop()

###Trying to make a pygame screen
###https://www.youtube.com/watch?v=gTvVDJofGdI
###creating basic window
##pygame.init() #initializes modules of pygame
##screen = pygame.display.set_mode((600,500)) #making a screen object with that pixel dimensions
##myfont = pygame.font.SysFont("Arial",12)
##done = False
##while not done:
##    for event in pygame.event.get(): #basic window with object
##        if event.type==pygame.QUIT:
##            done = True
##    text1 = myfont.render("Text",1,(0,255,0)) #makes the object attributes
##    screen.blit(text1, (400,10)) #adds font to the screen
##    pygame.draw.rect(screen,(255,0,0),pygame.Rect(100,100,100,100)) #draws a rectangle, 3 args screen object, colour, and 
##    pygame.display.update()


