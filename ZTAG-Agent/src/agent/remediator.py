import os
from src.utils.logger import log_event

class MondayRemediator:
    def __init__(self):
        self.name = "Monday-Remediator"

    def apply_fix(self, insecure_file, secure_code):
        """
        Genera la versión segura del conector aplicando estándares NSA.
        """
        try:
            # Aseguramos que el nombre cambie de insecure a secure
            secure_path = insecure_file.replace("insecure", "secure")
            
            # CORRECCIÓN: Escritura explícita en utf-8 para consistencia
            with open(secure_path, "w", encoding="utf-8") as f:
                f.write(secure_code)
            
            log_event("REMEDIATION", f"Archivo blindado generado exitosamente: {secure_path}")
            return True
        except Exception as e:
            log_event("ERROR", f"Fallo crítico en remediación: {str(e)}")
            return False