from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import json

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('./data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS progress
                 (week INTEGER PRIMARY KEY AUTOINCREMENT,
                 bench INTEGER,
                 b_reps INTEGER,
                 squat INTEGER,
                 s_reps INTEGER,
                 deadlift INTEGER,
                 d_reps INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('./data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM progress')
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    bench = request.form['bench']
    b_reps = request.form['b_reps']
    squat = request.form['squat']
    s_reps = request.form['s_reps']
    deadlift = request.form['deadlift']
    d_reps = request.form['d_reps']
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO progress (bench, b_reps, squat, s_reps, deadlift, d_reps) VALUES (?, ?, ?, ?, ?, ?)",
              (bench, b_reps, squat, s_reps, deadlift, d_reps))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/stats')
def stats():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM progress')
    data = c.fetchall()
    conn.close()
    
    weeks = [row[0] for row in data]
    bench = [row[1]*row[2] for row in data]
    squat = [row[3]*row[4] for row in data]
    deadlift = [row[5]*row[6] for row in data]
    total = [(row[1]*row[2]) + (row[3]*row[4]) + (row[5]*row[6]) for row in data]
    return json.dumps({
        'weeks': weeks,
        'bench': bench,
        'squat': squat,
        'deadlift': deadlift,
        'total': total
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
