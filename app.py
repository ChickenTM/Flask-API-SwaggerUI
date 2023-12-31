from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/basic_api/hello_world')
def hello_world():
    return "Hello World!"

@app.route('/basic_api/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of enitites',
            'method': request.method,
            'body': request.json
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
            'body': request.json
        }  

@app.route('/basic_api/entities/<int:entity_id>', methods=['PUT', 'GET', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }

    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'This endpoint should update the entity {} details'.format(entity_id),
            'method': request.method
        }
    
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'This endpoint should delete the entity {} details'.format(entity_id),
            'method': request.method
        }
