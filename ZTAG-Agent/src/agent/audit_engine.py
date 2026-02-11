import requests

class MondayAgent:
    def audit_code(self, target_file):
        try:
            with open(target_file, "r", encoding="utf-8") as f:
                code = f.read()
        except Exception as e:
            return f"Error al leer archivo: {str(e)}"

        # PROMPT REFORZADO: Separación de dominios SQL vs OS
        prompt = (
            f"Instrucción: Eres 'Monday', experto en Zero Trust (NSA). Analiza y corrige este código.\n\n"
            f"REGLAS CRÍTICAS DE SEGURIDAD:\n"
            f"1. DOMINIO SQL: Si detectas consultas a bases de datos, PROHIBIDO usar f-strings. Usa parámetros (?).\n"
            f"2. DOMINIO OS: Si detectas 'os.system' o 'os.popen', PROHIBIDO usar parámetros (?).\n"
            f"   SOLUCIÓN OS: REEMPLAZA por 'subprocess.run' usando una LISTA de argumentos y elimina el shell.\n\n"
            f"Estructura obligatoria:\n"
            f"### ANALISIS\n(Breve riesgo técnico según NSA Phase One)\n\n"
            f"### SOLUCION\n(Código Python completo, corregido y funcional)\n\n"
            f"Código a auditar:\n{code}"
        )

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "granite-code:8b", 
                    "prompt": prompt, 
                    "stream": False,
                    "options": {
                        "temperature": 0,       # Precisión total
                        "num_predict": 1024,
                        "num_ctx": 4096 
                    }
                },
                timeout=300 
            )
            return response.json().get("response", "Error: Granite no devolvió datos.")
        except requests.exceptions.Timeout:
            return "Error: Timeout. Monday está procesando una lógica compleja."
        except Exception as e:
            return f"Error conectando con Granite: {str(e)}"