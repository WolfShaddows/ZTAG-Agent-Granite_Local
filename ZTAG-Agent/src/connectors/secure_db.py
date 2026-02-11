import sqlite3

def access_data(user_input):
    conn = sqlite3.connect("database.db") # Usa un path relativo para conectarse a la base de datos
    cursor = conn.cursor()
    # USANDO PARÁMETROS: Protege contra la inyección SQL (Confianza implícita en user_input)
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_input,))
    return cursor.fetchone()