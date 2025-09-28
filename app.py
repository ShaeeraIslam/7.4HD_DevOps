from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
tasks = []

@app.route("/")
def home():
    return "Welcome to the Flask To-Do API!"

@app.route("/health")
def health():
    return jsonify({"status": "OK"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "title": data["title"]}
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(port=5000)