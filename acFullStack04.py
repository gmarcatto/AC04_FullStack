from flask import Flask, request
import sqlite3

app = Flask(_name_)

def inserir_dados():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tabela (coluna1, coluna2) VALUES (?, ?)", ('Coluna1', 'Coluna2'))
    conn.commit()
    conn.close()

@app.route('/dados', methods=['GET'])
def get_dados():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabela")
    dados = cursor.fetchall()
    conn.close()
    return str(dados)

@app.route('/dados', methods=['POST'])
def post_dados():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    dados = request.json
    cursor.execute("INSERT INTO tabela (coluna1, coluna2) VALUES (?, ?)",
                   (dados['valor1'], dados['valor2']))
    conn.commit()
    conn.close()
    return 'Dados inseridos com sucesso!'

if _name_ == '_main_':
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabela (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coluna1 TEXT,
            coluna2 TEXT
        )
    ''')
    conn.close()

    inserir_dados()

    app.run()