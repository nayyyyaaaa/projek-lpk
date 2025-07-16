import streamlit as s

def N(bobot_titrat, faktor_pengali, volume_titran, BE):
    hasil = bobot_titrat / (faktor_pengali * volume_titran * BE)
    return hasil

bobot_titrat_mg = s.number_input("Bobot Titrat (mg)", key="bobot_titrat")
faktor_pengali = s.number_input("Faktor pengali", key="faktor_pengali")
volume_titran = s.number_input("Volume titran", key="volume_titran")
bobot_molekul_titrat = s.number_input("BE", key="BE")

# Hitung N dan tampilkan
hasil = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
hasil = round(hasil, 4)
s.write("Hasil N:", hasil)

# Input untuk perhitungan kadar
volume_titran_kadar = s.number_input("Volume titran (kadar)", key="vol_titran_kadar")
konsentrasi_titran_mL_kadar = hasil  # Menggunakan nilai 'hasil' di atas
bobot_molekul_titrat_kadar = s.number_input("BE (kadar)", key="BE_kadar")
faktor_pengali_kadar = s.number_input("Faktor pengali (kadar)", key="faktor_pengali_kadar")
volume_titrat_kadar = s.number_input("Volume titrat (kadar)", key="vol_titrat_kadar")

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    hasil = (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * faktor_pengali_kadar) / volume_titrat
    return hasil

# Hanya hitung dan tampilkan hasil2 jika semua variabel setelah BE tidak nol
if (
    volume_titran_kadar != 0 and
    konsentrasi_titran_mL_kadar != 0 and
    bobot_molekul_titrat_kadar != 0 and
    faktor_pengali_kadar != 0 and
    volume_titrat_kadar != 0
):
    hasil2 = kadar(
        volume_titran_kadar,
        konsentrasi_titran_mL_kadar,
        bobot_molekul_titrat_kadar,
        faktor_pengali_kadar,
        volume_titrat_kadar
    )
    hasil2 = round(hasil2, 2)
    s.write("Hasil Kadar:", hasil2)
