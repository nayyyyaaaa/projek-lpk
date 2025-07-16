import streamlit as s

def N(bobot_titrat, faktor_pengali, volume_titran, BE):
    """
    Menghitung normalitas (N).
    """
    return bobot_titrat / (faktor_pengali * volume_titran * BE)

# Input untuk Normalitas
bobot_titrat_mg = s.number_input("Bobot Titrat (mg)", key="bt")
faktor_pengali = s.number_input("faktor pengali", key="fp")
volume_titran = s.number_input("volume titran", key="vt")
bobot_molekul_titrat = s.number_input("BE", key="be")

# Hitung dan tampilkan Normalitas
hasil_N = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
hasil_N = round(hasil_N, 4)
s.write(f"Normalitas (N): {hasil_N}")


def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    """
    Menghitung kadar zat.
    """
    return (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * faktor_pengali_kadar) / volume_titrat

# Input untuk Kadar
volume_titran_kadar = s.number_input("volume titran", key="vt_k")
konsentrasi_titran_mL_kadar = s.number_input("kosentrasi titrat", key="kt_k")
bobot_molekul_titrat_kadar = s.number_input("BE", key="be_k")
faktor_pengali_kadar = s.number_input("faktor pengali", key="fp_k")
volume_titrat_kadar = s.number_input("volume titrat", key="vtat_k")

# Hitung dan tampilkan Kadar
hasil_kadar = kadar(
    volume_titran_kadar,
    konsentrasi_titran_mL_kadar,
    bobot_molekul_titrat_kadar,
    faktor_pengali_kadar,
    volume_titrat_kadar
)
hasil_kadar = round(hasil_kadar, 2)
s.write(f"Kadar: {hasil_kadar}")
