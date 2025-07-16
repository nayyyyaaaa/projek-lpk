import streamlit as s

s.title("Aplikasi Perhitungan Titrasi")

# Fungsi Konsentrasi
def N(bobot_titrat, faktor_pengali, volume_titran, BE):
    hasil = bobot_titrat / (faktor_pengali * volume_titran * BE)
    return hasil

# ----------------------------
# Perhitungan Konsentrasi
# ----------------------------
s.header("Perhitungan Konsentrasi")

bobot_titrat_mg = s.number_input("Bobot Titrat (mg)", format="%.4f", key="bobot_titrat")
faktor_pengali = s.number_input("Faktor pengali", format="%.4f", key="faktor_pengali")
volume_titran = s.number_input("Volume titran", format="%.4f", key="volume_titran")
bobot_molekul_titrat = s.number_input("BE", format="%.4f", key="BE")

hasil = 0
if faktor_pengali != 0 and volume_titran != 0 and bobot_molekul_titrat != 0:
    hasil = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
    s.success(f"Hasil Konsentrasi: {round(hasil, 4)}")

# ----------------------------
# Perhitungan Kadar
# ----------------------------
s.header("Perhitungan Kadar")

volume_titran_kadar = s.number_input("Volume titran (kadar)", format="%.4f", key="vol_titran_kadar")
bobot_molekul_titrat_kadar = s.number_input("BE (kadar)", format="%.4f", key="BE_kadar")
faktor_pengali_kadar = s.number_input("Faktor pengali (kadar)", format="%.4f", key="faktor_pengali_kadar")
volume_titrat_kadar = s.number_input("Volume titrat (kadar)", format="%.4f", key="vol_titrat_kadar")

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    hasil = (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * faktor_pengali_kadar) / volume_titrat
    return hasil

if (
    volume_titran_kadar != 0 and
    hasil != 0 and
    bobot_molekul_titrat_kadar != 0 and
    faktor_pengali_kadar != 0 and
    volume_titrat_kadar != 0
):
    hasil2 = kadar(
        volume_titran_kadar,
        hasil,  # hasil dari perhitungan konsentrasi
        bobot_molekul_titrat_kadar,
        faktor_pengali_kadar,
        volume_titrat_kadar
    )
    s.success(f"Hasil Kadar: {round(hasil2, 2)}")
