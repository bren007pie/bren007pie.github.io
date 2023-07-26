#This file simply converts a text ascii art file into a single line to be printed
#I like to use one of these guys, sorry Liam Flan.:
#https://manytools.org/hacker-tools/convert-images-to-ascii-art/go
#https://www.text-image.com/convert/ascii.html

import time
from Colour import *
# import playsound
import random
import string

getext = "<"+red+"GAME ENGINE"+textcolour+">"

def nevadasw():
 print(" __    __  ________  __     __   ______   _______    ______  ")
 print("/  \  /  |/        |/  |   /  | /      \ /       \  /      \ ")
 print("$$  \ $$ |$$$$$$$$/ $$ |   $$ |/$$$$$$  |$$$$$$$  |/$$$$$$  |")
 print("$$$  \$$ |$$ |__    $$ |   $$ |$$ |__$$ |$$ |  $$ |$$ |__$$ |")
 print("$$$$  $$ |$$    |   $$  \ /$$/ $$    $$ |$$ |  $$ |$$    $$ |")
 print("$$ $$ $$ |$$$$$/     $$  /$$/  $$$$$$$$ |$$ |  $$ |$$$$$$$$ |")
 print("$$ |$$$$ |$$ |_____   $$ $$/   $$ |  $$ |$$ |__$$ |$$ |  $$ |")
 print("$$ | $$$ |$$       |   $$$/    $$ |  $$ |$$    $$/ $$ |  $$ |")
 print("$$/   $$/ $$$$$$$$/     $/     $$/   $$/ $$$$$$$/  $$/   $$/ ")
 #print("")
 #print(getext)

def nevadanw():
 print("$$\   $$\ $$$$$$$$\ $$\    $$\  $$$$$$\  $$$$$$$\   $$$$$$\  ")
 print("$$$\  $$ |$$  _____|$$ |   $$ |$$  __$$\ $$  __$$\ $$  __$$\ ")
 print("$$$$\ $$ |$$ |      $$ |   $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |")
 print("$$ $$\$$ |$$$$$\    \$$\  $$  |$$$$$$$$ |$$ |  $$ |$$$$$$$$ |")
 print("$$ \$$$$ |$$  __|    \$$\$$  / $$  __$$ |$$ |  $$ |$$  __$$ |")
 print("$$ |\$$$ |$$ |        \$$$  /  $$ |  $$ |$$ |  $$ |$$ |  $$ |")
 print("$$ | \$$ |$$$$$$$$\    \$  /   $$ |  $$ |$$$$$$$  |$$ |  $$ |")
 print("\__|  \__|\________|    \_/    \__|  \__|\_______/ \__|  \__|")
 print("")
 #print("")
 #print(getext)

def nevadane():
 print("  /$$   /$$ /$$$$$$$$ /$$    /$$  /$$$$$$  /$$$$$$$   /$$$$$$ ")
 print(" | $$$ | $$| $$_____/| $$   | $$ /$$__  $$| $$__  $$ /$$__  $$")
 print(" | $$$$| $$| $$      | $$   | $$| $$  \ $$| $$  \ $$| $$  \ $$")
 print(" | $$ $$ $$| $$$$$   |  $$ / $$/| $$$$$$$$| $$  | $$| $$$$$$$$")
 print(" | $$  $$$$| $$__/    \  $$ $$/ | $$__  $$| $$  | $$| $$__  $$")
 print(" | $$\  $$$| $$        \  $$$/  | $$  | $$| $$  | $$| $$  | $$")
 print(" | $$ \  $$| $$$$$$$$   \  $/   | $$  | $$| $$$$$$$/| $$  | $$")
 print(" |__/  \__/|________/    \_/    |__/  |__/|_______/ |__/  |__/")
 print("")
 #print("")
 #print(getext)
                                                             
