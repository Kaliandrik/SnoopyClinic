import streamlit as st
import base64
with open("sobrenos.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.image("img/snoopynatal_saida_volta.gif")


col1, col2, col3 = st.columns([1, 2, 1])  

with col2:
    st.image("img/imagemlegaldoatendimento_tremendo.gif", )
st.markdown(
    """
    <div style="
        background-color: #f9f9f9; 
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        margin-top: 40px;
    ">
        <h2 style="color: #2e86c1; text-align: center;">Sobre Nós – Snoopy Clinic 🐾</h2>
        <p style="color: #4d4d4d; font-size: 23px; line-height: 1.6;">
            Na <b>Snoopy Clinic</b>, nossa missão é cuidar da saúde e do bem-estar dos seus pets com dedicação, carinho e excelência. 
            Somos uma clínica veterinária apaixonada por animais e comprometida em oferecer o melhor atendimento tanto para eles quanto para você, tutor.
        </p>
        <p style="color: #4d4d4d; font-size: 23px; line-height: 1.6;">
            Com uma equipe de profissionais qualificados e em constante atualização, oferecemos uma ampla gama de serviços para garantir que o 
            seu amigo de quatro patas receba os cuidados que merece. Aqui, tratamos cada pet como um membro da nossa família.
        </p>
        <p style="color: #4d4d4d; font-size: 23px; line-height: 1.6;">
            Venha nos visitar e descubra por que tantos tutores confiam na Snoopy Clinic para cuidar de seus melhores amigos! 💙🐕🐈
        </p>
        <p style="color: black; font-size: 23px; line-height: 1.6;">
        FUNDADORES: Kaliandrik, Maria Flor, Lara, Giovanna Lima, Giovanna Albuquerque e Maria Vitória.
        </p>
        <div style="text-align: center; margin-top: 20px;">
            <p style="font-size: 18px; color: #2e86c1;"><b>📍 Endereço:</b> EEEP-Sebastião Vasconcelos Sobrinho</p>
            <p style="font-size: 18px; color: #2e86c1;"><b>📞 Contato:</b> (88) 99819-2669</p>
            <p style="font-size: 18px; color: #2e86c1;"><b>📧 E-mail:</b> snoopyclinic@gmail.com</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

background_image_path = "img/fundosobrenosclinic.jpg" 
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