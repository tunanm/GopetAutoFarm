import pyautogui as gui
import time

monster_count = 0
moving_speed = 135


def hold_key (hold_time,keypress):
    gui.keyDown(keypress)
    time.sleep(hold_time)
    gui.keyUp(keypress)

def moving_avatar(avatar, monster):
    global monster_count
    if monster_count > 30:
        time.sleep(3)
        hold_key(0.5, 'space')
        hold_key(20, '1')
        monster_count = 0
    avatar_center_bottom_x, avatar_center_bottom_y = avatar[:2]
    monster_center_bottom_x, monster_center_bottom_y = monster[:2]
    if avatar_center_bottom_x < monster_center_bottom_x:
        hold_time = (monster_center_bottom_x - avatar_center_bottom_x)/moving_speed
        hold_key(hold_time, 'right')
    if avatar_center_bottom_x > monster_center_bottom_x:
        hold_time = (avatar_center_bottom_x - monster_center_bottom_x)/moving_speed
        hold_key(hold_time, 'left')
    if avatar_center_bottom_y > monster_center_bottom_y:
        hold_time = (avatar_center_bottom_y - monster_center_bottom_y)/moving_speed
        hold_key(hold_time, 'up')
    if avatar_center_bottom_y < monster_center_bottom_y:
        hold_time = (monster_center_bottom_y - avatar_center_bottom_y)/moving_speed
        hold_key(hold_time, 'down')
    time.sleep(1)
    hold_key(0.5,'3')
    monster_count += 1
    time.sleep(3)



