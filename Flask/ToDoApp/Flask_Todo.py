from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (Resets when server restarts)
todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build a Todo App", "done": True}
]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    if task_text:
        # Generate a simple ID based on list length
        new_id = len(todos) + 1
        todos.append({"id": new_id, "task": task_text, "done": False})
    return redirect(url_for('index'))

@app.route('/check/<int:todo_id>')
def check(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done'] # Toggle completion
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    global todos
    # Filter out the task with the matching ID
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)