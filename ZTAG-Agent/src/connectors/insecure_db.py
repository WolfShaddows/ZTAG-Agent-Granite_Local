import sqlite3

# VIOLACIÓN: Path hardcodeado y credenciales expuestas
DB_PATH = "C:/Users/PC/Desktop/ZTAG-Agent/data/database.db"

def access_data(user_input):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # VIOLACIÓN CRÍTICA: Inyección SQL (Confianza implícita en user_input)
    query = f"SELECT * FROM users WHERE id = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchone()