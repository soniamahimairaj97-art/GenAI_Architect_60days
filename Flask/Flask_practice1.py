from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

@app.route('/')
def index():
    # Show all tasks
    return "<h1>My To-Do List</h1>" + "<br>".join(tasks) + \
           "<br><br><a href='/add'>Add a new task</a>"

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('index'))
    # Simple HTML form
    return '''
        <form method="post">
            Task: <input type="text" name="task">
            <input type="submit" value="Add">
        </form>
    '''

@app.route('/clear')
def clear():
    tasks.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)