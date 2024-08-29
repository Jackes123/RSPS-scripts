'''
Task:
1. Højre click "Instance Token(u)" og trykke "Last Instance"
2. Flyt karakteren ind i midten enten ved at højre click og trykke "Walk here" ellers skal
man bare bruge melee våben
3. Attack en af mobsene i midten (sørg for at at hvis man mister aggro så skal man attack igen)
4. Rinse og repeat i guess (efter et lille delay)
'''
import time
import pyautogui
import keyboard
import cv2
import numpy as np
from PIL import Image

Version = input("Desktop eller laptop:")

#Flytter musen og højreclicker
def moveRightClick(x,y):
    pyautogui.moveTo(x, y)
    time.sleep(np.random.uniform(1,2))
    pyautogui.rightClick(x, y)
    time.sleep(np.random.uniform(1,2))

#Flytter musen og venstreclicker
def moveClick(x,y):
    pyautogui.moveTo(x, y)
    time.sleep(np.random.uniform(1,2))
    pyautogui.click(x, y)
    time.sleep(np.random.uniform(1,2))

#Attack sequence i rigtig rækkefølge, alle de forskellige koordinaterne er til både desktop og laptop
def attackSequence():
    if Version.lower() == "desktop":
        moveRightClick(1815,433)
        moveClick(1783, 465)
        moveClick(1694, 53)
        moveClick(1407, 98)
        #moveClick(1394,128)
        time.sleep(np.random.uniform(0.5, 1))
        moveClick(1397,168)


    else:
        moveRightClick(1754, 661)
        moveClick(1710,691)
        moveClick(1581,77)
        moveClick(1153,163)
        time.sleep(np.random.uniform(0.5, 1))
        moveClick(1117,269)


#Funktion til at checke om der er gule prikker i minimap = mobs
def checkYellow(region): 
    #Take screenshot and do stuff with it
    Minimap = pyautogui.screenshot(region=region)
    Minimap_np = np.array(Minimap)
    yellow_lower = np.array([200, 200, 0], dtype=np.uint8)
    yellow_upper = np.array([255, 255, 100], dtype=np.uint8)
    yellow_mask = cv2.inRange(Minimap_np, yellow_lower, yellow_upper)
    return cv2.countNonZero(yellow_mask) <= 0

#Funktion der checker en region om der er rødt eller grønt hvilket vil sige jeg fighter
def checkaggro(region,color): 
    fightzone = pyautogui.screenshot(region=region) #1313 Y:   84
    fightzone_np = np.array(fightzone)

    if color == "green":
        lower_color = np.array([0, 100, 0], dtype = np.uint8)#lower og upper er threshold for grøn
        upper_color = np.array([100, 255, 100], dtype=np.uint8)
    elif color == "red":
        lower_color = np.array([0, 0, 100], dtype = np.uint8)
        upper_color = np.array([100, 100, 255], dtype = np.uint8)
    else:
        print("Images are not similar (MSE: {:.2f})".format(mse))
        return False
        raise ValueError ("Invalid color specified")
    color_mask = cv2.inRange(fightzone_np, lower_color, upper_color)
    return cv2.countNonZero(color_mask) > 0
    


while not keyboard.is_pressed("q"):
    if Version.lower() == "desktop":
        desktopRegion = (1750,90,70,70)
        region = (1313, 84, 200, 250)
        is_green_present = checkaggro(region, "green")
        #is_red_present = checkaggro(region, "red")

        if checkYellow(desktopRegion):
            print("AttackSequence")
            attackSequence()
            time.sleep(np.random.uniform(1, 2))
        else:
            time.sleep(np.random.uniform(2, 5))

            if is_green_present: # or is_red_present
                print("Currently fighting")
                print("\n")
                time.sleep(np.random.uniform(1, 2))

            else:
                print ("Lost aggro, regaining aggro. -.-")
                moveClick(1390,175)
                time.sleep(np.random.uniform(5, 10))

    else: #LAPTOP
        laptopRegion = (1670,115,90,90)
        region = (1138,98,300,250)
        is_green_present = checkaggro(region, "green")

        if checkYellow(laptopRegion):
            print("Attack Sequence")
            attackSequence()
            time.sleep(np.random.uniform(1, 2))
        else:
            time.sleep(np.random.uniform(1, 2))

            if is_green_present: # or is_red_present
                print("Currently fighting")
                print("\n")
                time.sleep(np.random.uniform(1, 2))
            else:
                print ("Lost aggro, regaining aggro. -.-")
                moveClick(1117,269)
                time.sleep(np.random.uniform(1, 3))







'''
#Denne function samligner et screenshot jeg har taget med en region på skærmen. Hvoraf den afgør om jeg har mistet aggro
def checkForLostAggro(x, y, w, h, image): # PC1300,75,250,225 "LostaggroPC.png" Laptop: 
    takescreen = pyautogui.screenshot(region= (x, y, w, h))
    referenceImage = Image.open(image)
    referenceArray = np.array(referenceImage)
    screenshotArray =np.array(takescreen)

    mse = np.mean((referenceArray - screenshotArray)**2)
    threshold = 30 # Adjust as needed
    if mse < threshold:
        print("Images are similar (MSE: {:.2f})".format(mse))
        return True
    else:
        print("Images are not similar (MSE: {:.2f})".format(mse))
        return False


                #Til PC
                    if checkForLostAggro(1300,75,250,225, "asslostagropc.png"): #"asslostagropc.png" - "LostaggroPC.png"
                print ("Lost aggro, regaining aggro. -.-")
                moveClick(1390,175)
                time.sleep(np.random.uniform(1, 2))


                #Til Desktop
                    if checkForLostAggro(1138,98,300,250, "Asslostagrolap.png"):#Asslostagrolap.png - LostaggroLaptop.png
                print ("Lost aggro, regaining aggro. -.-")
                pyautogui.click(1117,269)
                time.sleep(np.random.uniform(1, 2))
'''

'''#Funktion der tager et screenshot af en region
def captureScreenshot(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

#Converter ovennævnte screenshot til grå
def convertScreenToGray(image):
    grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return grayImage

#Samligner billeder
def compareImages(image1, image2):
    difference = cv2.absdiff(image1, image2)
    return difference
'''