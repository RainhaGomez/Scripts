# Script - Menu interativo para diagnóstico do sistema
# Objetivo: executar comandos de verificação no Linux
import platform
import shutil
import subprocess

def espaco_disco():
    total, usado, livre = shutil.disk_usage("/")
    print(f"Espaço livre: {livre // (2**30)} GB")

def usuarios_logados():
    subprocess.run(["who"])

def tempo_atividade():
    subprocess.run(["uptime"])

while True:
    print("\nMENU DE DIAGNÓSTICO")
    print("1 - Espaço em disco")
    print("2 - Usuários logados")
    print("3 - Tempo de atividade")
    print("0 - Sair")
    op = input("Escolha: ")
    if op == "1":
        espaco_disco()
    elif op == "2":
        usuarios_logados()
    elif op == "3":
        tempo_atividade()
    elif op == "0":
        break
    else:
        print("Opção inválida.")
