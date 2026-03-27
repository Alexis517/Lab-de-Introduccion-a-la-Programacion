import streamlit as st

st.set_page_config(layout="wide")

# ==============================
# CSS (COLORES SUAVES / NO BRILLANTES)
# ==============================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #1e293b, #334155);
    color: #e2e8f0;
}

/* CARD */
.card {
    width: 300px;
    border-radius: 15px;
    overflow: hidden;
    background: #2d3748;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
}

/* IMAGEN */
.card img {
    width: 100%;
    height: 170px;
    object-fit: cover;
}

/* CONTENIDO */
.card-body {
    padding: 15px;
    text-align: center;
}

.card-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #f1f5f9;
}

.card-text {
    font-size: 14px;
    color: #cbd5f5;
}

/* BOTONES */
.stButton > button {
    width: 100%;
    border-radius: 8px;
    background: #3b82f6;
    color: white;
    border: none;
    padding: 8px;
}

.stButton > button:hover {
    background: #2563eb;
}

/* INPUTS */
.stTextInput input, .stNumberInput input, .stSelectbox div {
    background: #1e293b !important;
    color: white !important;
    border: 1px solid #475569 !important;
    border-radius: 8px !important;
}

/* LOGIN CARD */
.login {
    width: 350px;
    margin: auto;
    margin-top: 100px;
    padding: 25px;
    border-radius: 15px;
    background: #2d3748;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# SESSION
# ==============================
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.intentos = 3

# ==============================
# LOGIN
# ==============================
if not st.session_state.login:

    st.markdown('<div class="login">', unsafe_allow_html=True)
    st.markdown("## 🔐 Iniciar Sesión")

    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if user == "Admin" and password == "Admin2026":
            st.session_state.login = True
            st.rerun()
        else:
            st.session_state.intentos -= 1
            st.error(f"Error | Intentos: {st.session_state.intentos}")

            if st.session_state.intentos == 0:
                st.error("🚫 Acceso bloqueado")

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# MENÚ CON CARDS
# ==============================
else:
    st.title("🚀 Menú Principal")

    col1, col2, col3 = st.columns(3)

    # -------- CARD 1 --------
    with col1:
        st.markdown("""
        <div class="card">
            <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb">
            <div class="card-body">
                <div class="card-title">Clasificar Número</div>
                <div class="card-text">Analiza signo y paridad.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        num = st.number_input("Número", step=1, key="num")

        if st.button("Clasificar"):
            if num > 0:
                st.success("Positivo")
            elif num < 0:
                st.warning("Negativo")
            else:
                st.info("Cero")

            st.write("Par" if num % 2 == 0 else "Impar")

    # -------- CARD 2 --------
    with col2:
        st.markdown("""
        <div class="card">
            <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f">
            <div class="card-body">
                <div class="card-title">Categoría Edad</div>
                <div class="card-text">Clasifica por edad.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        edad = st.number_input("Edad", step=1, key="edad")

        if edad <= 12:
            st.info("Niño")
        elif edad <= 17:
            st.info("Adolescente")
        elif edad <= 64:
            st.success("Adulto")
        else:
            st.warning("Adulto mayor")

    # -------- CARD 3 --------
    with col3:
        st.markdown("""
        <div class="card">
            <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d">
            <div class="card-body">
                <div class="card-title">Calcular Tarifa</div>
                <div class="card-text">Aplica descuentos.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        dia = st.selectbox("Día", list(range(1,8)))
        estudiante = st.checkbox("Estudiante")
        miembro = st.checkbox("Miembro")

        if st.button("Calcular"):
            total = 100
            if dia in [6,7]:
                total += 20
            if estudiante:
                total *= 0.85
            if miembro:
                total *= 0.9

            st.success(f"${total:.2f}")

    # CERRAR SESIÓN
    if st.button("Cerrar sesión"):
        st.session_state.login = False
        st.session_state.intentos = 3
        st.rerun()
