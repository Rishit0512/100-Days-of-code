from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'cafes.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    cafes = conn.execute('SELECT * FROM cafes').fetchall()
    conn.close()
    return render_template('index.html', cafes=cafes)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    conn = get_db()
    cafes = conn.execute('SELECT * FROM cafes WHERE name LIKE ?', (f'%{query}%',)).fetchall()
    conn.close()
    return render_template('search.html', cafes=cafes, query=query)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        name = request.form['name']
        wifi = request.form['wifi']
        coffee = request.form['coffee']
        conn = get_db()
        conn.execute('INSERT INTO cafes (name, wifi, coffee) VALUES (?, ?, ?)', (name, wifi, coffee))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_cafe.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_cafe(id):
    conn = get_db()
    if request.method == 'POST':
        name = request.form['name']
        wifi = request.form['wifi']
        coffee = request.form['coffee']
        conn.execute('UPDATE cafes SET name = ?, wifi = ?, coffee = ? WHERE id = ?', (name, wifi, coffee, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    cafe = conn.execute('SELECT * FROM cafes WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit_cafe.html', cafe=cafe)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_cafe(id):
    conn = get_db()
    conn.execute('DELETE FROM cafes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
