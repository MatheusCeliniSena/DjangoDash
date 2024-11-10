import subprocess
import webbrowser
import time
import os
import platform

def run_docker_script():
    # Verifica o sistema operacional para ajustar o comando
    script_path = "./start_docker.sh" if platform.system() != "Windows" else "start_docker.bat"

    # Executa o script .sh no Linux/macOS ou .bat no Windows
    try:
        subprocess.run(["sh", script_path], check=True)
        print("Docker iniciado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o Docker: {e}")

def open_browser():
    # Aguarde alguns segundos para garantir que o Docker esteja rodando
    time.sleep(5)
    # Abre o navegador padrão na URL especificada
    webbrowser.open("http://localhost:8000")

if __name__ == "__main__":
    run_docker_script()
    open_browser()
