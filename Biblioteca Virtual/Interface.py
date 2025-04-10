import streamlit as st
from streamlit_option_menu import option_menu
from Database import cadastro, autenticar, verificar_email_existente, enviar_email_confirmacao
from validador import validaCPF, validaEmail, validaSenha
# Para executar rode: python -m streamlit run Interface.py

# Título e ícone da página
st.set_page_config(page_title="Cadastro de usuários", page_icon="👤", layout="wide")

if "tela_atual" not in st.session_state:
    st.session_state.tela_atual = "Inicio"

# Alterar a tela atual e atualizar a interface
def mudar_tela(tela):
    st.session_state.tela_atual = tela

# Menu de navegação
with st.sidebar:
    menu = option_menu(
        "Menu",
        ["Início", "Filmes", "Diretores", "Sobre"], 
        icons=["house", "film", "star", "info-circle"],
        menu_icon="list", 
        default_index=0 
    )

# Configuração da navegação
if menu == "Início":
    st.title("Bem-vindo!")
    st.subheader("Escolha uma opção para continuar:")

    # Tela inicial
    if st.session_state.tela_atual == "Inicio":
        if st.button("Login"):
            mudar_tela("Login")  
        if st.button("Cadastro"):
            mudar_tela("Cadastro") 


    # Tela de Login
    elif st.session_state.tela_atual == "Login":
        st.title("Login")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            usuario = autenticar(email, senha)
            if usuario:
                st.success(f"Bem-vindo(a), {usuario[1]}!")
            else:
                st.error("E-mail ou senha incorretos.")
        if st.button("Voltar"):
            mudar_tela("Inicio") 

    # Tela de Cadastro
    elif st.session_state.tela_atual == "Cadastro":
      st.title("Cadastro")
    
      # Usuario preenche os dados
      nome = st.text_input("Nome completo", placeholder="Digite seu nome")
      cpf = st.text_input("CPF", placeholder="Digite seu CPF")
      email = st.text_input("E-mail", placeholder="Digite seu e-mail")
      nome_usuario = st.text_input("Nome de usuário", placeholder="Escolha um nome de usuário")
      senha = st.text_input("Crie uma senha", placeholder="Digite sua senha", type="password")
      confirmar_senha = st.text_input("Confirme sua senha", placeholder="Confirme sua senha", type="password")

      # Botão para realizar o cadastro
      if st.button("Cadastrar"):
        mensagens = []

        if nome and email and senha and cpf and nome_usuario:
            if senha == confirmar_senha:
                senha_valida, mensagens = validaSenha(senha)
                if senha_valida:
                    if validaEmail(email):
                        if not verificar_email_existente(email):
                            if validaCPF(cpf):
                                cadastro(nome, email, senha, cpf, nome_usuario)
                                enviar_email_confirmacao(email, nome_usuario)  # Envia o e-mail de confirmação
                                st.success("Cadastro realizado com sucesso!")
                                mudar_tela("Login")
                            else:
                                st.error("CPF inválido.")
                        else:
                            st.error("Erro: Este e-mail já está cadastrado.")
                    else:
                        st.error("Erro: E-mail inválido.")
                else:
                    for mensagem in mensagens:
                        st.error(mensagem)
            else:
                st.error("Erro: As senhas não coincidem.")
        else:
            st.error("Erro: Por favor, preencha todos os campos.")
    
      # Botão para voltar à tela inicial
      if st.button("Voltar"):
        mudar_tela("Inicio")


elif menu == "Sobre":
    st.title("Sobre a Biblioteca")
    st.write("Aqui você pode encontrar informações sobre a nossa Biblioteca Virtual.")

elif menu == "Livros":
    st.title("Catálogo de Livros")
    st.write("Aqui estão os livros disponíveis para consulta.")

elif menu == "Autores":
    st.title("Autores")
    st.write("Conheça os autores disponíveis no catálogo.")











