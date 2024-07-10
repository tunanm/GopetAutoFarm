import math
import os
import time
import cv2
import pyautogui as gui
from GameWindownSetUp import bring_window_to_foreground,re_login_and_move_to_road_to_mountain
from NearestMonsterPosition import find_nearest_monster
from Moving import moving_avatar,hold_key
from ultralytics import YOLO
from ImagesClassifierFeatureDetectors import map_object_detect
from CaptchaAutoFill import  send_captcha_email

model = YOLO('.venv/Lib/site-packages/ultralytics/best.pt')

classNames = ["Cat2","Death1","Minion1","Monkey1",
             "Monkey2","MyAvatar","Pikachu1","PigBoss",
             "Rabbit2","Sekeleton2","Snake2","Turtle2",
             "Unicorn","WillOWisp2","WillOWisp1","WrathDragon2","SakuraTree"]

skill_press = ['0','1','2','3','4']
total_mana = 5600
mana_cost = []
boss_skill_pattern = []
skill_use = 1

realtime_map = "Resources/GameMapRealTime"
cliff_directory = "Resources/Cliff"
captcha = "Resources/CaptchaDetect"
boss_info = 'Resources/BossInfo'

realtime_path = []
cliff_path = []
captcha_path = []
boss_path = []


# Bring game windown to screen

ind = 0

# Get the directory from resources
def get_directory_path(directory, array):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_path = os.path.normpath(file_path)
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            array.append(file_path)
    return array
# Skill kill boss
def boss_pattern():
    hold_key(0.3, '2')
    time.sleep(0.3)
    hold_key(0.3, '1')
    time.sleep(0.3)
    hold_key(0.3, '3')
    time.sleep(3)
def get_user_input():
    global total_mana, mana_cost, skill_use, boss_skill_pattern
    total_mana = int(input('total mana:'))
    skill_use = int(input('skill use(Eg: 1, 0 define for do nothing):'))
    skill_mana_count = int(input('number of skills for input array mana cost:'))
    for i in range(0,skill_mana_count):
        temp = int(input(f'Mana of {i} skill use:'))
        mana_cost.append(temp)
    skill_boss_pattern_num = int(input('number of skill use when match boss:'))
    for i in range(0,skill_boss_pattern_num):
        temp = str(input(f'Skill {i} is:'))
        boss_skill_pattern.append(temp)

# GetMapRealTime


# Detect avatar positions
# Example of how to start capture in a separate thread
if __name__ == "__main__":
    realtime_path = get_directory_path(realtime_map, realtime_path)
    cliff_path = get_directory_path(cliff_directory, cliff_path)
    boss_path = get_directory_path(boss_info, boss_path)
    captcha_path = get_directory_path(captcha,captcha_path)
    bring_window_to_foreground('Gopet2D')
    get_user_input()
    time.sleep(2)
    #packet_capture_thread()
    while True:
        #Get realtime map
        screen_shot = gui.screenshot(region=(0, 0, 850, 520))
        screen_shot.save(realtime_path[0])
        results = model.predict(realtime_path[0])
        avatar_positions = []
        monster_positions = []
        ciff_positions = map_object_detect(cliff_path[0],realtime_path[0])
        boss_fightting = map_object_detect(boss_path[0],realtime_path[0])
        captcha_exists = map_object_detect(captcha_path[0],realtime_path[0])
        if len(captcha_exists) > 0:
            cv2.waitKey()
        else:
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x, y, w, h = box.xywh[0]
                    x, y, w, h = int(x),int(y),int(w),int(h)
                    # Confidence
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    # Class Name
                    cls = int(box.cls[0])
                    currentClass = classNames[cls]
                    # Detec avatar positions
                    if currentClass == "MyAvatar" and conf >= 0.7:
                        avatar_positions.append((x + w/2,y + h, w, h))
                    # Detec monster positions
                    if currentClass != "MyAvatar" and currentClass != "SakuraTree" and conf >= 0.7:
                        monster_positions.append((x + w/2,y + h, w, h))
            # Find the nearest monster for each avatar
            nearest_monsters = []
            if len(avatar_positions) > 0 and len(monster_positions) > 0:
                nearest_monsters = find_nearest_monster(avatar_positions, monster_positions)
            if len(nearest_monsters) > 0:
                avatar_postition,monster_position = nearest_monsters[0][:2]
                print("avatar" + str(avatar_postition))
                print("monster" + str(monster_position))
                print("cliff" + str(ciff_positions))
                if len(boss_fightting) > 0:
                    print('boss')
                    moving_avatar(avatar_postition,monster_position, ciff_positions,boss_skill_pattern, total_mana, int(mana_cost[skill_use]))
                else:
                    moving_avatar(avatar_postition, monster_position, ciff_positions, skill_press[skill_use], total_mana,
                                  int(mana_cost[skill_use]))
                    print('normal monster')
            else:
                print('There no avatar or nerest monster')
                if ind % 2 == 0:
                    hold_key(0.4, 'right')
                    hold_key(0.2, 'down')
                else:
                    hold_key(0.4, 'left')
                    hold_key(0.2, 'down')
                ind+=1
                # testpass
                #re_login_and_move_to_road_to_mountain()
