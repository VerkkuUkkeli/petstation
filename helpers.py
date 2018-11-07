import glob

# return a dict of available audio files
# the filename base is used as the key and the file path is used as the value
def get_audio_files():
    filepaths = glob.glob('static/audio/*.wav')
    keys = [path[13:] for path in filepaths]
    return dict(zip(keys, filepaths))
