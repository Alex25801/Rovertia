import streamlit as st
import random

def humedad(min_valor=30, max_valor=60):
    """Función que define el parámetro óptimo de humedad"""
    parametro_optimo = (min_valor, max_valor)
    return random.randint(min_valor, max_valor)

def comparar_dato(dato_recibido, parametro_optimo, min_valor, max_valor):
    """Compara el dato recibido con los parámetros óptimos"""
    if min_valor <= dato_recibido <= max_valor:
        return "? El valor está dentro del rango óptimo"
    elif dato_recibido > max_valor:
        return "? El valor está por encima del rango óptimo" 
    else:
        return "? El valor está por debajo del rango óptimo"

def main():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: black;  /* Fondo negro para toda la aplicación */
            color: white;  /* Color del texto */
        }
        h1, h2, h3 {
            color: #00FF7F;  /* Color verde claro para los encabezados */
        }
        .stButton>button {
            background-color: #00FF7F;  /* Color verde para el botón */
            color: black;  /* Color del texto del botón */
            border: None;  /* Sin borde */
            border-radius: 5px;  /* Bordes redondeados */
            padding: 10px;  /* Espaciado interno */
            font-size: 16px;  /* Tamaño de fuente */
            font-weight: bold;  /* Texto en negrita */
        }
        .stButton>button:hover {
            background-color: #32CD32;  /* Color del botón al pasar el mouse */
        }
        .stNumberInput>div>label {
            color: #00FF7F;  /* Color de la etiqueta del input */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("??? Analizador de Humedad")
    st.write("### Bienvenido! Soy Rovert, tu asistente para analizar datos de humedad")
    
    # Valores mínimos y máximos fijos
    min_valor = 30
    max_valor = 60
    
    # Input del usuario
    dato_recibido = st.number_input("Ingresa el valor de humedad a analizar:", 
                                   min_value=0, 
                                   max_value=100,
                                   value=45)
    
    if st.button("Analizar"):
        parametro_optimo = humedad(min_valor, max_valor)
        
        # Mostrar resultados
        st.write("---")
        st.write("### Resultados del análisis")
        st.write(f"?? Rango óptimo: {min_valor}% - {max_valor}%")
        st.write(f"?? Valor analizado: {dato_recibido}%")
        
        resultado = comparar_dato(dato_recibido, parametro_optimo, min_valor, max_valor)
        st.write(resultado)
        
        # Visualización
        progress = dato_recibido
        st.progress(progress/100)
        
        if min_valor <= dato_recibido <= max_valor:
            st.balloons()
if __name__ == "__main__":
    main()
