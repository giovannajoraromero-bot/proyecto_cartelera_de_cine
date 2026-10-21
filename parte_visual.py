import streamlit as st
from PIL import Image

# Configuración inicial de la página
st.set_page_config(page_title="Cine Mushu", layout="wide")

# Función para nivelar las imágenes (Pillow)
def cargar_y_nivelar_imagen(ruta_archivo):
    try:
        img = Image.open(ruta_archivo)
        img_redimensionada = img.resize((400, 550))
        return img_redimensionada
    except:
        return ruta_archivo

# Inicializar las variables en memoria (st.session_state)
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "cartelera"
if "peli_elegida" not in st.session_state:
    st.session_state.peli_elegida = ""

# --- FUNCIÓN DE LA DULCERÍA Y COMPRA ---
def mostrar_dulceris():
    st.title("🍿 Dulcería y Boletos - Cine Mushu")
    st.success(f"🎬 ¡Excelente elección! Has seleccionado: **{st.session_state.peli_elegida}**")
    st.write("Personaliza tus boletos y snacks para la función:")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎟️ Entrada al Cine")
        # Selector numérico para los boletos
        cantidad_boletos = st.number_input("Cantidad de boletos:", min_value=1, max_value=10, value=1)
        precio_boleto = 45  # Precio por boleto
        total_boletos = cantidad_boletos * precio_boleto
        st.write(f"Subtotal Boletos: **${total_boletos}**")
        
    with col2:
        st.subheader("🥤 Tus Snacks")
        tamano = st.selectbox("Tamaño de Palomitas:", ["Medianas ($60)", "Grandes ($80)", "Combo Gigante ($120)"])
        sabor = st.selectbox("Sabor de Palomitas:", ["Mantequilla", "Caramelo", "Mixtas"])
        bebida = st.selectbox("Refresco:", ["Coca-Cola", "Sprite", "Fanta"])
        
        # Calcular precio del snack según la opción
        if "Medianas" in tamano:
            precio_snack = 60
        elif "Grandes" in tamano:
            precio_snack = 80
        else:
            precio_snack = 120

    st.markdown("---")
    
    # CALCULAR EL TOTAL GENERAL
    total_general = total_boletos + precio_snack
    st.header(f"💰 Total a pagar: ${total_general}")
    
    # BOTONES DE ACCIÓN
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("⬅️ Volver a la Cartelera"):
            st.session_state.pantalla = "cartelera"
            st.rerun()
            
    with col_btn2:
        # BOTÓN MÁGICO CON CONFETI
        if st.button("🛒 Confirmar y Pagar Compra"):
            st.balloons()  # Esto lanza los globos/confeti en la pantalla
            st.success(f"🎉 ¡Compra Exitosa! Disfrutarás de **{st.session_state.peli_elegida}** ({cantidad_boletos} boletos) con tus palomitas {sabor} y tu {bebida}.")

# --- FUNCIÓN DE LA CARTELERA ---
def mostrar_cartelera():
    st.title("🐉 Bienvenidos a Cine Mushu")
    st.write("Tu rincón favorito para disfrutar de los mejores estrenos.")
    st.markdown("---")

    # FILA 1
    fila1_col1, fila1_col2, fila1_col3 = st.columns(3)
    with fila1_col1:
        st.image(cargar_y_nivelar_imagen("alicia.jpg"), use_container_width=True)
        st.subheader("1. Alicia en el País de las Maravillas")
        if st.button("🎟️ Ver esta película", key="btn1"):
            st.session_state.peli_elegida = "Alicia en el País de las Maravillas"
            st.session_state.pantalla = "dulceria"
            st.rerun()

    with fila1_col2:
        st.image(cargar_y_nivelar_imagen("chaplin.jpg"), use_container_width=True)
        st.subheader("2. Chaplin")
        if st.button("🎟️ Ver esta película", key="btn2"):
            st.session_state.peli_elegida = "Chaplin"
            st.session_state.pantalla = "dulceria"
            st.rerun()

    with fila1_col3:
        st.image(cargar_y_nivelar_imagen("la_llorona.jpg"), use_container_width=True)
        st.subheader("3. La Llorona")
        if st.button("🎟️ Ver esta película", key="btn3"):
            st.session_state.peli_elegida = "La Llorona"
            st.session_state.pantalla = "dulceria"
            st.rerun()

    # FILA 2
    fila2_col1, fila2_col2, fila2_col3 = st.columns(3)
    with fila2_col1:
        st.image(cargar_y_nivelar_imagen("mickey.jpg"), use_container_width=True)
        st.subheader("4. Mickey Mouse")
        if st.button("🎟️ Ver esta película", key="btn4"):
            st.session_state.peli_elegida = "Mickey Mouse"
            st.session_state.pantalla = "dulceria"
            st.rerun()

    with fila2_col2:
        st.image(cargar_y_nivelar_imagen("scream.jpg"), use_container_width=True)
        st.subheader("5. Scream")
        if st.button("🎟️ Ver esta película", key="btn5"):
            st.session_state.peli_elegida = "Scream"
            st.session_state.pantalla = "dulceria"
            st.rerun()

    with fila2_col3:
        st.image(cargar_y_nivelar_imagen("toy_store.jpg"), use_container_width=True)
        st.subheader("6. Toy Store")
        if st.button("🎟️ Ver esta película", key="btn6"):
            st.session_state.peli_elegida = "Toy Store"
            st.session_state.pantalla = "dulceria"
            st.rerun()


if st.session_state.pantalla == "cartelera":
    mostrar_cartelera()
else:
    mostrar_dulceris()


