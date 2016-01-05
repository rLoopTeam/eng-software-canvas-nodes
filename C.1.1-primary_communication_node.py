from __future__ import print_function # In python 2.7
import sys
import time
import math

from flask import Flask, jsonify, make_response, request
from IDs import MessageList as ml

app = Flask(__name__)

commands = [
    {
        'id': 1,
        'name': u'stop',
        'arguments': [],
        'return_values': [],
        'description': 'This command brings the pod to a stop.'
    },
    {
        'id': 2,
        'name': u'start',
        'arguments': [],
        'return_values': [],
        'description': 'This command initialises the various systems and gets the pod ready to move.'
    },
    {
        'id': 3,
        'name': u'move',
        'arguments': ['speed'],
        'return_values': [],
        'description': 'This command makes the pod move at a specified speed.'
    },
    {
        'id': 4,
        'name': u'get_status',
        'arguments': [],
        'return_values': ['power_level',
                          'battery_temperature',
                          'internal_temperature',
                          'external_temperature',
                          'internal_pressure',
                          'external_pressure'],
        'description': 'This command returns the status of the modules in the pod.'
    },
    {
        'id': 5,
        'name': u'get_position',
        'arguments': [],
        'return_values': ['x','y','z'],
        'description': 'This command returns the x,y and z coordinates of the pod.'
    },
    {
        'id': 6,
        'name': u'get_speed',
        'arguments': [],
        'return_values': ['speed'],
        'description': 'This command returns the speed of the pod'
    }
]

@app.route('/stop', methods=['GET'])
def stop():
    result = {'command': 'start'}
    print(result, file=sys.stderr)
    return jsonify(result)

@app.route('/start', methods=['GET'])
def start():
    result = {'command': 'start'}
    print(result, file=sys.stderr)
    return jsonify(result)

@app.route('/move', methods=['POST'])
def move():
    if not request.json:
        abort(400)
    result = {'command': 'move', 'argument':request.json()}
    print(result, file=sys.stderr)
    return jsonify(result), 201

@app.route('/get_status', methods=['GET'])
def get_status():
    result = {'command': 'get_status', 'return_values':request.json()}
    print(result, file=sys.stderr)
    return jsonify(result)

@app.route('/get_position', methods=['GET'])
def get_position():
    result = {'command': 'get_position', 'return_values':request.json()}
    print(result, file=sys.stderr)
    return jsonify(result)

@app.route('/get_speed', methods=['GET'])
def get_speed():
    result = {'command': 'get_speed', 'return_values':request.json()}
    print(result, file=sys.stderr)
    return jsonify(result)

@app.route('/commands', methods=['GET'])
def get_commands():
    result = {'commands':commands}
    print(result, file=sys.stderr)
    return jsonify(result)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def main():
	#sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	#canvas.print_out("Primary communication node started")

	while 1:
                print("heart beat")

		time.sleep(2)

if __name__ == '__main__':
    app.debug = True
    app.run()
