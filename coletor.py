import csv
import re
from datetime import datetime

LOG_FILE = "auth_simulado.log"
CSV_FILE = "logs_de_seguranca.csv"

def extrair_tentativas_login_invalidas():
    with open(LOG_FILE, "r") as file:
        linhas = file.readlines()

    eventos = []
    for linha in linhas:
        if "Failed password" in linha:
            data = " ".join(linha.split()[0:3])
            usuario = re.findall(r"for invalid user (\w+)", linha)
            ip = re.findall(r"from ([\d.]+)", linha)

            eventos.append([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Tentativa de Login Inválido",
                usuario[0] if usuario else "Desconhecido",
                ip[0] if ip else "Desconhecido"
            ])
    return eventos

def salvar_em_csv(eventos):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        for evento in eventos:
            writer.writerow(evento)

if __name__ == "__main__":
    eventos = extrair_tentativas_login_invalidas()
    if eventos:
        salvar_em_csv(eventos)
        print(f"{len(eventos)} eventos salvos em {CSV_FILE}")
    else:
        print("Nenhum evento de login inválido encontrado.")