import random
import time
import win32con,win32gui
import pyautogui
from Moving import hold_key

login_position = (424,490)
#x=328, y=605 640*640 resolutios
logout_position = (188,472)
#x=232, y=581 640*640 resolution
function_position = (110,470)
#x=134, y=581 640*640 resolution
more_option = (771,484)
#x=566, y=595 640*640 resolution
change_area = (742,290)
#x=498, y=346 640*640 resolution
area_position = [(703,330),(762,330),(640,395),(700,395),(763,395),(637,461),(705,461)]

def bring_window_to_foreground(window_title):
    # Find the window by its title
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print(f"Window '{window_title}' not found.")
        return
    else:
        set_window_position(hwnd, 0, 0, 850, 520)
    # Bring the window to the foreground
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore if minimized
    win32gui.SetForegroundWindow(hwnd)
# Set game size and position prepare for gui.screenshot
def set_window_position(hwnd, x, y, width, height):
    # Set the window position and size
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, width, height, win32con.SWP_SHOWWINDOW)

def re_login_and_move_to_road_to_mountain():
    pyautogui.click(login_position)
    time.sleep(2)
    hold_key(4, 'left')
    time.sleep(0.1)
    hold_key(0.8, 'right')
    hold_key(2, 'up')
    hold_key(2, 'left')
    pyautogui.click(more_option)
    time.sleep(0.3)
    pyautogui.click(change_area)
    time.sleep(0.3)
    pyautogui.click(area_position[random.randint(0, 6)])
    time.sleep(0.3)
def logout():
    pyautogui.click(login_position)
    time.sleep(0.5)
    pyautogui.click(function_position)
    time.sleep(0.5)
    pyautogui.click(logout_position)
    time.sleep(0.5)