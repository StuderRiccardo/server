from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
@app.route('/')
def get_students():
    con = sqlite3.connect("tutorial.db")
    c = con.cursor()
    c.execute("""
    select * from students
    """)
    students = c.fetchall()
    con.close()
    return students

@app.route('/visualizzastudenti', methods=['GET'])
def view_students():
    studenti = get_students()
    return jsonify({'studenti': studenti})

def get_entry_exit():
    con = sqlite3.connect("tutorial.db")
    c = con.cursor()
    c.execute("""
    select * from entry_exit
    """)
    esc = c.fetchall()
    con.close()
    return esc

@app.route('/visualizzaentrateuscite', methods=['GET'])
def view_entry_exit(): # Rinomina la funzione in view_entry_exit
    entry_exit = get_entry_exit()
    return jsonify({'entrateuscite': entry_exit})

if __name__ == "__main__":
    app.run()