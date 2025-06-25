from flask import Blueprint, jsonify, request
from backend.model.task import Task
from backend.db_session import SessionLocal
api = Blueprint('api', __name__)

@api.route('/create_task', methods=['POST'])
def create_task():
    session = SessionLocal()
    task = Task(name=request.form["name"])
    session.add(task)
    session.commit()

    return jsonify({"message": "sssss"})

@api.route('/read_task/<int:id>', methods=['GET'])
def get_task_by_id(id):
    session = SessionLocal()
    task = session.query(Task).filter_by(id=id).first()
    if task is None:
        return jsonify({"message": "task not found"})
    return jsonify(f"{task}")

@api.route('/update_task/<int:id>', methods=['PATCH'])
def update_task_by_id(id, name):
    session = SessionLocal()
    task = session.query(Task).filter_by(id=id).first()
    if task is None:
        return jsonify({"message": "task not found"})
    task.name = name
    session.commit()
    return jsonify({"message": "task updated"})

@api.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    session = SessionLocal()
    task = session.query(Task).filter_by(id=id).first()
    session.delete(task)
    session.commit()
    return jsonify({"message": "success"})
