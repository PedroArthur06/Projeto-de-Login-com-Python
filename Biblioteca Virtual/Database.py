import mysql.connector
import streamlit as st

# Função para criar a conexão com o banco de dados
def conect_banco():
    conn = mysql.connector.connect(
        host="Nome do Host",  
        user="Usuario",  
        password="Senha", 
        database="biblioteca"
    )
    return conn

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

# Função para autenticar um usuário
def autenticar(email, senha):
    conn = conect_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def verificar_email_existente(email):
    conn = conect_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario
