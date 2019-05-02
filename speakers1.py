
from flask import Flask, render_template
import requests
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('Init')


app = Flask(__name__)

@app.route('/')
def status():
    logging.warning('Main Page')
    uri = 'http://192.168.1.116:8000/room_status/'
    r = requests.get(uri)
    b = r.json()
    status=r.status_code  
    return render_template('index1.html', test = b )

@app.route('/on/<room_on>')
def on(room_on):
    uri = 'http://192.168.1.116:8000/room_on/' + room_on
    r = requests.get(uri)
    b = r.json()
    status=r.status_code
    return render_template('index1.html', test = b )

@app.route('/off/<room_off>')
def off(room_off):
    uri = 'http://192.168.1.116:8000/room_off/' + room_off
    r = requests.get(uri)
    b = r.json()
    status=r.status_code
    return render_template('index1.html', test = b)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    ## app.run()
