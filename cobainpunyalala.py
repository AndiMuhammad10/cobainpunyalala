import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Kalkulator Gas Ideal",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Kalkulator Gas Ideal Interaktif")
st.markdown("### Hukum Gas + Animasi Studi Kasus + Grafik Hubungan Variabel")

# =========================
# SIDEBAR MENU
# =========================
menu = st.sidebar.radio(
    "📌 Pilih Menu",
    [
        "🏠 Home",
        "📘 Kalkulator Gas",
        "🎬 Animasi Studi Kasus",
        "📈 Grafik Hubungan Variabel"
    ]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":

    st.header("Selamat Datang 👋")

    st.write("""
    Aplikasi ini berisi:

    ✅ Kalkulator hukum gas  
    ✅ Animasi studi kasus gas ideal  
    ✅ Grafik hubungan variabel gas  

    Dibuat menggunakan:
    - Python
    - Streamlit
    - Plotly
    - Matplotlib
    """)

# =========================
# KALKULATOR GAS
# =========================
elif menu == "📘 Kalkulator Gas":

    st.header("📘 Kalkulator Hukum Gas")

    hukum = st.selectbox(
        "Pilih Hukum Gas",
        [
            "Hukum Boyle",
            "Hukum Charles",
            "Hukum Gay-Lussac",
            "Hukum Avogadro",
            "Persamaan Gas Ideal"
        ]
    )

    # ====================================
    # HUKUM BOYLE
    # ====================================
    if hukum == "Hukum Boyle":

        st.subheader("Hukum Boyle")
        st.latex(r"P_1V_1 = P_2V_2")

        P1 = st.number_input("P1", value=1.0)
        V1 = st.number_input("V1", value=1.0)
        P2 = st.number_input("P2", value=1.0)

        if st.button("Hitung V2"):
            V2 = (P1 * V1) / P2
            st.success(f"V2 = {V2:.3f}")

    # ====================================
    # HUKUM CHARLES
    # ====================================
    elif hukum == "Hukum Charles":

        st.subheader("Hukum Charles")
        st.latex(r"\frac{V_1}{T_1} = \frac{V_2}{T_2}")

        V1 = st.number_input("V1 ", value=1.0)
        T1 = st.number_input("T1 (K)", value=273.0)
        T2 = st.number_input("T2 (K)", value=300.0)

        if st.button("Hitung V2 "):
            V2 = (V1 * T2) / T1
            st.success(f"V2 = {V2:.3f}")

    # ====================================
    # HUKUM GAY LUSSAC
    # ====================================
    elif hukum == "Hukum Gay-Lussac":

        st.subheader("Hukum Gay-Lussac")
        st.latex(r"\frac{P_1}{T_1} = \frac{P_2}{T_2}")

        P1 = st.number_input("P1 ", value=1.0)
        T1 = st.number_input("T1 ", value=273.0)
        T2 = st.number_input("T2 ", value=300.0)

        if st.button("Hitung P2"):
            P2 = (P1 * T2) / T1
            st.success(f"P2 = {P2:.3f}")

    # ====================================
    # HUKUM AVOGADRO
    # ====================================
    elif hukum == "Hukum Avogadro":

        st.subheader("Hukum Avogadro")
        st.latex(r"\frac{V_1}{n_1} = \frac{V_2}{n_2}")

        V1 = st.number_input("V1  ", value=1.0)
        n1 = st.number_input("n1", value=1.0)
        n2 = st.number_input("n2", value=2.0)

        if st.button("Hitung V2  "):
            V2 = (V1 * n2) / n1
            st.success(f"V2 = {V2:.3f}")

    # ====================================
    # PERSAMAAN GAS IDEAL
    # ====================================
    elif hukum == "Persamaan Gas Ideal":

        st.subheader("Persamaan Gas Ideal")
        st.latex(r"PV = nRT")

        P = st.number_input("Tekanan (atm)", value=1.0)
        V = st.number_input("Volume (L)", value=1.0)
        n = st.number_input("Mol (n)", value=1.0)

        R = 0.0821

        if st.button("Hitung Suhu"):
            T = (P * V) / (n * R)
            st.success(f"Suhu = {T:.2f} K")

# =========================
# ANIMASI STUDI KASUS
# =========================
elif menu == "🎬 Animasi Studi Kasus":

    st.header("🎬 Animasi Studi Kasus Gas Ideal")

    st.write("""
    ### Kasus:

    Sebuah gas berada dalam tabung:

    - Tekanan = 1 atm
    - Volume = 5 L
    - Mol = 1 mol

    Berapa suhu gas?
    """)

    st.latex(r"PV = nRT")

    P = 1
    V = 5
    n = 1
    R = 0.0821

    T = (P * V) / (n * R)

    progress = st.progress(0)

    for i in range(100):
        progress.progress(i + 1)

    st.success(f"Hasil suhu gas = {T:.2f} K")

    # ANIMASI TABUNG
    fig = go.Figure()

    fig.add_shape(
        type="rect",
        x0=0.4,
        y0=0,
        x1=0.6,
        y1=1,
        line=dict(width=3)
    )

    y = np.random.rand(50)
    x = np.random.uniform(0.42, 0.58, 50)

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode='markers',
            marker=dict(size=10)
        )
    )

    fig.update_layout(
        title="Animasi Partikel Gas",
        width=500,
        height=600
    )

    st.plotly_chart(fig)

# =========================
# GRAFIK
# =========================
elif menu == "📈 Grafik Hubungan Variabel":

    st.header("📈 Grafik Hubungan Variabel Gas")

    pilihan = st.selectbox(
        "Pilih Grafik",
        [
            "Tekanan vs Volume",
            "Volume vs Suhu",
            "Tekanan vs Suhu"
        ]
    )

    # ====================================
    # P vs V
    # ====================================
    if pilihan == "Tekanan vs Volume":

        V = np.linspace(1, 10, 100)
        P = 10 / V

        fig, ax = plt.subplots()

        ax.plot(V, P)

        ax.set_xlabel("Volume")
        ax.set_ylabel("Tekanan")
        ax.set_title("Grafik Boyle")

        st.pyplot(fig)

    # ====================================
    # V vs T
    # ====================================
    elif pilihan == "Volume vs Suhu":

        T = np.linspace(200, 500, 100)
        V = T / 100

        fig, ax = plt.subplots()

        ax.plot(T, V)

        ax.set_xlabel("Suhu (K)")
        ax.set_ylabel("Volume")

        ax.set_title("Grafik Charles")

        st.pyplot(fig)

    # ====================================
    # P vs T
    # ====================================
    elif pilihan == "Tekanan vs Suhu":

        T = np.linspace(200, 500, 100)
        P = T / 100

        fig, ax = plt.subplots()

        ax.plot(T, P)

        ax.set_xlabel("Suhu (K)")
        ax.set_ylabel("Tekanan")

        ax.set_title("Grafik Gay-Lussac")

        st.pyplot(fig)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Dibuat dengan Streamlit 🚀")
