import streamlit as s

s.title("Aplikasi Perhitungan Normalitas, Kadar, dan %RPD pada Titrasi")

s.header("Perhitungan Konsentrasi Normalitas")

def try_float(val):
    try:
        return float(val)
    except:
        return None

# Ambil input sebagai string
bobot_titrat_str = s.text_input("Bobot Titrat (mg)")
faktor_pengali_str = s.text_input("Faktor pengali")
volume_titran_str = s.text_input("Volume titran (mL)")
be_str = s.text_input("BE/BM")

# Konversi string ke float (jika bisa)
bobot_titrat = try_float(bobot_titrat_str)
faktor_pengali = try_float(faktor_pengali_str)
volume_titran = try_float(volume_titran_str)
be = try_float(be_str)

# Hitung jika valid
if all(val is not None for val in [bobot_titrat, faktor_pengali, volume_titran, be]) and volume_titran != 0 and be != 0:
    hasil = bobot_titrat / (max(faktor_pengali, 1) * volume_titran * be)
    s.success(f"Hasil Konsentrasi: {hasil} N")
else:
    s.info("⚠ Masukkan semua nilai dengan benar untuk menghitung normalitas.")
