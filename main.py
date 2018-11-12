from flask import Flask, render_template, request
from helpers import get_audio_files
import RPi.GPIO as io
import pygame
import time
from io_control import IOController

# global variables
app = Flask(__name__)
ioCtrl = IOController()

# render index page template
@app.route('/')
def index():
    # return page html as a response
    return render_template('index.html', audio_files=list(get_audio_files().keys()))

# render laser control page template
@app.route('/laser_control')
def laser_control():
    return render_template('laser_control.html')


# handlers for GET requests made using XMLHttpRequest from the client
# each function is responsible for handling the state for the corresponding key

# key events
@app.route('/w<int:state>')
def w_state(state):
    global ioCtrl
    print("W state:", state)
    ioCtrl.set_laser_controls(None, state)
    return "w"+str(state)

@app.route('/a<int:state>')
def a_state(state):
    global ioCtrl
    print("A state:", state)
    ioCtrl.set_laser_controls(state, None)
    return "a"+str(state)

@app.route('/s<int:state>')
def s_state(state):
    global ioCtrl
    print("S state:", state)
    ioCtrl.set_laser_controls(None, -state)
    return "s"+str(state)

@app.route('/d<int:state>')
def d_state(state):
    global ioCtrl
    print("D state:", state)
    ioCtrl.set_laser_controls(-state, None)
    return "d"+str(state)

@app.route('/laser<int:state>')
def laser_state(state):
    print("Laser state:", state)
    laser_on = False
    if state == 1:
        laser_on = True
       
    ioCtrl.set_laser_state(laser_on)
    return "laser"+str(state)

# handler for XMLHttpRequests for playing audio files
@app.route('/play_audio/<filename>')
def play_audio(filename):
    filepath = get_audio_files()[filename]
    print("Playing audio from file", filepath)
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    return ""

if __name__ == '__main__':
    ioCtrl.start()
    app.run(host='0.0.0.0')
