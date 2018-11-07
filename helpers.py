import glob
import pygame

# return a dict of available audio files
# the filename base is used as the key and the file path is used as the value
def get_audio_files():
    filepaths = glob.glob('static/audio/*.wav')
    keys = [path[13:] for path in filepaths]
    return dict(zip(keys, filepaths))

def play_audio(filepath):
    print("Playing audio from file", filepath)
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy() == True:
        # continue
