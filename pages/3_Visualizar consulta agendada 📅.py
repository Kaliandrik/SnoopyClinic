import streamlit as st
import base64
with open("visualizarcom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("img/imagemdoagendamento.png", width=300)
st.title("Consulta agendada:")
st.sidebar.image("img/gatotop.jpg")

if "nomepet" in st.session_state and "medico" in st.session_state and "data" in st.session_state and "horario" in st.session_state and "nomedono" in st.session_state and "clinica" in st.session_state:
    st.title(f"Dono: {st.session_state["nomedono"]}")
    st.header(f"Pet: {st.session_state["nomepet"]}")
    st.header(f"Medico: {st.session_state["medico"]}")
    st.header(f"Horário: {st.session_state["horario"]}")
    st.header(f"Data:{st.session_state["data"]}")
    st.header(f"Clínica:{st.session_state["clinica"]}")
else:
    st.warning("Nenhuma consulta foi agendada ainda")


def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

background_image_path = "img/testedefundoo.jpeg"
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

import streamlit as st










