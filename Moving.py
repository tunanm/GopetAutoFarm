import math
import pyautogui as gui
import time

monster_count = 0
moving_speed = 135
#160 old value with hwnd, 0, 0, 640, 640


def hold_key (hold_time,keypress):
    if keypress != '0':
        gui.keyDown(keypress)
        time.sleep(hold_time)
        gui.keyUp(keypress)
    else:
        time.sleep(2)

def moving_avatar(avatar, monster, ciff_positions, keypress, total_mana, mana_cost):
    global monster_count
    if mana_cost != 0 and monster_count > math.floor(total_mana/mana_cost):
        time.sleep(3)
        hold_key(0.5, 'space')
        hold_key(20, '1')
        monster_count = 0
    avatar_center_bottom_x, avatar_center_bottom_y = avatar[:2]
    monster_center_bottom_x, monster_center_bottom_y = monster[:2]
    moving_ciff_path = False
    if len(ciff_positions) > 0:
        cliff_center_bottom_x,cliff_center_bottom_y,w,h = ciff_positions[0][:]
        cliff_center_bottom_y = cliff_center_bottom_y - h/2
        if (avatar_center_bottom_y < cliff_center_bottom_y
            and cliff_center_bottom_y < monster_center_bottom_y) or (avatar_center_bottom_y > cliff_center_bottom_y
            and cliff_center_bottom_y > monster_center_bottom_y):
            moving_ciff_path = True
    if moving_ciff_path:
        moving_cliff_roadmap(avatar,monster,ciff_positions,keypress)
    else:
        moving_nomal_roadmap(avatar,monster,keypress)

def moving_nomal_roadmap(avatar,monster,keypress):
    global monster_count
    print('move normal pattern')
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
    for key in keypress:
        time.sleep(1.5)
        hold_key(0.3,key)
    monster_count += 1

def moving_cliff_roadmap(avatar,monster,ciff_positions,keypress):
    global monster_count
    print('move cliff pattern')
    avatar_center_bottom_x, avatar_center_bottom_y = avatar[:2]
    monster_center_bottom_x, monster_center_bottom_y = monster[:2]
    cliff_center_bottom_x, cliff_center_bottom_y, w, h = ciff_positions[0][:]
    hold_time = abs(cliff_center_bottom_x - avatar_center_bottom_x) / moving_speed
    if cliff_center_bottom_x > avatar_center_bottom_x:
        hold_key(hold_time, 'right')
    else:
        hold_key(hold_time, 'left')
    if (avatar_center_bottom_y < cliff_center_bottom_y
            and cliff_center_bottom_y < monster_center_bottom_y):
        hold_time = (monster_center_bottom_y - avatar_center_bottom_y) / moving_speed
        hold_key(hold_time, 'down')
    if (avatar_center_bottom_y > cliff_center_bottom_y
            and cliff_center_bottom_y > monster_center_bottom_y):
        hold_time = (avatar_center_bottom_y - monster_center_bottom_y) / moving_speed
        hold_key(hold_time, 'up')
    if cliff_center_bottom_x > monster_center_bottom_x:
        hold_time = (cliff_center_bottom_x - monster_center_bottom_x) / moving_speed
        hold_key(hold_time, 'left')
    if cliff_center_bottom_x < monster_center_bottom_x:
        hold_time = (monster_center_bottom_x - cliff_center_bottom_x) / moving_speed
        hold_key(hold_time, 'right')
    for key in keypress:
        time.sleep(1.5)
        hold_key(0.3,key)
    monster_count += 1




