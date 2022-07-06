import sqlite3
from django.urls import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    con = con.cursor()
    con.execute('select * from posts')
    posts = cur.fetchall()
    return posts