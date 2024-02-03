import streamlit as st
import pandas as pd
import plotly.express as px

# BASE DE DADOS UTILIZADA
url_dataset = "https://raw.githubusercontent.com/JorgeMiGo/Data-Science-Salaries-2023/main/Dataset/ds_salaries.csv"

df = pd.read_csv(url_dataset)
job = df["job_title"].value_counts()
job_principais = job[job > 101]


# SIDE BAR
st.sidebar.image(
        "imagens/imagem2.jpeg", width=200, use_column_width=True)

opcao = st.sidebar.selectbox("Escolha a profissão", job_principais.index)

tile = st.container(height=120)


# CONTAINER 1
with st.container(height=500, border=False):
    col1, col2 = st.columns(2)

    if opcao == job_principais.index[0]:
        tile.title(opcao)
        with col1:
            st.column_config.width = 80
            # esse trecho exibe o card com o salário médio anual
            with st.container(height=105):
                media_salario_anual = df[df["job_title"] == opcao]["salary_in_usd"].mean()
                st.metric(
                "Salário Médio Anual", value=f"US$ {round(media_salario_anual,2)}"
            )
            with st.container(height=318):
                # esse trecho exibe o histograma da distribuição salarial anual
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
            st.column_config.width = 80

            with st.container(height=390):
                taxa_remota = st.radio(
                    "Selecione a taxa (%) de trabalho remoto",
                    options=["GERAL", 0, 50, 100], horizontal=True)

                if taxa_remota == "GERAL":
                    experiencia_salario = (
                        df[df["job_title"] == opcao].groupby("experience_level")[["salary_in_usd"]].mean()
                    )
                else:
                    experiencia_salario = (
                        df[(df["job_title"] == opcao) & (df["remote_ratio"] == taxa_remota)]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                fig2 = px.bar(
                    experiencia_salario,
                    x=experiencia_salario.index,
                    y="salary_in_usd",
                    title='''Nível de Experiência vs Salário em USD''',
                    labels={
                        "experience_level": "Nível de Experiência",
                        "salary_in_usd": "Salário em USD",
                        "remote_ratio": "Taxa de trabalho remoto",
                    },
                    category_orders={"experience_level": ["EN", "MI", "SE", "EX"]},
                    height=270,
                    width=280,
                )
                st.plotly_chart(fig2)

    elif opcao == job_principais.index[1]:
        tile.title(opcao)
        with col1:
            st.column_config.width = 80
            # esse trecho exibe o card com o salário médio anual
            with st.container(height=105):
                media_salario_anual = df[df["job_title"] == opcao][
                    "salary_in_usd"
                ].mean()
                st.metric(
                    "Salário Médio Anual", value=f"US$ {round(media_salario_anual,2)}"
                )
            with st.container(height=318):
                # esse trecho exibe o histograma da distribuição salarial anual
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
            st.column_config.width = 80

            with st.container(height=390):
                taxa_remota = st.radio(
                    "Selecione a taxa (%) de trabalho remoto",
                    options=["GERAL", 0, 50, 100],
                    horizontal=True,
                )

                if taxa_remota == "GERAL":
                    experiencia_salario = (
                        df[df["job_title"] == opcao]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                else:
                    experiencia_salario = (
                        df[
                            (df["job_title"] == opcao)
                            & (df["remote_ratio"] == taxa_remota)
                        ]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                fig2 = px.bar(
                    experiencia_salario,
                    x=experiencia_salario.index,
                    y="salary_in_usd",
                    title="""Nível de Experiência vs Salário em USD""",
                    labels={
                        "experience_level": "Nível de Experiência",
                        "salary_in_usd": "Salário em USD",
                        "remote_ratio": "Taxa de trabalho remoto",
                    },
                    category_orders={"experience_level": ["EN", "MI", "SE", "EX"]},
                    height=270,
                    width=280,
                )
                st.plotly_chart(fig2)

    elif opcao == job_principais.index[2]:
        tile.title(opcao)
        with col1:
            st.column_config.width = 80
            # esse trecho exibe o card com o salário médio anual
            with st.container(height=105):
                media_salario_anual = df[df["job_title"] == opcao][
                    "salary_in_usd"
                ].mean()
                st.metric(
                    "Salário Médio Anual", value=f"US$ {round(media_salario_anual,2)}"
                )
            with st.container(height=318):
                # esse trecho exibe o histograma da distribuição salarial anual
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
            st.column_config.width = 80

            with st.container(height=390):
                taxa_remota = st.radio(
                    "Selecione a taxa (%) de trabalho remoto",
                    options=["GERAL", 0, 50, 100],
                    horizontal=True,
                )

                if taxa_remota == "GERAL":
                    experiencia_salario = (
                        df[df["job_title"] == opcao]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                else:
                    experiencia_salario = (
                        df[
                            (df["job_title"] == opcao)
                            & (df["remote_ratio"] == taxa_remota)
                        ]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                fig2 = px.bar(
                    experiencia_salario,
                    x=experiencia_salario.index,
                    y="salary_in_usd",
                    title="""Nível de Experiência vs Salário em USD""",
                    labels={
                        "experience_level": "Nível de Experiência",
                        "salary_in_usd": "Salário em USD",
                        "remote_ratio": "Taxa de trabalho remoto",
                    },
                    category_orders={"experience_level": ["EN", "MI", "SE", "EX"]},
                    height=270,
                    width=280,
                )
                st.plotly_chart(fig2)

    elif opcao == job_principais.index[3]:
        tile.title(opcao)
        with col1:
            st.column_config.width = 80
            # esse trecho exibe o card com o salário médio anual
            with st.container(height=105):
                media_salario_anual = df[df["job_title"] == opcao][
                    "salary_in_usd"
                ].mean()
                st.metric(
                    "Salário Médio Anual", value=f"US$ {round(media_salario_anual,2)}"
                )
            with st.container(height=318):
                # esse trecho exibe o histograma da distribuição salarial anual
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
            st.column_config.width = 80

            with st.container(height=390):
                taxa_remota = st.radio(
                    "Selecione a taxa (%) de trabalho remoto",
                    options=["GERAL", 0, 50, 100],
                    horizontal=True,
                )

                if taxa_remota == "GERAL":
                    experiencia_salario = (
                        df[df["job_title"] == opcao]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                else:
                    experiencia_salario = (
                        df[
                            (df["job_title"] == opcao)
                            & (df["remote_ratio"] == taxa_remota)
                        ]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                fig2 = px.bar(
                    experiencia_salario,
                    x=experiencia_salario.index,
                    y="salary_in_usd",
                    title="""Nível de Experiência vs Salário em USD""",
                    labels={
                        "experience_level": "Nível de Experiência",
                        "salary_in_usd": "Salário em USD",
                        "remote_ratio": "Taxa de trabalho remoto",
                    },
                    category_orders={"experience_level": ["EN", "MI", "SE", "EX"]},
                    height=270,
                    width=280,
                )
                st.plotly_chart(fig2)

        
    else:
        tile.title(opcao)
        with col1:
            st.column_config.width = 80
            # esse trecho exibe o card com o salário médio anual
            with st.container(height=105):
                media_salario_anual = df[df["job_title"] == opcao][
                    "salary_in_usd"
                ].mean()
                st.metric(
                    "Salário Médio Anual", value=f"US$ {round(media_salario_anual,2)}"
                )
            with st.container(height=318):
                # esse trecho exibe o histograma da distribuição salarial anual
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
            st.column_config.width = 80

            with st.container(height=390):
                taxa_remota = st.radio(
                    "Selecione a taxa (%) de trabalho remoto",
                    options=["GERAL", 0, 50, 100],
                    horizontal=True,
                )

                if taxa_remota == "GERAL":
                    experiencia_salario = (
                        df[df["job_title"] == opcao]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                else:
                    experiencia_salario = (
                        df[
                            (df["job_title"] == opcao)
                            & (df["remote_ratio"] == taxa_remota)
                        ]
                        .groupby("experience_level")[["salary_in_usd"]]
                        .mean()
                    )
                fig2 = px.bar(
                    experiencia_salario,
                    x=experiencia_salario.index,
                    y="salary_in_usd",
                    title="""Nível de Experiência vs Salário em USD""",
                    labels={
                        "experience_level": "Nível de Experiência",
                        "salary_in_usd": "Salário em USD",
                        "remote_ratio": "Taxa de trabalho remoto",
                    },
                    category_orders={"experience_level": ["EN", "MI", "SE", "EX"]},
                    height=270,
                    width=280,
                )
                st.plotly_chart(fig2)


# CONTAINER 2
# with st.expander("Saiba mais"):
#     with st.container(border=True):
#         st.write("Container 2")
