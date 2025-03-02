import pyautogui
import time
import json
import random
import string

# Fail-safe feature - move mouse to upper left corner to abort
pyautogui.FAILSAFE = True
        
def main():
    print("Get ready to work!")
    
    # load JSON and text data
    with open('script/formatted.json', 'r') as file:
        data = json.load(file)    

    with open('script/sampleDocument.txt', 'r') as file:
        document = file.read()
        
    keyCount = 0
    time.sleep(5)
    
    # main loop
    for i in range(100207):
        t = str(i)
        if t not in data:
            continue

        task = data[t]
         
        if "x" in task and task["x"] != False:
            if task["x"] == 0 and task["y"] == 0:
                continue
            pyautogui.moveTo(task["x"], task["y"], duration = .2)
        else:
            # mistype + backspace:
            if random.random() < .05:
                letter = random.choice(string.ascii_lowercase)
                pyautogui.typewrite(letter)
                time.sleep(.3)
                pyautogui.press('backspace')
                time.sleep(.3)
            else:
                pyautogui.typewrite(document[keyCount])
                keyCount += 1
                
        time.sleep(.01)

main()