import streamlit as st
import base64
from PIL import Image
import numpy as np
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


create_shaking_effect("img/snoopynatal.png", "img/snoopynatal_tremendo.gif")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def cadastro():
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
            background-position: 250px 50%;  
            }}
    </style>
    """, unsafe_allow_html=True)

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
        clinica = st.selectbox("QUAL CLINICA VOCÊ DESEJA?", ["Snoopy Clinic (SOBRAL)", "Snoopy Clinic (Tianguá)"])
        input_email = st.text_input("DIGITE SEU EMAIL:", placeholder="seuemail@gmail.com")
        selecionar_pet = st.selectbox("QUAL O SEU PET🐶?", ["Cachorro", "Gato", "Aves", "Répteis e anfíbios", "Outro"])
        
        if st.button("Enviar"):
            if input_name == "":
                st.error("Preencha o seu nome de usuário")
            elif input_email == "":
                st.error("Preencha seu email completo.")
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
