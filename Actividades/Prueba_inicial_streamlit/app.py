import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de Universidades Top", page_icon="🎓", layout="wide")

st.title("🎓 Análisis de las Mejores Universidades del Mundo")
st.markdown("Este dashboard interactivo permite explorar, analizar y visualizar datos simulados de las 20 mejores universidades del mundo.")

# 1. Simulación de datos
@st.cache_data
def load_data():
    np.random.seed(42)
    universities = [
        "Massachusetts Institute of Technology (MIT)", "University of Cambridge",
        "University of Oxford", "Harvard University", "Stanford University",
        "Imperial College London", "ETH Zurich", "National University of Singapore (NUS)",
        "UCL", "University of California, Berkeley (UCB)", "University of Chicago",
        "University of Pennsylvania", "Cornell University", "The University of Melbourne",
        "California Institute of Technology (Caltech)", "Yale University",
        "Peking University", "Princeton University", "The University of New South Wales",
        "The University of Sydney"
    ]
    regions = ["Norteamérica", "Europa", "Europa", "Norteamérica", "Norteamérica",
               "Europa", "Europa", "Asia", "Europa", "Norteamérica", "Norteamérica",
               "Norteamérica", "Norteamérica", "Oceanía", "Norteamérica", "Norteamérica",
               "Asia", "Norteamérica", "Oceanía", "Oceanía"]

    data = pd.DataFrame({
        "Universidad": universities,
        "Región": regions,
        "Puntaje General": np.round(np.random.uniform(85, 100, 20), 1),
        "Reputación Académica": np.round(np.random.uniform(90, 100, 20), 1),
        "Reputación Empleadores": np.round(np.random.uniform(80, 100, 20), 1),
        "Ratio Prof/Estudiante": np.round(np.random.uniform(70, 100, 20), 1),
        "Estudiantes Internacionales": np.round(np.random.uniform(60, 100, 20), 1),
    })
    # Ordenar por puntaje y asignar ranking
    data = data.sort_values(by="Puntaje General", ascending=False).reset_index(drop=True)
    data.insert(0, "Rank", range(1, 21))
    return data

df = load_data()

# 3. Interacción Dinámica (Sidebar)
st.sidebar.header("Filtros Interactivos")
selected_regions = st.sidebar.multiselect(
    "Selecciona la(s) Región(es)",
    options=df["Región"].unique(),
    default=df["Región"].unique()
)

score_range = st.sidebar.slider(
    "Rango de Puntaje General",
    min_value=float(df["Puntaje General"].min()),
    max_value=float(df["Puntaje General"].max()),
    value=(float(df["Puntaje General"].min()), float(df["Puntaje General"].max()))
)

# Filtrar dataset
df_filtered = df[
    (df["Región"].isin(selected_regions)) & 
    (df["Puntaje General"] >= score_range[0]) & 
    (df["Puntaje General"] <= score_range[1])
]

# Tabs para las secciones requeridas
tab1, tab2, tab3 = st.tabs(["📊 Análisis Cuantitativo", "📈 Análisis Gráfico", "📝 Análisis Cualitativo"])

with tab1:
    st.header("Análisis Cuantitativo")
    st.dataframe(df_filtered.style.background_gradient(cmap='Blues', subset=['Puntaje General']), use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Universidades", len(df_filtered))
    col2.metric("Promedio Puntaje General", f"{df_filtered['Puntaje General'].mean():.2f}" if not df_filtered.empty else "0")
    col3.metric("Mejor Puntaje", f"{df_filtered['Puntaje General'].max()}" if not df_filtered.empty else "0")
    
    st.subheader("Estadísticas Descriptivas")
    if not df_filtered.empty:
        st.dataframe(df_filtered.describe().T)
    else:
        st.warning("No hay datos con los filtros actuales.")

with tab2:
    st.header("Análisis Gráfico")
    if not df_filtered.empty:
        # Gráfico de Barras
        st.subheader("Puntaje General por Universidad")
        fig_bar = px.bar(
            df_filtered, 
            x="Universidad", 
            y="Puntaje General", 
            color="Región",
            title="Puntajes de las Universidades Filtradas",
            text="Puntaje General"
        )
        fig_bar.update_traces(textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Gráfico de Dispersión
        st.subheader("Reputación Académica vs Empleadores")
        fig_scatter = px.scatter(
            df_filtered, 
            x="Reputación Académica", 
            y="Reputación Empleadores", 
            size="Puntaje General", 
            color="Región",
            hover_name="Universidad",
            title="Comparación de Reputaciones (Burbujas por Puntaje General)"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("Ajusta los filtros para ver las gráficas.")

with tab3:
    st.header("Análisis Cualitativo")
    if not df_filtered.empty:
        st.markdown("### Hallazgos Clave a partir de los datos interactivos")
        
        top_uni = df_filtered.iloc[0]
        st.markdown(f"- **Líder Actual:** En esta selección, la institución líder es **{top_uni['Universidad']}** ({top_uni['Región']}), con un puntaje general de **{top_uni['Puntaje General']}**.")
        
        region_counts = df_filtered['Región'].value_counts()
        top_region = region_counts.index[0]
        st.markdown(f"- **Dominancia Regional:** La región con mayor presencia en este rango es **{top_region}** con **{region_counts.iloc[0]}** universidades representadas.")
        
        # Correlación
        corr = df_filtered['Reputación Académica'].corr(df_filtered['Reputación Empleadores'])
        corr_text = "alta" if abs(corr) > 0.7 else "moderada" if abs(corr) > 0.4 else "baja"
        st.markdown(f"- **Relación Académica-Laboral:** Existe una correlación {corr_text} ({corr:.2f}) entre la reputación académica y la percepción de los empleadores, lo que indica cómo el rigor académico impacta la empleabilidad en este conjunto.")
        
        st.info("💡 La interacción con los filtros laterales modifica instantáneamente este análisis cualitativo, adaptándose al contexto de la muestra elegida.")
    else:
        st.warning("No hay datos para analizar.")
