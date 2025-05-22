
# Pagina principal del App multipaginas
# streamlit run c:/LCT_PYTHON/STREAMLIT/SENSOR_WATTS/SW_DASHBOARD/main.py
# URL de la App SensorWatts en GitHub
# https://github.com/lctdidacticos/sensorwatts_dashboard

import streamlit as st
import pandas as pd
from estadist_pag_7 import stadist
from volt_pag_1 import volt
from pot_pag_2 import pot
from energ_pag_3 import energ
from fase_pag_4 import fase
from frec_pag_5 import frec
from costo_pag_6 import costo
from PIL import Image

# Título de la aplicación
c1, c2 = st.columns([0.25, 0.75])  # Cambio de (0.25,1) a (0.25,0.75)

# SENSOR_WATTS\SW_DASHBOARD\sw_imagen
icono_path = "sw_imagen/SW_ICON.png"
icono = Image.open(icono_path)
with c1:
    st.image(icono, use_container_width=True)
with c2:
    st.write("## Estadísticas SensorWatts")

# Cargar el archivo CSV
archivo = st.file_uploader("Cargue archivo CSV", type=["csv"])

if archivo is not None:
    datos = pd.read_csv(archivo)

    # Reparar columna "Tiempo" si existe
    if "Tiempo" in datos.columns:
        datos["Tiempo"] = datos["Tiempo"].astype(str).str.strip()
        # Corregir "24:MM:SS" por "00:MM:SS" para evitar error de conversión
        datos["Tiempo"] = datos["Tiempo"].str.replace(r"^24:(\d{2}):(\d{2})$", r"00:\1:\2", regex=True)

else:
    datos = None

if datos is not None:
    # Crear un sidebar para seleccionar la página
    page = st.sidebar.selectbox(
        "Seleccione la medición",
        [
            "Voltaje & Corriente",
            "Potencias",
            "Energias",
            "Fase",
            "Frecuencia",
            "Costo Energia",
            "Estadisticas",
        ],
    )

    # Mostrar la página seleccionada
    if page == "Voltaje & Corriente":
        volt(datos)
    elif page == "Potencias":
        pot(datos)
    elif page == "Energias":
        energ(datos)
    elif page == "Fase":
        fase(datos)
    elif page == "Frecuencia":
        frec(datos)
    elif page == "Costo Energia":
        costo(datos)
    elif page == "Estadisticas":
        stadist(datos)

      
