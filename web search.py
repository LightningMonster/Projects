import random, string, pyautogui, time
numbers=random.randint(1000000000, 1000000000000)
c = 0

time.sleep(3)
while c < 30:
 r = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(5)))
 time.sleep(0.5)
 pyautogui.click(400, 150)
 pyautogui.click(400, 150)
 time.sleep(0.5)
 pyautogui.keyDown('ctrl')
 pyautogui.press("a")
 pyautogui.keyUp('ctrl')
 time.sleep(0.5)
 pyautogui.keyDown('backspace')
 time.sleep(0.2)
 pyautogui.keyUp('backspace')
 time.sleep(0.5)
 pyautogui.write(str(r))
 time.sleep(0.5)
 pyautogui.press('enter')
 c=c+1
 print(c)