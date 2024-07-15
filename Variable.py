from ultralytics import YOLO

realtime_map_directory = "Resources\\GameMapRealTime\\map.png"
cliff_directory = "Resources\\Cliff\\Ladder.png"
captcha_directory = "Resources\\CaptchaDetect\\detect.png"
boss_info_directory = 'Resources\\BossInfo\\atk.png'
session_directory = 'Resources\\Session\\session.png'
captcha_file_path = 'Resources\\Captcha\\captcha.jpg'
login_screen_directory = 'Resources\\LoginScreen\\login_screen.png'
wrong_captcha_directory = 'Resources\\WrongCaptcha\\Wrongcaptcha.png'
model = YOLO('.venv/Lib/site-packages/ultralytics/best.pt')

classNames = ["Cat2","Death1","Minion1","Monkey1",
             "Monkey2","MyAvatar","Pikachu1","PigBoss",
             "Rabbit2","Sekeleton2","Snake2","Turtle2",
             "Unicorn","WillOWisp2","WillOWisp1","WrathDragon2","SakuraTree"]
skill_press = ['0','1','2','3','4']
