
#Pagina principal del App multipaginas
#streamlit run c:/LCT_PYTHON/STREAMLIT/SENSOR_WATTS/SW_DASHBOARD/main.py

import streamlit as st
import pandas as pd
from volt_pag_1 import volt
from pot_pag_2 import pot
from energ_pag_3 import energ
from fase_pag_4 import fase
from frec_pag_5 import frec
from PIL import Image

# Título de la aplicación

c1,c2 = st.columns([0.25,1])
icono_path = "C:/LCT_PYTHON/STREAMLIT/SENSOR_WATTS/SW_DASHBOARD/sw_imagen/SW_ICON.png"
icono = Image.open(icono_path)
with c1:
    st.image(icono, width= 120)
with c2:
    st.write("## Tablero SensorWatts Datos CSV")

# Cargar el archivo CSV
archivo = st.file_uploader("Cargue archivo CSV", type=["csv"])

if archivo is not None:
    datos = pd.read_csv(archivo)
    
else:
    "Cargue archivo de Datos Tipo: CSV"
    datos = None

if datos is not None:  
# Crear un sidebar para seleccionar la página
    
    page = st.sidebar.selectbox("Seleccione la medicion", ["Voltaje & Corriente", "Potencias", "Energias", "Fase", "Frecuencia"])

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
      
