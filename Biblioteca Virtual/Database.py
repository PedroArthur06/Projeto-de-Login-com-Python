import mysql.connector
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Conectando com o banco de dados
def conect_banco():
    conn = mysql.connector.connect(
        host="Nome do Host",  
        user="Usuario",  
        password="Senha", 
        database="biblioteca"
    )
    return conn

# Cadastro de usuário
def cadastro(nome, email, senha, cpf, nome_usuario):
    conn = conect_banco()
    cursor = conn.cursor()
    if verificar_email_existente(email):
        st.error("Erro: Este e-mail já está cadastrado.")
        return 
    
    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha, cpf, nome_usuario) VALUES (%s, %s, %s, %s, %s)",
            (nome, email, senha, cpf, nome_usuario)
        )
        conn.commit()
        st.success("Cadastro realizado com sucesso!") 

    except mysql.connector.Error as e:
        st.error(f"Erro durante o cadastro: {e}")

    finally:
        conn.close()

# Autenticar os dados
def autenticar(email, senha):
    conn = conect_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

# Verifica se o email não estã cadastrado no banco de dados
def verificar_email_existente(email):
    conn = conect_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def enviar_email_confirmacao(email, nome_usuario):
    try:
        # Configuração do servidor SMTP
        servidor = "smtp.gmail.com"
        porta = 587
        email_remetente = "pedroxxl917@gmail.com"
        senha_remetente = "ltdx vtzd goub qhlz"

        # Criar a mensagem
        mensagem = MIMEMultipart()
        mensagem["From"] = email_remetente
        mensagem["To"] = email
        mensagem["Subject"] = "Confirmação de Cadastro"

        # Corpo do e-mail
        corpo_email = f"""
        Olá, {nome_usuario}!
        
        Seu cadastro foi realizado com sucesso.
        
        Seja bem-vindo(a) à nossa plataforma!
        """
        mensagem.attach(MIMEText(corpo_email, "plain"))

        # Conectar ao servidor e enviar o e-mail
        with smtplib.SMTP(servidor, porta) as smtp:
            smtp.starttls()  # Ativar criptografia TLS
            smtp.login(email_remetente, senha_remetente)
            smtp.sendmail(email_remetente, email, mensagem.as_string())

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
