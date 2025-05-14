import json
import os

ARQUIVO_CONSULTAS = 'consultas.json'

def carregar_consultas():
    if not os.path.exists(ARQUIVO_CONSULTAS):
        return []
    with open(ARQUIVO_CONSULTAS, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def salvar_consultas(consultas):
    with open(ARQUIVO_CONSULTAS, 'w') as file:
        json.dump(consultas, file, indent=4)
