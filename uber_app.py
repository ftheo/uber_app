from flask import Flask
from flask import request
from threading import Thread
import random
import string


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Uber Auto Server'

@app.route('/dispatch', methods=['GET'])
def upload_file():
    task_time = int(request.args.get('time', ''))
    thr = Thread(target=dispatch, args=[app, task_time])
    thr.start()
    return str(task_time)

def dispatch(app, task_time):
    import time
    id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    print "task " + id + " started"
    end_time = int(time.time()) + task_time
    while int(time.time()) < end_time:
        pass
    print "task " + id + " completed"


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=80)