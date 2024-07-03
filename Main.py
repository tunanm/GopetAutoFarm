import math
import os
import threading
import time
import pyautogui as gui
from GameWindownSetUp import bring_window_to_foreground,re_login_and_move_to_road_to_mountain
from NearestMonsterPosition import find_nearest_monster
from Moving import moving_avatar,hold_key
from ultralytics import YOLO
from CapturePacket import packet_capture_thread
from ImagesClassifierFeatureDetectors import map_object_detect

flag_boss = False
model = YOLO('.venv/Lib/site-packages/ultralytics/best.pt')

classNames = ["Cat2","Death1","Minion1","Monkey1",
             "Monkey2","MyAvatar","Pikachu1","PigBoss",
             "Rabbit2","Sekeleton2","Snake2","Turtle2",
             "Unicorn","WillOWisp2","WillOWisp1","WrathDragon2"]

realtime_map = "Resources/GameMapRealTime"
cliff_directory = "Resources/Cliff"
realtime_path = []
cliff_path = []
test_image_captcha = "D:\\Code\\GoPetAutoFarm\\Resources\\Captcha\\"

# Bring game windown to screen


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



# Detect avatar positions
# Example of how to start capture in a separate thread
if __name__ == "__main__":
    realtime_path = get_directory_path(realtime_map, realtime_path)
    cliff_path = get_directory_path(cliff_directory, cliff_path)
    bring_window_to_foreground('Gopet2D')
    time.sleep(2)
    #packet_capture_thread()
    while True:
        #Get realtime map
        screen_shot = gui.screenshot(region=(0,0,640,640))
        screen_shot.save(realtime_path[0])
        results = model.predict(realtime_path[0])
        avatar_positions = []
        monster_positions = []
        ciff_positions = map_object_detect(cliff_path[0],realtime_path[0])
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
                if currentClass == "MyAvatar" and conf >= 0.5:
                    avatar_positions.append((x + w/2,y + h, w, h))
                # Detec monster positions
                if currentClass != "MyAvatar" and conf >= 0.5:
                    monster_positions.append((x + w/2,y + h, w, h))
        # Find the nearest monster for each avatar
        nearest_monsters = []
        if len(avatar_positions) > 0 and len(monster_positions) > 0:
            nearest_monsters = find_nearest_monster(avatar_positions, monster_positions)
        if len(nearest_monsters) > 0:
            avatar_postition,monster_position = nearest_monsters[0][:2]
            moving_avatar(avatar_postition,monster_position, ciff_positions,'3', 3600, 140)
        else:
            print('There no avatar or nerest monster')
            if flag_boss:
                boss_pattern()
            else:
                hold_key(0.3, 'up')
                hold_key(0.3, 'down')
                # testpass
                #re_login_and_move_to_road_to_mountain()
