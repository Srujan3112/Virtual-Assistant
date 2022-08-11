import os
import random

from speak_module import speak

def change_wallpaper():
    wallpaper_path = '/home/srujan/Pictures'
    wallpapers = os.listdir(wallpaper_path)
    wallpaper = random.choice(wallpapers)
    command = 'gsettings set org.gnome.desktop.background picture-uri file:///'+ wallpaper_path +"/" + wallpaper
    os.system(command)
    speak("wallpaper changed")
