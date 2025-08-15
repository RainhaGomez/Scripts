# Script Verificar se um serviço Linux está ativo
# Objetivo: verificar o status de um serviço no sistema Linux

import os
servico = input("Informe o nome do serviço: ")
status = os.system(f"systemctl is-active --quiet {servico}")
if status == 0:
    print(f"O serviço {servico} está ATIVO.")
else:
    print(f"O serviço {servico} está INATIVO.")
