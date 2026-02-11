import sys
import re
from src.agent.audit_engine import MondayAgent
from src.agent.remediator import MondayRemediator
from src.utils.logger import log_event

def run_ztag_workflow(target_path):
    monday = MondayAgent()
    remediator = MondayRemediator()
    
    print(f"\n--- [ZTAG SYSTEM: MONDAY AGENT ON DUTY] ---")
    log_event("SYSTEM_START", f"Iniciando orquestación sobre: {target_path}")

    report = monday.audit_code(target_path)
    print(f"\n[INFORME DE MONDAY]:\n{report}\n")

    # Lógica de extracción flexible para DB y OS
    fix_code = ""
    # Buscamos patrones comunes de inicio de código corregido
    patterns = ["import sqlite3", "import subprocess", "import os", "def "]
    
    for pattern in patterns:
        if pattern in report:
            parts = report.split(pattern)
            # Tomamos la última ocurrencia por si Monday explicó el código antes de ponerlo
            fix_code = pattern + parts[-1]
            break

    if fix_code:
        # Limpieza de bloques de markdown
        fix_code = re.sub(r'```python|```', '', fix_code).strip()
        
        # Validación de seguridad preventiva: ¿Monday intentó colar otro os.system?
        if "os.system(" in fix_code:
            print("[ALERTA] Monday propone una solución que aún usa os.system. Riesgo persistente.")
        
        print("-" * 50)
        print(">>> Monday ha propuesto una mejora técnica de seguridad.")
        opcion = input(f"¿Deseas aplicar esta solución en el activo seguro? (s/n): ")
        
        if opcion.lower() == 's':
            success = remediator.apply_fix(target_path, fix_code)
            if success:
                print(f"[OK] ZTAG ha blindado el componente: {target_path}")
                log_event("REMEDIATION_APPLIED", f"Blindaje exitoso en {target_path}")
    else:
        print("[!] Monday no proporcionó un bloque de código ejecutable para la solución.")
        log_event("AUDIT_ONLY", "Informe generado sin código de remediación")

if __name__ == "__main__":
    # RETO: Cambiamos a la auditoría de Sistema Operativo
    run_ztag_workflow("src/connectors/insecure_os.py")