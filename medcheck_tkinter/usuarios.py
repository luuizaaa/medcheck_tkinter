import json
import os

ARQUIVO_USUARIOS = 'usuarios.json'

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    with open(ARQUIVO_USUARIOS, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w') as file:
        json.dump(usuarios, file, indent=4)

def registrar_usuario(email, cpf, senha):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['email'] == email or usuario['cpf'] == cpf:
            return False
    usuarios.append({"email": email, "cpf": cpf, "senha": senha})
    salvar_usuarios(usuarios)
    return True

def autenticar_usuario(email_ou_cpf, senha):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if (usuario['email'] == email_ou_cpf or usuario['cpf'] == email_ou_cpf) and usuario['senha'] == senha:
            return usuario
    return None
