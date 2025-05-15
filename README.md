# 💊 MedCheck | Sistema de Agendamento de Consultas com Tkinter

Projeto desenvolvido como parte do curso de Análise e Desenvolvimento de Sistemas. O MedCheck é um sistema de agendamento médico com interface gráfica utilizando Python (Tkinter), armazenamento em JSON, criptografia de senhas e boas práticas de proteção de dados conforme a LGPD.

---

## 🧠 Objetivo

Permitir que o usuário:
- Cadastre seus dados com segurança;
- Marque consultas médicas;
- Visualize e cancele agendamentos;
- Tudo isso com uma interface gráfica simples e eficiente.

---

## 🔧 Tecnologias utilizadas

- Python 3
- Tkinter (interface gráfica)
- JSON (armazenamento de dados)
- SHA-256 (criptografia de senha)

---

## 🗂 Estrutura do Projeto

```bash
medcheck_tkinter_seguro/
├── main_interface.py        # Interface gráfica principal
├── usuarios.py              # Registro e autenticação de usuários
├── consultas.py             # Controle de agendamentos
├── persistencia.py          # Leitura e escrita dos dados JSON
├── usuarios.json            # Armazena dados dos usuários
├── consultas.json           # Armazena agendamentos
└── README.txt               # Documentação do sistema
