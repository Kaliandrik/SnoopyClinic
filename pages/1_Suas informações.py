import streamlit as st
import base64
from PIL import Image
import numpy as np

# Inicializar o estado da imagem no session_state
if "uploaded_image" not in st.session_state:
    st.session_state["uploaded_image"] = None

# Adicionar CSS personalizado
with open("suasinformações.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def create_shaking_effect(image_path, output_path, shakes=10, intensity=5):
    img = Image.open(image_path)
    frames = []
    width, height = img.size

    for _ in range(shakes):
        dx = np.random.randint(-intensity, intensity)
        dy = np.random.randint(-intensity, intensity)
        frame = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        frame.paste(img, (dx, dy))
        frames.append(frame)

    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=50)


create_shaking_effect("img/natalsidebar.jpg", "img/natalsidebar_tremendo.gif")
if "nome" in st.session_state and "clinica" in st.session_state and "email" in st.session_state and "pet" in st.session_state:

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Adicionar uploader de imagem
        st.subheader("Foto de Perfil")
        uploaded_file = st.file_uploader("Clique para escolher uma imagem", type=["png", "jpg", "jpeg"])

        # Se uma imagem for carregada, salvá-la no session_state
        if uploaded_file is not None:
            st.session_state["uploaded_image"] = uploaded_file

        # Preparar a imagem a ser exibida (carregada ou padrão)
        if st.session_state["uploaded_image"]:
            # Converter o arquivo carregado pelo usuário para base64
            uploaded_file_content = st.session_state["uploaded_image"].getvalue()
            encoded_image = base64.b64encode(uploaded_file_content).decode()
        else:
            # Converter a imagem padrão para base64
            with open("img/usuario3.png", "rb") as f:
                encoded_image = base64.b64encode(f.read()).decode()

        # Exibir a imagem com estilo circular
        st.markdown(
            f"""
            <style>
            .profile-pic {{
                display: block;
                margin: 0 auto;
                border-radius: 50%;
                width: 300px;
                height: 300px;
                object-fit: cover;
                border: 5px solid #888cba;
            }}
            </style>
            <img class="profile-pic" src="data:image/jpeg;base64,{encoded_image}">
            """,
            unsafe_allow_html=True,
        )

st.title("Suas Informações:")
st.sidebar.image("img/natalsidebar_tremendo.gif")

if "nome" in st.session_state and "clinica" in st.session_state and "email" in st.session_state and "pet" in st.session_state:
    st.header(f"Nome: {st.session_state['nome']}")
    st.header(f"Clinica: {st.session_state['clinica']}")
    st.header(f"Email: {st.session_state['email']}")
    st.header(f"Pet: {st.session_state['pet']}")
else:
    st.warning("Nenhuma informação cadastrada. Por favor, preencha o cadastro em 'Cadastro'.")


def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str


background_image_path = "img/fundoinfo.jpg"
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
            border: 4px solid rgb(136, 140, 180);
            border-radius: 12px;
            }}
    </style>
    """, unsafe_allow_html=True)

st.image("img/imglegal.jpg")
