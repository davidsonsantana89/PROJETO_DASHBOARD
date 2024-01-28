import streamlit as st
import pandas as pd
import plotly.express as px

st.title("PRINCIPAIS PROFISSÕES EM DADOS")


# BASE DE DADOS UTILIZADA
url_dataset = "https://raw.githubusercontent.com/JorgeMiGo/Data-Science-Salaries-2023/main/Dataset/ds_salaries.csv"

df = pd.read_csv(url_dataset)
job = df["job_title"].value_counts()
job_principais = job[job > 101]


# SIDE BAR
opcao = st.sidebar.selectbox("Escolha a profissão", job_principais.index)

# CONTAINER 1
with st.container(height=500, border=False):
    col1, col2 = st.columns(2)

    if opcao == job_principais.index[0]:
        with col1:
            st.column_config.width = 80
            st.subheader(f"{opcao}")
            media_salario_anual = df[df["job_title"] == opcao]["salary_in_usd"].mean()
            st.metric(
                "Salário Médio Anual", value=f"US$ {round(media_salario_anual,2)}"
            )

            fig = px.histogram(
                df,
                x=df[df["job_title"] == opcao]["salary_in_usd"],
                nbins=10,
                title="Histograma dos Salários em Dolar",
                labels={"x": "Faixas salariais em USD"},
                height=270,
                width=270,
            )
            st.plotly_chart(fig)

        with col2:
            # fig = px.histogram(
            #     df,
            #     x=df[df["job_title"] == opcao]["salary_in_usd"],
            #     nbins=10,
            #     title="Histograma dos Salários em Dolar",
            #     labels={"x": "Faixas salariais em USD"},
            #     height=270,
            #     width=270,
            # )
            # st.plotly_chart(fig)
            st.write('teste')

    elif opcao == job_principais.index[1]:
        with col1:
            st.column_config.width = 80
            st.subheader(f"{opcao}")
            media_salario_anual = df[df["job_title"] == opcao]["salary_in_usd"].mean()
            st.metric(
                "Salário Médio Anual", value=f"US$ {round(media_salario_anual,2)}"
            )
        with col2:
            fig = px.histogram(
                df,
                x=df[df["job_title"] == opcao]["salary_in_usd"],
                nbins=10,
                title="Histograma dos Salários em Dolar",
                labels={"x": "Faixas salariais em USD"},
                height=270,
                width=270,
            )
            st.plotly_chart(fig)

    elif opcao == job_principais.index[2]:
        with col1:
            st.column_config.width = 80
            st.subheader(f"{opcao}")
            media_salario_anual = df[df["job_title"] == opcao]["salary_in_usd"].mean()
            st.write(f"MÉDIA SALARIAL ANUAL:")
            st.write(f"US$ {media_salario_anual:.2f}")
        with col2:
            fig = px.histogram(
                df,
                x=df[df["job_title"] == opcao]["salary_in_usd"],
                nbins=10,
                title="Histograma dos Salários em Dolar",
                labels={"x": "Faixas salariais em USD"},
                height=270,
                width=270,
            )
            st.plotly_chart(fig)

    elif opcao == job_principais.index[3]:
        with col1:
            st.column_config.width = 80
            st.subheader(f"{opcao}")
            media_salario_anual = df[df["job_title"] == opcao]["salary_in_usd"].mean()
            st.write(f"MÉDIA SALARIAL ANUAL:")
            st.write(f"US$ {media_salario_anual:.2f}")
        with col2:
            fig = px.histogram(
                df,
                x=df[df["job_title"] == opcao]["salary_in_usd"],
                nbins=10,
                title="Histograma dos Salários em Dolar",
                labels={"x": "Faixas salariais em USD"},
                height=270,
                width=270,
            )
            st.plotly_chart(fig)

    else:
        with col1:
            st.column_config.width = 80
            st.subheader(f"{opcao}")
            media_salario_anual = df[df["job_title"] == opcao]["salary_in_usd"].mean()
            st.write(f"MÉDIA SALARIAL ANUAL:")
            st.write(f"US$ {media_salario_anual:.2f}")
        with col2:
            fig = px.histogram(
                df,
                x=df[df["job_title"] == opcao]["salary_in_usd"],
                nbins=10,
                title="Histograma dos Salários em Dolar",
                labels={"x": "Faixas salariais em USD"},
                height=270,
                width=270,
            )
            st.plotly_chart(fig)


# CONTAINER 2
# with st.expander("Saiba mais"):
#     with st.container(border=True):
#         st.write("Container 2")
