from flask import Blueprint, jsonify, request, session
from backend.model.task import Task
from backend import db_session
api = Blueprint('api', __name__)

@api.route('/create_task', methods=['POST'])
def create_task():

    task = Task(name=request.form["name"])
    db_session.add(task)
    db_session.commit()

    return jsonify({"message": "sssss"})