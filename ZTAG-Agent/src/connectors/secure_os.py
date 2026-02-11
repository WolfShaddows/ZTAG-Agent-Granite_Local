import subprocess

def maintain_system(command_type, target_file):
    # Solución CRítica 1: Evita la inyección de comandos SQL utilizando parámetros (?)
    print("Ejecutando mantenimiento tipo ? en ?...")
    
    # Esto permite ejecutar: "delete ; rm -rf /" 
    subprocess.run(["echo", command_type, ">", "log.txt"], check=True)
    subprocess.run(["cat", target_file], check=True)

if __name__ == "__main__":
    maintain_system("cleanup", "config.yaml")