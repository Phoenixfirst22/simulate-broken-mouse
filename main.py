import win32api
import random
import keyboard
######################
k = random.randint(-12, 12)

k2 = random.randint(-12, 12)
######################




while keyboard.is_pressed("esc") == False:
    k = random.randint(-12, 12)

    k2 = random.randint(-12, 12)

    x, y = win32api.GetCursorPos()

    cos = win32api.GetCursorPos()

    if cos != win32api.GetCursorPos():
        win32api.SetCursorPos((x + k, y + k2))













