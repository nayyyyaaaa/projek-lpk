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
