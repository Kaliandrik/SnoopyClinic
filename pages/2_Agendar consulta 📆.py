import streamlit as st
import datetime
import base64


with open("agendarconsulta.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str


background_image_default = get_base64_image("img/denovo3.jpg")
background_image_success = get_base64_image("img/fundodpsdeagendar.jpg")


if "agendar_consulta" in st.session_state and st.session_state["agendar_consulta"]:
    background_image = background_image_success
else:
    background_image = background_image_default

st.markdown(f"""
    <style>
        .stApp {{
            background-color: white;  
            background-image: url("data:image/jpeg;base64,{background_image}");
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed; 
        }}
    </style>
    """, unsafe_allow_html=True)


if "consultas" not in st.session_state:
    st.session_state["consultas"] = []


def agendar_consulta():
    st.image("img/imagemagendar.png")
    st.sidebar.image("img/mulhersegurandogato.jpg")
    st.title("Agendar consulta:")
    
    if "agendar_consulta" in st.session_state and st.session_state["agendar_consulta"]:
        st.markdown(
            """
            <div style='
                text-align: center;
                background-color: blue;
                color: white;
                border-radius: 50%;
                width: 340px;
                height: 340px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3); 
                text-shadow: 5px 4px 10px rgba(0, 0, 0, 0.5);
            '>
                <h3 style='margin: 0; font-size: 40px;'>CONSULTA AGENDADA COM ÊXITO!</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.header("Clique no botão abaixo para acessar as informações de sua consulta.")
       
        if st.button("Consultas agendadas ℹ️"):
            st.switch_page("pages/3_Visualizar consulta agendada 📅.py")
    else:
        nome_dono = st.text_input("Digite seu nome:")
        nome_pet = st.text_input("Nome do seu animalzinho:")
        nome_medico = st.selectbox("Escolha o Médico", ["Dr. João", "Dra. Maria", "Dr. Bruno", "Dr. Gustavo"])
        data_consulta = st.date_input("Data da Consulta", min_value=datetime.date.today())

        horarios = {
            "Dr. João": ["9:00H", "10:30H", "11:00H", "12:00H", "13:00H"],
            "Dra. Maria": ["7:00H", "14:30H", "11:30H", "12:30H", "13:50H"],
            "Dr. Bruno": ["9:45H", "15:00H", "16:00H", "16:45H", "17:00H"],
            "Dr. Gustavo": ["18:00H", "18:30H", "19:00H", "19:30H", "20:00H"],
        }
        horario_consulta = st.selectbox("Horários disponíveis:", horarios[nome_medico])
        col1, col2, col3 = st.columns([1, 2, 1])  

        with col2:
            if st.button("Agendar"):
                if not nome_pet:
                    st.error("Preencha o nome do seu pet.")
                elif not nome_dono:
                    st.error("Preencha o seu nome.")
                else:
                    st.session_state["nomepet"] = nome_pet
                    st.session_state["nomedono"] = nome_dono
                    st.session_state["medico"] = nome_medico
                    st.session_state["data"] = data_consulta
                    st.session_state["horario"] = horario_consulta
                    st.session_state["agendar_consulta"] = True
                    st.success("Cadastro realizado com sucesso!")


if "cadastro_realizado" not in st.session_state or not st.session_state["cadastro_realizado"]:
    st.warning("Acesso negado! Você precisa se cadastrar antes de acessar esta página.")
    st.stop()

agendar_consulta()
