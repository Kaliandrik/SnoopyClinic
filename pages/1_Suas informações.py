import streamlit as st
import base64
from PIL import Image
import numpy as np


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
col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.header("foto de perfil")
with col2:
    st.image("img/usuario3.png", width=900)
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








