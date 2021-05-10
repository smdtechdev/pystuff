import pyautogui

w, h = pyautogui.size()

print(w, h, pyautogui.position())

#pyautogui.moveTo(50, 10, duration=2)

#pyautogui.moveRel(80, 400, duration=2)

#pyautogui.moveTo(122, 402, duration=2)

#pyautogui.click()

#pyautogui.typewrite('Hello World', interval=0.25)

#pyautogui.typewrite(['e','y','left','left','H', 'right', 'right', 'space', 'Y','o','u','.'], interval=0.25)
#print(pyautogui.KEYBOARD_KEYS)

#pyautogui.press('f5')

#pyautogui.hotkey('ctrl','n')

#pyautogui.screenshot('Automation\\files\\ss.png')

print(pyautogui.locateOnScreen('Automation\\files\\ot.png'))

print(pyautogui.locateCenterOnScreen('Automation\\files\\ot.png'))