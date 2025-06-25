from flask import Flask
from api_endpoints import api

app = Flask(__name__)

app.register_blueprint(api)
@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

if __name__ == "__main__":
    app.run(debug=True)




"""
curl -X POST -d "name=task 1" http://127.0.0.1:5000/create_task
curl -X POST -d "name=task 2" http://127.0.0.1:5000/create_task
curl -X POST -d "name=task 3" http://127.0.0.1:5000/create_task


curl -G curl -X GET  http://127.0.0.1:5000/get_task/0
curl -X PUT -d "name=this task has been updated" http://127.0.0.1:5000/update_task/0
curl -X "DELETE"  http://127.0.0.1:5000/get_task/0

"""