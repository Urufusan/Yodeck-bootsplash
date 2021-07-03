#!/usr/bin/python3
import sys
import os
from PIL import Image #Importing PIL (Pillow)
if os.geteuid()==0: #root check
  print("Yodeck bootsplash changer -- Made by P.M.") #start screen
else:
  sys.exit("The program is not running as root!") 

def locmove(loclocal):
    cmd1 = "cp "+loclocal+" /tmp/tempwgetpic."+ext1 #Function for moving the image 
    os.system(cmd1)
    

def wgetprog(locwget):
    cmd2 = "wget "+locwget+" -O /tmp/tempwgetpic."+ext1 #Wget blob 
    os.system(cmd2)

def resizeimg():   #Image manipulation for the boot image (Always in 16:9 Asp. Ratio, 1080p)
    ext2 = "/tmp/tempwgetpic."+ext1
    ext3 = ext2+"."+ext1 #String reformating || tempwgetpic.(something) --> jpg
    Image.open(ext2).convert('RGB').save(ext3)      
    slika0 = Image.open(ext3)
    slika1 = slika0.resize((1920, 1080))
    slika1.save('/tmp/tempwgetpicR.jpg') #Output image
    
def imgbootset():
    os.system("mv /tmp/tempwgetpicR.jpg /usr/share/yodeck/resources/YoDeck_1080p.jpg") #Output image moving func.

print("Type in the location of the wanted image file for the splash screen || 'local' or 'URL' ")
ans1 = input(">> ")
if ans1 == "local":
    print("Type in the location of the image file on the local disk:") #The menu bla bla bla....
    loc1 = input(">> ")
    if not loc1:
        sys.exit("Wrong input!")
    if loc1.endswith('jpg'):  ##Checking filetype
        ext1 = "jpg"
    elif loc1.endswith('png'):
        ext1 = "png"
    else:
        sys.exit("Wrong filetype!")
    print("Copying image....")
    locmove(loc1)
    resizeimg()
    imgbootset()
    print("Task finished!")
    print("Reboot the RPi using 'reboot' or 'sudo reboot'!")

elif ans1 == "URL":
    print("Type in the URL of the image:")
    loc2 = input(">> ")
    if not loc2:
        sys.exit("Wrong input!")
    if loc2.endswith('jpg'):
        ext1 = "jpg"  ##Checking filetype
    elif loc2.endswith('png'):
        ext1 = "png"
    else:
        sys.exit("Wrong filetype!")        
    print("Downloading image....")
    wgetprog(loc2)
    resizeimg()
    print("Overwriting image....")
    imgbootset()
    print("Task finished!")
    print("Reboot the RPi using 'reboot' or 'sudo reboot'!")
else:
    print("Wrong input!")
    
