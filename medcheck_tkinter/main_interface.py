import tkinter as tk
from tkinter import messagebox
from usuarios import registrar_usuario, autenticar_usuario
from consultas import marcar_consulta, listar_consultas, cancelar_consulta
from datetime import datetime

usuario_logado = None

def abrir_menu_usuario():
    janela = tk.Tk()
    janela.title("MedCheck - Menu")

    def marcar():
        janela_marcar = tk.Toplevel()
        janela_marcar.title("Marcar Consulta")

        tk.Label(janela_marcar, text="Data (dd/mm/aaaa):").grid(row=0, column=0)
        entrada_data = tk.Entry(janela_marcar)
        entrada_data.grid(row=0, column=1)

        tk.Label(janela_marcar, text="Horário (hh:mm):").grid(row=0, column=0)
        entrada_horario = tk.Entry(janela_marcar)
        entrada_horario.grid(row=1, column=1)

        def confirmar_marcacao():
            try:
                data = datetime.strptime(entrada_data.get(), '%d/%m/%Y').date()
                horario = entrada_horario.get()
                resultado = marcar_consulta(usuario_logado, data, horario)
                if resultado:
                    messagebox.showinfo("Sucesso", f"Consulta marcada para {entrada_data.get()} às {horario}.")
                    janela_marcar.destroy()
                else:
                    messagebox.showerror("Erro", "Já existe uma consulta nesse dia e horário.")
            except ValueError:
                messagebox.showerror("Erro", "Data ou horário inválido.")

        tk.Button(janela_marcar, text="Marcar", command=confirmar_marcacao).grid(row=2, columnspan=2)

    def ver():
        janela_ver = tk.Toplevel()
        janela_ver.title("Consultas Agendadas")
        consultas = listar_consultas(usuario_logado)
        if consultas:
            for i, c in enumerate(consultas):
                tk.Label(janela_ver, text=f"{i+1}. {c['data']} às {c['horario']}").pack()
        else:
            tk.Label(janela_ver, text="Nenhuma consulta agendada.").pack()

    def cancelar():
        janela_cancelar = tk.Toplevel()
        janela_cancelar.title("Cancelar Consulta")
        consultas = listar_consultas(usuario_logado)
        if not consultas:
            tk.Label(janela_cancelar, text="Nenhuma consulta para cancelar.").pack()
            return

        for i, c in enumerate(consultas):
            tk.Label(janela_cancelar, text=f"{i+1}. {c['data']} às {c['horario']}").pack()

        tk.Label(janela_cancelar, text="Número da consulta:").pack()
        entrada = tk.Entry(janela_cancelar)
        entrada.pack()

        def confirmar_cancelamento():
            try:
                indice = int(entrada.get()) - 1
                if cancelar_consulta(usuario_logado, indice):
                    messagebox.showinfo("Cancelado", "Consulta cancelada com sucesso.")
                    janela_cancelar.destroy()
                else:
                    messagebox.showerror("Erro", "Não foi possível cancelar.")
            except:
                messagebox.showerror("Erro", "Entrada inválida.")

        tk.Button(janela_cancelar, text="Cancelar", command=confirmar_cancelamento).pack()

    tk.Button(janela, text="Marcar Consulta", width=25, command=marcar).pack(pady=5)
    tk.Button(janela, text="Ver Consultas", width=25, command=ver).pack(pady=5)
    tk.Button(janela, text="Cancelar Consulta", width=25, command=cancelar).pack(pady=5)
    tk.Button(janela, text="Sair", width=25, command=janela.destroy).pack(pady=5)
    janela.mainloop()

def abrir_janela_principal():
    janela_login = tk.Tk()
    janela_login.title("MedCheck - Login")

    tk.Label(janela_login, text="E-mail ou CPF").grid(row=0, column=0)
    entrada_usuario = tk.Entry(janela_login)
    entrada_usuario.grid(row=0, column=1)

    tk.Label(janela_login, text="Senha").grid(row=1, column=0)
    entrada_senha = tk.Entry(janela_login, show="*")
    entrada_senha.grid(row=1, column=1)

    def fazer_login():
        global usuario_logado
        email_cpf = entrada_usuario.get()
        senha = entrada_senha.get()
        usuario = autenticar_usuario(email_cpf, senha)
        if usuario:
            usuario_logado = usuario
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            janela_login.destroy()
            abrir_menu_usuario()
        else:
            messagebox.showerror("Erro", "Email/CPF ou senha inválidos.")

    def abrir_cadastro():
        janela_cadastro = tk.Toplevel()
        janela_cadastro.title("Cadastro")

        tk.Label(janela_cadastro, text="E-mail").grid(row=0, column=0)
        email = tk.Entry(janela_cadastro)
        email.grid(row=0, column=1)

        tk.Label(janela_cadastro, text="CPF").grid(row=1, column=0)
        cpf = tk.Entry(janela_cadastro)
        cpf.grid(row=1, column=1)

        tk.Label(janela_cadastro, text="Senha").grid(row=2, column=0)
        senha = tk.Entry(janela_cadastro, show="*")
        senha.grid(row=2, column=1)

        consentimento_var = tk.IntVar()
        tk.Checkbutton(
            janela_cadastro,
            text="Li e concordo com o uso dos meus dados conforme a LGPD",
            variable=consentimento_var
        ).grid(row=3, columnspan=2)

        def registrar():
            if not consentimento_var.get():
                messagebox.showerror("Erro", "Você deve aceitar os termos de consentimento.")
                return
            
            if registrar_usuario(email.get(), cpf.get(), senha.get()):
                messagebox.showinfo("Cadastro", "Usuário registrado com sucesso.")
                janela_cadastro.destroy()
            else:
                messagebox.showerror("Erro", "Usuário já existe.")

        tk.Button(janela_cadastro, text="Registrar", command=registrar).grid(row=3, columnspan=2)

    tk.Button(janela_login, text="Entrar", command=fazer_login).grid(row=2, columnspan=2)
    tk.Button(janela_login, text="Cadastrar", command=abrir_cadastro).grid(row=3, columnspan=2)
    janela_login.mainloop()

if __name__ == "__main__":
    abrir_janela_principal()
