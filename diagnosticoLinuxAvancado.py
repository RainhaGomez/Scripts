# Script Menu interativo avançado para diagnóstico do sistema
# Objetivo: Executar verificações no Linux Debian 12 com opções extras

import shutil       # Manipulação de arquivos e verificação de espaço em disco
import subprocess   # Executar comandos do terminal
import psutil       # Biblioteca para informações do sistema (precisa instalar: pip install psutil)
import time         # Registrar data/hora no relatório
import os           # Para manipular caminhos de arquivos

# Função: verificar espaço em disco
def espaco_disco():
    total, usado, livre = shutil.disk_usage("/")
    print(f"Espaço livre: {livre // (2**30)} GB")

# Função: listar usuários logados
def usuarios_logados():
    subprocess.run(["who"])

# Função: exibir tempo de atividade
def tempo_atividade():
    subprocess.run(["uptime"])

# Função: exibir uso de memória RAM
def uso_memoria():
    memoria = psutil.virtual_memory()
    print(f"Memória usada: {memoria.percent}% ({memoria.used // (2**20)} MB de {memoria.total // (2**20)} MB)")

# Função: exibir temperatura da CPU (requer lm-sensors)
def temperatura_cpu():
    try:
        subprocess.run(["sensors"])
    except FileNotFoundError:
        print("'lm-sensors' não está instalado. Instale com: sudo apt install lm-sensors")

# Função: verificar status de um serviço
def status_servico():
    servico = input("Digite o nome do serviço: ")
    status = subprocess.run(["systemctl", "is-active", servico], capture_output=True, text=True)
    if status.stdout.strip() == "active":
        print(f"O serviço {servico} está ATIVO.")
    else:
        print(f"O serviço {servico} está INATIVO.")

# Função: salvar relatório de diagnóstico
def salvar_relatorio():
    nome_arquivo = f"relatorio_sistema_{time.strftime('%Y%m%d_%H%M%S')}.txt"
    caminho = os.path.join(os.getcwd(), nome_arquivo)

    with open(caminho, "w") as rel:
        rel.write(f"Relatório de Diagnóstico - {time.ctime()}\n")
        rel.write("="*50 + "\n")
        
        # Espaço em disco
        total, usado, livre = shutil.disk_usage("/")
        rel.write(f"Espaço livre: {livre // (2**30)} GB\n")
        
        # Memória RAM
        memoria = psutil.virtual_memory()
        rel.write(f"Memória usada: {memoria.percent}% ({memoria.used // (2**20)} MB de {memoria.total // (2**20)} MB)\n")
        
        # Tempo de atividade
        uptime = subprocess.run(["uptime"], capture_output=True, text=True)
        rel.write(f"Tempo de atividade: {uptime.stdout.strip()}\n")

        # Usuários logados
        who = subprocess.run(["who"], capture_output=True, text=True)
        rel.write(f"Usuários logados:\n{who.stdout.strip()}\n")

    print(f"Relatório salvo em: {caminho}")

# Loop principal do menu
while True:
    print("\n=== MENU DE DIAGNÓSTICO AVANÇADO ===")
    print("1 - Espaço em disco")
    print("2 - Usuários logados")
    print("3 - Tempo de atividade")
    print("4 - Uso de memória RAM")
    print("5 - Temperatura da CPU")
    print("6 - Status de um serviço")
    print("7 - Salvar relatório do sistema")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        espaco_disco()
    elif op == "2":
        usuarios_logados()
    elif op == "3":
        tempo_atividade()
    elif op == "4":
        uso_memoria()
    elif op == "5":
        temperatura_cpu()
    elif op == "6":
        status_servico()
    elif op == "7":
        salvar_relatorio()
    elif op == "0":
        break
    else:
        print("Opção inválida.")


#No Debian 12, instale antes:
#sudo apt update
#sudo apt install python3-pip lm-sensors
#pip install psutil

#Ative os sensores:
#sudo sensors-detect
