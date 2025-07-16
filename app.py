import streamlit as s

s.title("Aplikasi Perhitungan Titrasi")

# ----------------------------
# Fungsi Perhitungan
# ----------------------------

def N(bobot_titrat_gram, faktor_pengali, volume_titran, BE):
    return bobot_titrat_gram / (faktor_pengali * volume_titran * BE)

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    return (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * faktor_pengali_kadar) / volume_titrat

def hitung_rpd(c1, c2):
    rata2 = (c1 + c2) / 2
    rpd = abs(c1 - c2) / rata2 * 100
    return round(rpd, 2), round(rata2, 4)

# ----------------------------
# Perhitungan Konsentrasi
# ----------------------------
s.header("Perhitungan Konsentrasi")

bobot_titrat_gram = s.number_input("Bobot Titrat (gram)", format="%.4f", key="bobot_titrat_gram")
faktor_pengali = s.number_input("Faktor pengali", step=1, format="%d", key="faktor_pengali")  # hanya bilangan bulat
volume_titran = s.number_input("Volume titran", format="%.4f", key="volume_titran")
bobot_molekul_titrat = s.number_input("BE", format="%.4f", key="BE")

hasil = 0.0
if faktor_pengali != 0 and volume_titran != 0 and bobot_molekul_titrat != 0:
    hasil = N(bobot_titrat_gram, faktor_pengali, volume_titran, bobot_molekul_titrat)
    hasil = round(hasil, 4)
    s.success(f"Hasil Konsentrasi: {hasil} N")

# ----------------------------
# Perhitungan Kadar
# ----------------------------
s.header("Perhitungan Kadar")

volume_titran_kadar = s.number_input("Volume titran (kadar)", format="%.4f", key="vol_titran_kadar")
bobot_molekul_titrat_kadar = s.number_input("BE (kadar)", format="%.4f", key="BE_kadar")
faktor_pengali_kadar = s.number_input("Faktor pengali (kadar)", step=1, format="%d", key="faktor_pengali_kadar")
volume_titrat_kadar = s.number_input("Volume titrat (kadar)", format="%.4f", key="vol_titrat_kadar")

hasil2 = 0.0
if (
    volume_titran_kadar != 0 and
    hasil != 0 and
    bobot_molekul_titrat_kadar != 0 and
    faktor_pengali_kadar != 0 and
    volume_titrat_kadar != 0
):
    hasil2 = kadar(
        volume_titran_kadar,
        hasil,
        bobot_molekul_titrat_kadar,
        faktor_pengali_kadar,
        volume_titrat_kadar
    )
    hasil2 = round(hasil2, 2)
    s.success(f"Hasil Kadar: {hasil2} %")

# ----------------------------
# Perhitungan %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = s.number_input("Konsentrasi 1", format="%.4f", key="kons1")
konsentrasi2 = s.number_input("Konsentrasi 2", format="%.4f", key="kons2")

if konsentrasi1 != 0 and konsentrasi2 != 0:
    rpd, rata_rata = hitung_rpd(konsentrasi1, konsentrasi2)
    s.success(f"Rata-rata Konsentrasi: {rata_rata} N")
    s.success(f"%RPD: {rpd} %")
