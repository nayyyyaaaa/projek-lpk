import streamlit as s

s.title("Aplikasi Perhitungan Titrasi")

def N(bobot_titrat_gram, faktor_pengali, volume_titran, BE):
    return bobot_titrat_gram / (faktor_pengali * volume_titran * BE)

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    return (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * faktor_pengali_kadar) / volume_titrat

def hitung_rpd(c1, c2):
    rata2 = (c1 + c2) / 2
    rpd = abs(c1 - c2) / rata2 * 100
    return round(rpd, 2), round(rata2, 4)

# ----------------------------
# PERHITUNGAN KONSENTRASI
# ----------------------------
s.header("Perhitungan Konsentrasi")

bobot_titrat_gram = s.number_input("Bobot Titrat (gram)", format="%.4f", key="bobot_titrat_gram")
faktor_pengali = s.number_input("Faktor pengali", step=1, format="%d", key="faktor_pengali")
volume_titran = s.number_input("Volume titran", format="%.4f", key="volume_titran")
bobot_molekul_titrat = s.number_input("BE", format="%.4f", key="BE")

hasil = 0.0
if all([bobot_titrat_gram, faktor_pengali, volume_titran, bobot_molekul_titrat]):
    hasil = N(bobot_titrat_gram, faktor_pengali, volume_titran, bobot_molekul_titrat)
    hasil = round(hasil, 4)
    s.success(f"Hasil Konsentrasi: {hasil} N")
else:
    s.info("⚠ Isi semua input di bagian konsentrasi agar hasil muncul.")

# ----------------------------
# PERHITUNGAN KADAR
# ----------------------------
s.header("Perhitungan Kadar")

volume_titran_kadar = s.number_input("Volume titran (kadar)", format="%.4f", key="vol_titran_kadar")
bobot_molekul_titrat_kadar = s.number_input("BE (kadar)", format="%.4f", key="BE_kadar")
faktor_pengali_kadar = s.number_input("Faktor pengali (kadar)", step=1, format="%d", key="faktor_pengali_kadar")
volume_titrat_kadar = s.number_input("Volume titrat (kadar)", format="%.4f", key="vol_titrat_kadar")

if all([volume_titran_kadar, hasil, bobot_molekul_titrat_kadar, faktor_pengali_kadar, volume_titrat_kadar]):
    hasil2 = kadar(volume_titran_kadar, hasil, bobot_molekul_titrat_kadar, faktor_pengali_kadar, volume_titrat_kadar)
    hasil2 = round(hasil2, 2)
    s.success(f"Hasil Kadar: {hasil2} %")
else:
    s.info("⚠ Isi semua input di bagian kadar agar hasil muncul.")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = s.number_input("Konsentrasi 1", format="%.4f", key="kons1")
konsentrasi2 = s.number_input("Konsentrasi 2", format="%.4f", key="kons2")

if konsentrasi1 and konsentrasi2:
    rpd, rata_rata = hitung_rpd(konsentrasi1, konsentrasi2)
    s.success(f"Rata-rata Konsentrasi: {rata_rata} N")
    s.success(f"%RPD: {rpd} %")
else:
    s.info("⚠ Isi Konsentrasi 1 dan 2 untuk menghitung %RPD.")