def nevadase():
 print("  __    __  ________  __     __   ______   _______    ______  ")
 print(" |  \  |  \|        \|  \   |  \ /      \ |       \  /      \ ")
 print(" | $$\ | $$| $$$$$$$$| $$   | $$|  $$$$$$\| $$$$$$$\|  $$$$$$\ ")
 print(" | $$$\| $$| $$__    | $$   | $$| $$__| $$| $$  | $$| $$__| $$")
 print(" | $$$$\ $$| $$  \    \$$\ /  $$| $$    $$| $$  | $$| $$    $$")
 print(" | $$\$$ $$| $$$$$     \$$\  $$ | $$$$$$$$| $$  | $$| $$$$$$$$")
 print(" | $$ \$$$$| $$_____    \$$ $$  | $$  | $$| $$__/ $$| $$  | $$")
 print(" | $$  \$$$| $$     \    \$$$   | $$  | $$| $$    $$| $$  | $$")
 print("  \$$   \$$ \$$$$$$$$     \$     \$$   \$$ \$$$$$$$  \$$   \$$")
 #print("")
 #print(getext)
                                                             

# #Cycling animation. Don't like it because cycling is weird
# def nevada_animation(timestep, number_cycles):
#     for i in range(number_cycles):
#         print(CLEARSCREEN)
#         nevadane()
#         time.sleep(timestep)
#         print(CLEARSCREEN)
#         nevadase()
#         time.sleep(timestep)
#         print(CLEARSCREEN)
#         nevadasw()
#         time.sleep(timestep)
#         print(CLEARSCREEN)
#         nevadanw()
#         time.sleep(timestep)

randchars = random.choice(["!","@#$%^&*~?", "EPTA", "Who is SMSE?","COVID-19","Erik","Minnick","McMaster","Cassidy",
                           "Quantum","Minecraft","Zelda","Bren007Pie","Is Tyler awake?", "Where is Mitch?", "Iron Ring",
                           "Declaration","Dr. Okon", "Forest", "Phil",
                          string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, string.digits,
                          string.hexdigits, string.punctuation, string.printable, string.whitespace])

def nevada_animation(audiopath):
    movingtext = getext
    # playsound.playsound(audiopath, False)  # plays the sound with 'multi-threading'
    print(CLEARSCREEN)
    time.sleep(0.234)
    nevadanw()
    time.sleep(2.135-0.234)
    print(movingtext)
    time.sleep(3.604 - 2.135-0.234)
    for i in range(1,6):
        print(CLEARSCREEN)
        random.choice([nevadanw,nevadane,nevadasw,nevadase])()  # https://stackoverflow.com/questions/5465455/syntax-to-call-random-function-from-a-list
        #print(i*"--------" + "" + getext)
        #print(i*"?????????" + "." + getext)
        movingtext = (''.join(random.choice(randchars) for i in range(9))) + "." + movingtext  # https://pynative.com/python-generate-random-string/#:~:text=If%20you%20want%20to%20generate,string%20constant%20using%20a%20random.
        print(movingtext)
        time.sleep(0.4)
    print(CLEARSCREEN)
    nevadanw()
    #print(number_cycles*"----------" + "-")
    print(movingtext.rstrip(getext) + (''.join(random.choice(randchars) for i in range(11))) )
    time.sleep(1.8)
    print(CLEARSCREEN)
    nevadanw()
    print(6 * "??????????" + "?")
    time.sleep(1.0)
    print(CLEARSCREEN)
    time.sleep(2.0)






def randomstringgenerator(randchars,length):
    result_str = ''.join(random.choice(randchars) for i in range(length))
    print(result_str)

def random_nevada_string(numbRandtext):
    nevadanw()
    for i in range(numbRandtext):
        rchars = random.choice(
            ["!", "@#$%^&*~?", "EPTA", "Who is SMSE?", "COVID-19", "Erik", "Minnick", "McMaster", "Cassidy",
             "Quantum", "Minecraft", "Zelda", "Bren007Pie", "Is Tyler awake?", "Where is Mitch?", "Iron Ring",
             string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, string.digits,
             string.hexdigits, string.punctuation, string.printable, string.whitespace])
        randtext = ""
        for j in range(1,6):
            randtext = (''.join(random.choice(rchars) for i in range(9))) + "." + randtext
        randtext = randtext + (''.join(random.choice(rchars) for i in range(11)))
        print(randtext)

#audiopath =
#nevada_animation()

#random_nevada_string(50)