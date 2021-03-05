import pyautogui
import subprocess
import win32gui
import time

print('start')

wh = pyautogui.size()
print(wh)


def mouse_move_test(cnt: int = 1):
    for i in range(cnt):
        pyautogui.move(100, 0, duration=0.25)   # right
        pyautogui.move(0, 100, duration=0.25)   # down
        pyautogui.move(-100, 0, duration=0.25)  # left
        pyautogui.move(0, -100, duration=0.25)  # up


# move mouse
# for i in range(2):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)

mouse_move_test()

# mouse position
mouse_pos = pyautogui.position()
print(mouse_pos)
# click
pyautogui.click()
# scroll
pyautogui.scroll(100)

# info = pyautogui.mouseInfo()
# print(info)

# screenshot
im = pyautogui.screenshot()
im.save(r'pyboringstuff\input_data\cp20\sc.png')

try:
    pyautogui.locateOnScreen(r'pyboringstuff\input_data\cp20\sc2.png')
except:
    print('file not found')

# manipulating window
fw = pyautogui.getActiveWindow()
fw.topleft = (50, 100)

# proc = subprocess.Popen(r'c:\windows\system32\notepad.exe')
proc = subprocess.Popen(['start', 'notepad'], shell=True)
time.sleep(2)
# メモ帳をactiveにする
memoapp = win32gui.FindWindow(None, '無題 - メモ帳')
win32gui.SetForegroundWindow(memoapp)
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 0, 0, 500, 500, True)


time.sleep(1)
pyautogui.write('hello,world', 0.1)
pyautogui.write(['enter'])
pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

pyautogui.hotkey('ctrl', 'a')

# time.sleep(2)  # ウエイト

rtn = pyautogui.confirm('Are you finish?')
print(rtn)

print('end')
