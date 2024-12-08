import streamlit as st
import base64

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def toggle_senha():
    st.session_state.senha_visible = not st.session_state.senha_visible


def cadastro():
    senha_visible = False
    if 'senha_visible' not in st.session_state:
        st.session_state.senha_visible = senha_visible

    if "cadastro_realizado" in st.session_state and st.session_state["cadastro_realizado"]:
        background_image_path = "img/fundonatal.jpg"  
    else:
        background_image_path = "img/fundonovoo.jpg"

    base64_image = get_base64_image(background_image_path)
    
    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{base64_image}");
            background-size: cover; 
            background-position: center;
            background-attachment: fixed;
        }}
        @media (max-width: 768px) {{
            .stApp {{
                background-attachment: scroll; /* Resolve problemas em celulares */
                background-position: center center;
            }}
        }}
        @keyframes preloader {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        .stApp {{
            animation: preloader 0.8s ease-in-out;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Sidebar e título
    st.sidebar.image("img/logosemfundo.png")
    st.title("Snoopy Clinic")
    st.title("Aqui cada patinha importa.")  
    st.title("Cadastro:")
    st.markdown("<div style='margin-top: -160px;'>", unsafe_allow_html=True)

    
    if "cadastro_realizado" in st.session_state and st.session_state["cadastro_realizado"]:
        st.markdown(
            """
            <div style='
                text-align: center;
                background-color: green;
                color: white;
                border-radius: 50%;
                width: 340px;
                height: 340px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto;
            '>
                <h1 style='margin: 0; font-size: 40px;'>CADASTRO REALIZADO COM ÊXITO!</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image("img/snoopynatal_tremendo.gif")
    else:
       
        input_name = st.text_input("DIGITE SEU NOME:", placeholder="Seu nome")
        clinica = st.selectbox("QUAL CLÍNICA VOCÊ DESEJA?", ["Snoopy Clinic (SOBRAL)", "Snoopy Clinic (Tianguá)"])
        input_email = st.text_input("DIGITE SEU EMAIL:", placeholder="seuemail@gmail.com")
        input_senha = st.text_input("Digite sua senha:", type="text" if st.session_state.senha_visible else "password")
        selecionar_pet = st.selectbox("QUAL O SEU PET🐶?", ["Cachorro", "Gato", "Aves", "Répteis e anfíbios", "Outro"])
        
        if st.button("Enviar"):
            if input_name == "":
                st.error("Preencha o seu nome de usuário")
            elif input_email == "":
                st.error("Preencha seu email completo.")
            elif len(input_senha) < 5:
                st.error("Sua senha deve conter no mínimo 5 dígitos.")
            elif input_senha == "":
                st.error("Digite sua senha.")
            elif not input_email.endswith("@gmail.com"):
                st.error("Por favor, insira um e-mail válido que termine com @gmail.com.")
            else:
                
                st.session_state["nome"] = input_name
                st.session_state["clinica"] = clinica
                st.session_state["email"] = input_email
                st.session_state["pet"] = selecionar_pet
                st.session_state["cadastro_realizado"] = True
                st.success("Cadastro realizado com sucesso!")


cadastro()
