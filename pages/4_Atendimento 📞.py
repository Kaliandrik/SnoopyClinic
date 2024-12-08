import streamlit as st
import base64

with open("atendimento.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
    st.image("img/fotolegalatendimento.jpg", width=300)
st.title("Está com problemas? 😥")
st.header("Como podemos ajudar você? 😁")
st.sidebar.image("img/snoopy.jpg")


ajuda = st.selectbox("Qual o seu problema?", ["Selecione uma opção", "Estou com problemas no cadastro.", "Como visualizo minhas informações?", "Como funciona o agendamento de consultas?"])
if st.button("Clique aqui para resolvermos seu problema!"):
    if ajuda == "Estou com problemas no cadastro.":
        st.markdown(
            """
            <div style="
                background-color: #f0f8ff; 
                padding: 15px; 
                border-radius: 10px; 
                color: #000; 
                font-size: 16px;
            ">
            <p style="color: black; font-size: 16px;">
            Olá! Sentimos muito pelo transtorno com o cadastro. Estamos aqui para ajudar você a resolver isso rapidamente.
            <br><br>
            Por favor, envie mais detalhes sobre o problema (como uma captura de tela ou a mensagem de erro, se possível), e nossa equipe entrará em contato para solucionar o mais breve possível.
            <br><br>
            Se preferir, você também pode nos ligar pelo <b>(88) 99756-3445</b> ou enviar um e-mail para <b>snoopyclinic@gmail.com</b>. 
            <br><br>
            Agradecemos pela paciência e estamos à disposição!
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        uploaded_file = st.file_uploader("Envie uma imagem", type=["jpg", "png", "jpeg"])

        if uploaded_file is not None:
            st.image(uploaded_file, caption="Imagem enviada", use_column_width=True)
    elif ajuda == "Como visualizo minhas informações?":
        st.markdown(
            """
            <div style="
                background-color: #f0f8ff; 
                padding: 15px; 
                border-radius: 10px; 
                color: #000; 
                font-size: 16px;
            ">
            <p style="color: black; font-size: 16px;">
            Olá! Para visualizar suas informações clique na aba "Suas informações" situada no menu ao lado.
            <br><br>
            Lembrando que a mensagem só aparecerá caso você possua um cadastro no site.
            <br><br>
            Agradecemos pela paciência e estamos à disposição!
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif ajuda == "Como funciona o agendamento de consultas?":
        st.markdown(
            """
            <div style="
                background-color: #f0f8ff; 
                padding: 15px; 
                border-radius: 10px; 
                color: #000; 
                font-size: 16px;
            ">
            <p style="color: black; font-size: 16px;">
            Para agendar uma consulta você deve clicar na aba "Agendar consulta" situada no menu ao lado.
            <br><br>
            Lembrando que a mensagem só aparecerá caso você possua um cadastro no site.
            <br><br>
            Agradecemos pela paciência e estamos à disposição!
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif ajuda == "Selecione uma opção":
        st.warning("Por favor, selecione uma opção válida.")


def get_base64_image(file_path):
    with open(file_path, "rb") as image:  
        base64_str = base64.b64encode(image.read()).decode()
    return base64_str

background_image_path = "img/atendimentofundobom.jpg" 
base64_image = get_base64_image(background_image_path)

st.markdown(f"""
    <style>
        .stApp {{
            background-color: white;  
            background-image: url("data:image/jpeg;base64,{base64_image}"); 
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed; 
            background-position: 250px 50%;  
            }}
    </style>
    """, unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])  

with col2:
    st.image("img/desenhoatendimento.jpg", width=300)