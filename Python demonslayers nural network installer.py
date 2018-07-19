import pip

error_import = """If you get a error make sure python is added to path
if it doesn't work try running as admin""")
watermark = """

___  ___          _        _
|  \/  |         | |      | |
|      | __ _  __| | ___  | |__  _   _
| |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |
| |  | | (_| | (_| |  __/ | |_) | |_| |
\_|  |_/\__,_|\__,_|\___| |_ __/ \__, |
                                  __/ |
                                 |___/





88        88               88                                                                      ,ad8888ba,   88b           d88  88888888ba,
88        88               88                                                                     d8"'    `"8b  888b         d888  88      `"8b
88        88               88                                                                    d8'            88`8b       d8'88  88        `8b
88        88  8b,dPPYba,   88   ,d8   8b,dPPYba,    ,adPPYba,   8b      db      d8  8b,dPPYba,   88             88 `8b     d8' 88  88         88
88        88  88P'   `"8a  88 ,a8"    88P'   `"8a  a8"     "8a  `8b    d88b    d8'  88P'   `"8a  88             88  `8b   d8'  88  88         88
88        88  88       88  8888[      88       88  8b       d8   `8b  d8'`8b  d8'   88       88  Y8,            88   `8b d8'   88  88         8P
Y8a.    .a8P  88       88  88`"Yba,   88       88  "8a,   ,a8"    `8bd8'  `8bd8'    88       88   Y8a.    .a8P  88    `888'    88  88      .a8P
 `"Y8888Y"'   88       88  88   `Y8a  88       88   `"YbbdP"'       YP      YP      88       88    `"Y8888Y"'   88     `8'     88  88888888Y"'

"""

print(watermark)
print('installing dependencies (Unless you installed them ofc)')


#Try to import modules error in importing results in installation
try:
    import os
except ImportError:
    print('Sorry bruh yo missing phat module n i gotta get phat\n')
    os.system('python -m pip install os') #Not sure if os is a module or not so just incase
import os

try:
  import requests
except ImportError:
  print "Trying to Install required module: requests\n"
  os.system('python -m pip install requests')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
    print(error_import)
import requests

try:
    import pywin32
except ImportError:
    print('Not again i forgot my keys at home now i gotta go and get them\n')
    os.system('python -m pip install pywin32')
    print(error_import)
    import pywin32

try:
    import keyboard
except ImportError:
    print("Man you ain't got this either?\n")
    os.system('python -m pip install keyboard')
    print(error_import)
    import keyboard

try:
    import pygame
except ImportError:
    print("Honestly I'm running out of insults for you")
    print('Importing pygame for yo lazy ass')
    os.system('Python -m pip install pygame')
    print(error_import)
    import pygame

try:
    import pyscreenshot
except ImportError:
    print("Now you can't be serious")
    print("Installing you modules")
    os.system(python -m pip install pyscreenshot)
    print(error_import)
    import pyscreenshot

try:
    import imutils
except ImportError:
    print('WTF KYLE')
    print('You know the deal installing for you')
    os.system('python -m pip install imutils')
    print(error_import)
    import imutils

try:
    import numpy
except ImportError:
    print('OMG YOURE SUCH A NUUB')
    print('Imma still install it for you tho ;)')
    os.system('python -m pip install numpy')
    print(error_import)
    import numpy

try:
    import argparse
except ImportError:
    print("""99 little bugs in the code.
    99 little bugs in the code.
    take one down, pathc it around.
    127 little bugs in the code...""")
    print('Enjoyed the little joke? guess not as this is to quick to read anyways installing for ya')
    os.system('python -m pip install argparse')
    print(error_import)
    import argparse

try:
    import opencv-python
except ImportError:
    print(""""Spent the last three and a half hours trying to figure out how to do os.system correctly""")
    print('Installing my pennies')
    os.systsem('python -m pip install opencv-python')
    print(error_import)
    import opencv-python

try:
    import pyautogui
except ImportError:
    print("Not sure if I'm good at programming... or good at googling")
    print('anyhow u know the deal imma install this 4 ya')
    os.system('python -m pip install pyautogui')
    print(error_import)
    import pyautogui

try:
    import urllib
except ImportError:
    print('DONT PANIC!')
    print('installing it for ya you scallywag')
    os.system(python -m pip install urllib)
    print(error_import)
    import urllib

print("""now that the dependencies are over imma work on the important files for ya""")


# Makes createFolder function aka it makes folders fucking basic bs
def createFolder(directory):
    try:
        if os.path.exists(directory):
            print('Nural_Network directory exists skipping step')

        if not os.path.exists(directory):
            os.makedirs(directory)
            print ('Making folder for the nural network in current working directory')
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#make folder called Nural_Network
createFolder('./Nural_Network/')

#Request raw post of MobileNetSSD_deploy.prototxt
r = requests.get('https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/MobileNetSSD_deploy.prototxt')

print('Getting MobileNetSSD_deploy.prototxt from https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/MobileNetSSD_deploy.prototxt')

'Requests:' in r.text
r.headers['Content-Type']
r = requests.get('https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/MobileNetSSD_deploy.prototxt')
'Requests:' in r.text
r.headers['Content-Type']

#Writes the content of raw paste in MobileNetSSD_deploy.prototxt
with open('./Nural_Network/MobileNetSSD_deploy.prototxt', 'a') as output:
    output.write(r.text)
print('Importing MobileNetSSD_deploy.caffemodel from https://github.com/C-Aniruddh/realtime_object_recognition/raw/master/MobileNetSSD_deploy.caffemodel')


#using cleaner method after being informed by gooogle XD
deploy = urllib.URLopener()
deploy.retrieve("https://github.com/chuanqi305/MobileNet-SSD/raw/master/MobileNetSSD_deploy.caffemodel", "./Nural_Network/MobileNetSSD_deploy.caffemodel")

print("it's almost over now just one more thing")
