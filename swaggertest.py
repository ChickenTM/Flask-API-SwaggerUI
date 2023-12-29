from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields
from werkzeug.utils import cached_property

import werkzeug
from werkzeug.utils import cached_property
from flask.scaffold import _endpoint_from_view_func
import flask

flask.helpers._endpoint_from_view_func = _endpoint_from_view_func
werkzeug.cached_property = cached_property
# from flask import Flask
# from flask_restplus import Api

app = Flask(__name__)
api = Api(app)

# A sample list of tasks
tasks = [
    {
        "id": 1,
        "title": "Do laundry",
        "description": "Wash clothes and hang them to dry",
        "done": False,
    },
    {
        "id": 2,
        "title": "Buy groceries",
        "description": "Get eggs, milk, bread, and fruits",
        "done": False,
    },
]

# Define the task model
task_model = api.model(
    "Task",
    {
        "id": fields.Integer(readOnly=True),
        "title": fields.String(required=True),
        "description": fields.String(required=True),
        "done": fields.Boolean,
    },
)


# GET request for tasks
@api.route("/tasks")
class TaskList(Resource):
    @api.doc("list_tasks")
    @api.marshal_list_with(task_model)
    def get(self):
        """List all tasks"""
        return tasks


# GET request for a specific task
@api.route("/tasks/<int:task_id>")
class Task(Resource):
    @api.doc("get_task")
    @api.marshal_with(task_model)
    def get(self, task_id):
        """Fetch a task given its identifier"""
        task = [task for task in tasks if task["id"] == task_id]
        if len(task) == 0:
            api.abort(404, "Task not found")
        return task[0]


# POST request to add a new task
@api.route("/tasks")
class TaskCreate(Resource):
    @api.doc("create_task")
    @api.expect(task_model)
    @api.marshal_with(task_model, code=201)
    def post(self):
        """Create a new task"""
        task = {
            "id": tasks[-1]["id"] + 1,
            "title": request.json["title"],
            "description": request.json["description"],
            "done": False,
        }
        tasks.append(task)
        return task, 201


# PUT request to update a task
@api.route("/tasks/<int:task_id>")
class TaskUpdate(Resource):
    @api.doc("update_task")
    @api.expect(task_model)
    @api.marshal_with(task_model)
    def put(self, task_id):
        """Update a task given its identifier"""
        task = [task for task in tasks if task["id"] == task_id]
        if len(task) == 0:
            api.abort(404)
