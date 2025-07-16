import streamlit as st

def hitung_konsentrasi_titrat(volume_titran_ml: float,
                              molaritas_titran: float,
                              volume_titrat_ml: float,
                              rasio_mol_titran: int = 1,
                              rasio_mol_titrat: int = 1) -> float:
    """
    Menghitung konsentrasi titrat berdasarkan data titrasi.

    Parameters:
    - volume_titran_ml: Volume titran (mL)
    - molaritas_titran: Konsentrasi titran (mol/L)
    - volume_titrat_ml: Volume titrat (mL)
    - rasio_mol_titran: Rasio mol titran dalam reaksi stoikiometri
    - rasio_mol_titrat: Rasio mol titrat dalam reaksi stoikiometri

    Returns:
    - molaritas_titrat: Konsentrasi titrat (mol/L)
    """
    # Konversi mL ke L
    V1 = volume_titran_ml / 1000  # Titran (buret)
    V2 = volume_titrat_ml / 1000  # Titrat (erlenmeyer)

    # Hitung mol titran
    mol_titran = molaritas_titran * V1

    # Stoikiometri: mol titrat
    mol_titrat = mol_titran * (rasio_mol_titrat / rasio_mol_titran)

    # Molaritas titrat
    return mol_titrat / V2

# ---------------- Streamlit App ----------------
st.set_page_config(
    page_title="Kalkulator Konsentrasi Titrat",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🔬 Kalkulator Konsentrasi Titrat")
st.write(
    "Aplikasi web untuk menghitung konsentrasi larutan titrat berdasarkan data titrasi. "
    "Masukkan volume dan molaritas titran, serta volume titrat, lalu klik 'Hitung'"
)

# Sidebar untuk input
with st.sidebar:
    st.header("📥 Input Data")
    V_titran = st.number_input(
        label="Volume Titran (mL)",
        min_value=0.0,
        format="%.2f",
        help="Masukkan volume titran dalam mililiter"
    )
    M_titran = st.number_input(
        label="Molaritas Titran (mol/L)",
        min_value=0.0,
        format="%.4f",
        help="Masukkan konsentrasi titran dalam mol per liter"
    )
    V_titrat = st.number_input(
        label="Volume Titrat (mL)",
        min_value=0.0,
        format="%.2f",
        help="Masukkan volume titrat dalam mililiter"
    )
    st.markdown("---")
    rasio_titran = st.selectbox(
        "Rasio mol Titran:",
        options=[1, 2, 3, 4],
        index=0,
        help="Rasio stoikiometri mol titran"
    )
    rasio_titrat = st.selectbox(
        "Rasio mol Titrat:",
        options=[1, 2, 3, 4],
        index=0,
        help="Rasio stoikiometri mol titrat"
    )

# Tombol untuk memulai perhitungan
if st.button("Hitung Konsentrasi"):
    if V_titran <= 0 or M_titran <= 0 or V_titrat <= 0:
        st.error("Semua input harus lebih besar dari nol!")
    else:
        M_titrat = hitung_konsentrasi_titrat(
            V_titran,
            M_titran,
            V_titrat,
            rasio_mol_titran=rasio_titran,
            rasio_mol_titrat=rasio_titrat
        )
        st.success(f"Konsentrasi titrat: **{M_titrat:.4f} mol/L**")
        st.balloons()  # Optional celebration effect
