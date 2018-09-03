import os
from flask import Flask, render_template
CLICLICK = '/Users/rkmbp/Downloads/cliclick'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fullscr')
def fullscreen():
    os.system(CLICLICK+' m:1270,750')
    os.system(CLICLICK+' c:.')
    return 'FULLSCREEN   clicked.'

@app.route('/normalscr')
def normalscreen():
    #os.system(CLICLICK+' m:1270,810')
    os.system(CLICLICK+' kp:esc')
    return 'normalscreen clicked.'

@app.route('/pause')
def pause():
    os.system(CLICLICK+' kp:space')
    return ' ||   pause clicked   || '

@app.route('/volup')
def volume_up():
    os.system(CLICLICK+' kp:arrow-up')
    return '++++++++ volume up ++++++++'

@app.route('/voldown')
def volume_down():
    os.system(CLICLICK+' kp:arrow-down')
    return '------- volume down -------'

@app.route('/mute')
def mute():
    os.system(CLICLICK+' kp:f10')
    return 'xxxxxxxxx  mute  xxxxxxxxx'

@app.route('/ff')
def ff():
    os.system(CLICLICK+' kp:arrow-right')
    return '>>>> ff by 10 secs >>>>'

@app.route('/rw')
def rw():
    os.system(CLICLICK+' kp:arrow-left')
    return '<<<< rw by 10 secs <<<<'
