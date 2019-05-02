
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', checked1 = " ")


@app.route('/on/<room_on>')
def on(room_on):
    uri = 'http://192.168.1.116:8000/room_on/' + room_on
    r = requests.get(uri)
    a = r.json()
    print "On Request : ", a
    print " "	
    status=r.status_code
    return render_template('index.html')

@app.route('/off/<room_off>')
def off(room_off):
    uri = 'http://192.168.1.116:8000/room_off/' + room_off
    r = requests.get(uri)
    b = r.json()
    print "Off Request : ", b	
    print " "
    status=r.status_code
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    ## app.run()
