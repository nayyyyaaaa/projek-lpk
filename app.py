import streamlit as s

s.title("Aplikasi Perhitungan Titrasi")

# ----------------------------
# Fungsi Perhitungan
# ----------------------------

def N(bobot_titrat_mg, faktor_pengali, volume_titran, BE):
    if volume_titran != 0 and BE != 0:
        return bobot_titrat_mg / (max(faktor_pengali, 1) * volume_titran * BE)
    return 0.0

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    if volume_titrat != 0:
        return (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * max(faktor_pengali_kadar, 1)) / volume_titrat
    return 0.0

def hitung_rpd(c1, c2):
    rata2 = (c1 + c2) / 2
    rpd = abs(c1 - c2) / rata2 * 100
    return round(rpd, 2), round(rata2, 4)

# ----------------------------
# PERHITUNGAN KONSENTRASI
# ----------------------------
s.header("Perhitungan Konsentrasi")

bobot_titrat_mg = s.number_input("Bobot Titrat (mg)", format="%.4f", key="bobot_titrat_mg")
faktor_pengali = s.number_input("Faktor pengali", step=1, format="%d", key="faktor_pengali")
volume_titran = s.number_input("Volume titran", format="%.4f", key="volume_titran")
bobot_molekul_titrat = s.number_input("BE", format="%.4f", key="BE")

hasil = 0.0
if bobot_titrat_mg != 0 and volume_titran != 0 and bobot_molekul_titrat != 0:
    hasil = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
    hasil = round(hasil, 4)
    s.success(f"Hasil Konsentrasi: {hasil} N")
else:
    s.info("⚠ Mohon isi Bobot Titrat, Volume Titran, dan BE untuk menghitung Konsentrasi.")

# ----------------------------
# PERHITUNGAN KADAR
# ----------------------------
s.header("Perhitungan Kadar")

konsentrasi_input = s.number_input("Konsentrasi (N)", format="%.4f", key="kons_n_manual")
volume_titran_kadar = s.number_input("Volume titran (kadar)", format="%.4f", key="vol_titran_kadar")
bobot_molekul_titrat_kadar = s.number_input("BE (kadar)", format="%.4f", key="BE_kadar")
faktor_pengali_kadar = s.number_input("Faktor pengali (kadar)", step=1, format="%d", key="faktor_pengali_kadar")
volume_titrat_kadar = s.number_input("Volume titrat (kadar)", format="%.4f", key="vol_titrat_kadar")

hasil2 = 0.0
if (
    konsentrasi_input != 0 and volume_titran_kadar != 0 and
    bobot_molekul_titrat_kadar != 0 and volume_titrat_kadar != 0
):
    hasil2 = kadar(
        volume_titran_kadar,
        konsentrasi_input,
        bobot_molekul_titrat_kadar,
        faktor_pengali_kadar,
        volume_titrat_kadar
    )
    hasil2 = round(hasil2, 2)
    s.success(f"Hasil Kadar: {hasil2} %")
else:
    s.info("⚠ Mohon isi Konsentrasi, Volume Titran, BE, dan Volume Titrat untuk menghitung Kadar.")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = s.number_input("Konsentrasi/Kadar 1", format="%.4f", key="kons1")
konsentrasi2 = s.number_input("Konsentrasi/Kadar 2", format="%.4f", key="kons2")

if konsentrasi1 and konsentrasi2:
    rpd, rata_rata = hitung_rpd(konsentrasi1, konsentrasi2)
    s.success(f"Rata-rata Konsentrasi: {rata_rata} N")
    s.success(f"%RPD: {rpd} %")
else:
    s.info("⚠ Isi Konsentrasi/Kadar 1 dan 2 untuk menghitung %RPD.")

# Tambahkan CSS untuk styling pink peach
s.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background-color: #FFF0F5;
        color: #4A4A4A;
    }

    h1, h2, h3 {
        color: #d63384;
        font-weight: 700;
    }

    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background-color: #ffe4e1;
        border: 1px solid #ffb6c1;
        border-radius: 10px;
        padding: 10px;
    }

    .stNumberInput label,
    .stTextInput label {
        font-size: 16px;
        color: #b03060;
    }

    .stSuccess {
        background-color: #ffc0cb30;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #ffb6c1;
        color: #b03060;
    }

    .stInfo {
        background-color: #fce4ec;
        padding: 1rem;
        border-radius: 10px;
        border: 1px dashed #f8bbd0;
        color: #a64d79;
    }

    .stApp {
        background-image: linear-gradient(to bottom right, #fff0f5, #ffe4e1);
    }

    </style>
""", unsafe_allow_html=True)

# Tambahkan Google Font 'Poppins' atau yang kamu suka
s.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)
