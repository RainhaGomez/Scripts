# Script: listar_servicos_linux.py
# Objetivo: listar todos os serviços instalados no Debian 12
# Funciona em sistemas com systemd (como Debian, Ubuntu, etc.)

import subprocess  # Permite executar comandos do sistema e capturar a saída

# Comando para listar todos os serviços instalados (ativos e inativos)
# systemctl list-unit-files mostra todos os serviços disponíveis e seus estados
comando = ["systemctl", "list-unit-files", "--type=service"]

# Executa o comando e captura a saída
# stdout=subprocess.PIPE → captura a saída padrão
# stderr=subprocess.PIPE → captura mensagens de erro
resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Verifica se o comando executou com sucesso
if resultado.returncode == 0:
    print("Lista de serviços instalados no Debian 12:\n")
    print(resultado.stdout)  # Mostra a saída do comando systemctl
else:
    print("Erro ao listar serviços:")
    print(resultado.stderr)  # Mostra mensagens de erro caso ocorra
