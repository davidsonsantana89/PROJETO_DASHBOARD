import streamlit as st


st.title("PRINCIPAIS PROFISSÕES EM DADOS")

url_dataset = (
    "https://github.com/JorgeMiGo/Data-Science-Salaries-2023/tree/main/Dataset"
)

c1, c2 = st.columns(2)

with c1:
    st.image('imagens/imagem1.jpeg', 
             caption='Esta imagem foi gerada usando a inteligência artificial DALL-E 3', 
             width=300)
with c2:
    st.markdown(
        f"""Este dashboard apresenta as principais profissões da área de dados, 
        de acordo com a Análise Exploratória 
        de dados feita pelo time de estudantes: 
        **Carlos Mendonça**, **Davidson Santana** e **Tiago Fittipaldi**.
        
        \nA base dados utilizada, nessa análise exploratória de dados, pode ser acessada neste <a href="{url_dataset}">link</a>.\n
        """, unsafe_allow_html=True
    )
    st.write()
