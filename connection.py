from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) #consente di richiedere delle risorse da una pagina web ad un altro dominio
@app.route('/') #serve all'utente per ricordare l'URL
def get_students():# funzione per mostrare la tabella studenti
    con = sqlite3.connect("tutorial.db") #connessione alla tabella
    c = con.cursor()
    c.execute("""
    select * from students
    """) #esegue una query
    students = c.fetchall()
    con.close() #chiude la connessione
    return jsonify({'studenti': students})# restituisce la tabella studenti in un json



@app.route('/students')
def get_entry_exit():
    con = sqlite3.connect("tutorial.db")
    c = con.cursor()
    c.execute("""
    select * from entry_exit
    """)
    esc = c.fetchall()
    con.close()
    return jsonify({'movimento': esc})
def showClass():
    con = sqlite3.connect('tutorial.db')
    c = con.cursor()
    c.execute("""
        select 

    """
    )

if __name__ == "__main__":
    app.run()