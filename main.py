from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# render index page template
@app.route('/')
def index():
    return render_template('index.html')

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
