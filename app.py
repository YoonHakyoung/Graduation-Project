from flask import Flask, request, jsonify, render_template
import json
from nearest import find_nearest_node
import a_star_al

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data = request.json.get('data')

        if data is None:
            return jsonify({'result': 'Invalid request'}), 400
        
        graph01 = a_star_al.Graph()
        start_node = find_nearest_node(data['startID'])
        end_node = find_nearest_node(data['endID'])
        result = graph01.a_star_algorithm(start_node,end_node)
        return jsonify({'result': result['lati,longi']}), 200
    elif request.method == 'GET':
        return jsonify({'message': 'This is a GET request'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

'''
from a_result import lati1, lati2, longi1, longi2
import a_result
app = Flask(__name__)

@app.route('/')
def result():
    return a_result.result
if __name__ == '__main__':
    app.run()
'''