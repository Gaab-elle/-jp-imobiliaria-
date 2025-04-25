from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Permite comunicação com o front-end

# Configuração do banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Cria o banco de dados se não existir
def init_db():
    if not os.path.exists('database.db'):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE moradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                residencial TEXT NOT NULL,
                apartamento TEXT NOT NULL,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

# Rota para adicionar/listar moradores
@app.route('/api/moradores', methods=['GET', 'POST'])
def moradores():
    conn = get_db_connection()
    
    if request.method == 'POST':
        data = request.get_json()
        print("Dados recebidos:", data)  # Para depuração
        
        conn.execute(
            'INSERT INTO moradores (residencial, apartamento, nome, telefone) VALUES (?, ?, ?, ?)',
            (data['residencial'], data['apartamento'], data['nome'], data['telefone'])
        )
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 201
    
    # Se for GET
    moradores = conn.execute('SELECT * FROM moradores').fetchall()
    conn.close()
    return jsonify([dict(row) for row in moradores])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)