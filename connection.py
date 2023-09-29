from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
@app.route('/')
def get_students():
    con = sqlite3.connect("tutorial.db")
    c = con.cursor()
    c.execute("""
    select * from students
    """)
    students = c.fetchall()
    con.close()
    return jsonify({'studenti': students})



def get_entry_exit():
    con = sqlite3.connect("tutorial.db")
    c = con.cursor()
    c.execute("""
    select * from entry_exit
    """)
    esc = c.fetchall()
    con.close()
    return esc
def change():
    con = sqlite3.connect('tutorial.db')
    c = con.cursor()
    c.execute("""


    """
    )

if __name__ == "__main__":
    app.run()