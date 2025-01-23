from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS todo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """
    Displays the main page with all todo tasks
    Returns: Rendered index.html template with list of all tasks
    """
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todo")
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """
    Handles POST requests to add new tasks
    Gets task from form data and inserts it into database
    Returns: Redirects to main page after adding task
    """
    task = request.form.get('task')
    if task:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM todo WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    if request.method == 'POST':
        new_task = request.form.get('task')
        c.execute("UPDATE todo SET task = ? WHERE id = ?", (new_task, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        c.execute("SELECT * FROM todo WHERE id = ?", (task_id,))
        task = c.fetchone()
        conn.close()
        return render_template('edit.html', task=task)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)