from flask import Flask, jsonify, request

app = Flask(__name__)

# A sample list of tasks
tasks = [
    {
        'id': 1,
        'title': 'Do laundry',
        'description': 'Wash clothes and hang them to dry',
        'done': False
    },
    {
        'id': 2,
        'title': 'Buy groceries',
        'description': 'Get eggs, milk, bread, and fruits',
        'done': False
    }
]

# GET request for tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# GET request for a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify({'task': task[0]})

# POST request to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# PUT request to update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'}), 404
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# DELETE request to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'}), 404
    tasks.remove(task[0])
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
