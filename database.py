import sqlite3


def create_table():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT, date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()


def add_password(username, email, password):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()


def get_passwords():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    data = c.fetchall()
    conn.close()
    return data
