'''
WC indtil fuld inv - sacrifice - wc igen.

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

def feedFire():
    if Version.lower() == "desktop":
        pyautogui.moveTo(1697, 56)
        time.sleep(np.random.uniform(0.3,0.5))
        pyautogui.click(1697, 56)
        time.sleep(np.random.uniform(0.3,0.5))
        moveClick(1633, 191)
        time.sleep(np.random.uniform(2,3))
        moveClick(1180, 211)
    else:
        pyautogui.moveTo(1581, 67)
        time.sleep(0.1)
        pyautogui.click(1581, 67)
        time.sleep(0.2)
        pyautogui.moveTo(1497, 297)
        time.sleep(0.2)
        pyautogui.click(1497, 297)
        #moveClick(1497, 297)
        time.sleep(2.6)
        pyautogui.moveTo(801, 307)
        time.sleep(1.7)
        pyautogui.click(801, 307)
        #moveClick(801, 307)
    

def checkIfChopping(region):
    #Capture screenshot
    screenshot = pyautogui.screenshot(region=region) #Pc = (1847, 390, 25, 25)

    #Convert the screenshot to a NumPy array for OpenCV:
    screenshot_np = np.array(screenshot)

    #Convert the color you want to check for:
    target_color = (12, 85, 215)  #rgb(12, 85, 215)præcise blå hvis den generelle blå ikke virker
    
    #Check if color is there
    mask = cv2.inRange(screenshot_np, target_color, target_color)
    color_present = np.any(mask)

    if color_present:
        print("Target color present - feeding fire.") 
        feedFire()
    else:
        time.sleep(np.random.uniform(0.5,1))

while not keyboard.is_pressed("q"):
    if Version.lower() == "desktop":
        pcRegion= (1847, 463, 25, 25)
        checkIfChopping(pcRegion)
    else:
        laptopRegion = (1738, 692, 35, 35) #1806 Y:  692 1738 Y:  695
        checkIfChopping(laptopRegion)






#If i recall correctly - i was experimenting with if the script was able to find the fire on its own. Looks like i didn't succeed.
'''def findFirenew():
    #Load the Object image and Convert to Grayscale
    object_image = cv2.imread('Celefire.png', cv2.IMREAD_GRAYSCALE)

    #Intialize ORB Detector
    orb = cv2.ORB_create()

    #Detect ORB Keypoints and Descriptors for the Object Image
    kp_object, des_object = orb.detectAndCompute(object_image, None)

    #Capture the Screenshot and Convert to Grayscale:
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    #Detect ORB Keypoints and Descriptors for the Screenshot:
    kp_screenshot, des_screenshot = orb.detectAndCompute(screenshot_gray, None)

    #Match the Keypoints:
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des_object, des_screenshot)

    #Sort Matches by Distance:
    matches = sorted(matches, key=lambda x: x.distance)

    #Define a Threshold for Matching:
    match_threshold = 0.7
    good_matches = [m for m in matches if m.distance < match_threshold]


    # Extract coordinates of matched keypoints
    matched_points = [(int(kp_screenshot[m.trainIdx].pt[0]), int(kp_screenshot[m.trainIdx].pt[1])) for m in good_matches]

    # Perform an action (e.g., click) on each matched point
    for x, y in matched_points:
        pyautogui.click(x, y)


    #Draw the Matches:
    #img_matches = cv2.drawMatches(object_image, kp_object, screenshot_gray, kp_screenshot, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


 



def findFire():
    # Define the region where you want to search for the object
    region_x, region_y = 1157, 34  # Top-left corner coordinates of the region
    region_width, region_height = 515, 340  # Width and height of the region

    # Capture a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(region_x, region_y, region_width, region_height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # Load the image of the object you want to search for
    fireImage = cv2.imread('Celefire1.png') 

    # Perform template matching
    result = cv2.matchTemplate(screenshot, fireImage, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Define a threshold for a match
    threshold = 0.5

    # Check if a match is found
    if max_val >= threshold:
        # Get the coordinates of the match
        match_x, match_y = max_loc
  
        # Calculate the center coordinates of the matched region
        match_center_x = match_x + region_x + region_width // 2
        match_center_y = match_y + region_y + region_height // 2
   
        # Perform actions on the matched object using PyAutoGUI (for example, click on it)
        moveClick(match_center_x, match_center_y)
    else:
        print("Object not found in the region.")

    # Display the screenshot with the match (for debugging purposes)
    cv2.imshow('Screenshot with Match', screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



findFirenew()
'''