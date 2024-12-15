from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'todo.db'

def get_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with the tasks table."""
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
        ''')
        conn.commit()

@app.route('/')
def index():
    """Display all tasks."""
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    """Add a new task."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        conn = get_db()
        conn.execute('INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)', (title, description, 0))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    """Edit an existing task."""
    conn = get_db()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        completed = 1 if 'completed' in request.form else 0
        conn.execute('UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?', (title, description, completed, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    """Delete a task."""
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    """Search tasks by title."""
    query = request.args.get('query', '')
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks WHERE title LIKE ?', (f'%{query}%',)).fetchall()
    conn.close()
    return render_template('search.html', tasks=tasks, query=query)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
