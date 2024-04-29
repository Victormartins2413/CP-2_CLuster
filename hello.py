from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Conecte-se ao banco de dados SQLite
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    # Execute uma consulta
    cursor.execute("SELECT * FROM mytable")
    result = cursor.fetchall()

    # Encerre a conexão
    cursor.close()
    connection.close()

    return str(result)

if __name__ == '__main__':
    # Crie o banco de dados SQLite e a tabela se ainda não existirem
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER)''')
    connection.commit()
    cursor.close()
    connection.close()

    # Inicie o aplicativo Flask
    app.run(host='0.0.0.0')
