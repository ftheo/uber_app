from flask import Flask
from flask import request
from threading import Thread
import random
import string
import socket
import os


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Uber Auto Server: ' + socket.gethostname()


@app.route('/dispatch', methods=['GET'])
def dispatch_request():
    task_time = int(request.args.get('time', ''))
    thr = Thread(target=dispatch, args=[app, task_time])
    thr.start()
    return 'Uber Auto Server: ' + socket.gethostname() + " with processing time: " + str(task_time), 200


def dispatch(app, task_time):
    import time
    id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    print "task " + id + " started"
    end_time = int(time.time()) + task_time
    while int(time.time()) < end_time:
        pass
    print "task " + id + " completed", 200


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=80)