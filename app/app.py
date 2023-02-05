from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
import pymysql


def get_db_connection():
    conn = pymysql.connect(
        host= 'to-do-list-app-db.ci0bwdslg8qr.us-east-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'fghrty9182',
        db = 'tasks_db',
        )
    return conn

def get_post(post_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks WHERE id = %d' % (post_id))
    post = cur.fetchone()
    conn.close()
    cur.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks')
    posts = cur.fetchall()
    print(posts)
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        new_title = request.form['title']
        new_content = request.form['content']

        if not new_title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO tasks (title, content) VALUES (%s, %s)" ,(new_title, new_content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        new_title = request.form['title']
        new_content = request.form['content']
        if not new_title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('UPDATE tasks SET title = %s , content = %s WHERE id = %s' ,(new_title, new_content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %d' % (id))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post[2]))
    return redirect(url_for('index'))

if __name__ == '__name__':
    app2.run(debug=True, port=8001)
