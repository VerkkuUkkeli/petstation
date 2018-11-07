from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from helpers import get_audio_files, play_audio

app = Flask(__name__)
Bootstrap(app)

# render index page template
@app.route('/')
def index():
    # if query string parameter for audio received, play corresponding audio
    audio_file = request.args.get('audio')
    if audio_file is not None:
        audio_paths = get_audio_files()
        play_audio(audio_paths[audio_file])

    # return page html as a response
    return render_template('index.html', audio_files=list(get_audio_files().keys()))

# render laser control page template
@app.route('/laser_control')
def laser_control():
    return render_template('laser_control.html')


# key events
# handlers for GET requests made using XMLHttpRequest from the client
# each function is responsible for handling the state for the corresponding key
@app.route('/w<int:state>')
def w_state(state):
    print("W state:", state)
    # TODO: move laser up if state is 1, stop movement if 0
    return "w"+str(state)

@app.route('/a<int:state>')
def a_state(state):
    print("A state:", state)
    # TODO: move laser left if state is 1, stop movement if 0
    return "a"+str(state)

@app.route('/s<int:state>')
def s_state(state):
    print("S state:", state)
    # TODO: move laser down if state is 1, stop movement if 0
    return "s"+str(state)

@app.route('/d<int:state>')
def d_state(state):
    print("D state:", state)
    # TODO: move laser right if state is 1, stop movement if 0
    return "d"+str(state)

@app.route('/laser<int:state>')
def laser_state(state):
    print("Laser state:", state)
    # TODO: Turn laser pin on if state is 1, turn laser of if 0
    return "laser"+str(state)
