import os

from pyttsx3 import speak 
import file_search



music_path = "/home/srujan/Music"

def play_music():
    
    os.system("rhythmbox-client --play")
    return "Playing Music"

def pause_music():
        os.system("rhythmbox-client --pause")
        return "Music paused"
  
def stop_music():
        os.system("rhythmbox-client --stop")
        return "Music stopped"

def next_song():
        os.system("rhythmbox-client --next")
        return "Playing next song"

def previous_song():
        os.system("rhythmbox-client --previous")
        return "Playing previous song"

def play_specific_song(song_name):

    song_name = song_name.replace('play', '')
    file_search.set_root(music_path)
    songs = file_search.searchFile(song_name)
    try:
        song_uri = songs[0]
        command = 'rhythmbox-client --play-uri="' + song_uri + '"'
        os.system(command)
        return ("playing  " + song_name)
    except:
        return("song not found in your computer")
        
def handle_music(query):
    if "play music" in query:
        speak("playing music")
        speak("playing music")

        play_music()
    elif "next song" in query:
        speak("playing next song")
        speak("playing next song")

        next_song()
    elif "previous song" in query:
        speak("playing previous song")
        print("playing previous song")
        previous_song()


