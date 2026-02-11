import os

def maintain_system(command_type, target_file):
    # VIOLACIÓN CRÍTICA: Inyección de comandos de sistema operativo
    # Confianza implícita en la entrada del usuario (NSA 2.4.1)
    print(f"Ejecutando mantenimiento tipo {command_type} en {target_file}...")
    
    # Esto permite ejecutar: "delete ; rm -rf /" 
    os.system(f"echo {command_type} > log.txt && cat {target_file}")

if __name__ == "__main__":
    maintain_system("cleanup", "config.yaml")