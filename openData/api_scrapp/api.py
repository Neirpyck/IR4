import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Access Click and Collect Angers</h1>
<p>A prototype API to access Click And Collect restaurants in Angers.</p>'''

@app.route('/restaurants/all', methods=['GET'])
def api_all():
    with open('data.json','r') as f:
        data = json.load(f)
    return jsonify(data).status_code(200)


@app.route('/restaurants', methods=['GET'])
def api_name():
    with open('data.json','r') as f:
        data = json.load(f)
    if 'restaurant' in request.args:
        restaurant = request.args['restaurant']
    else:
        return 'Error: No restaurant field provided. Please specify an restaurant.'

    results = []

    if restaurant in data.keys():
        results.append(data[restaurant])
    
    return jsonify(results).status_code(200)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    app.run(debug=True)
    