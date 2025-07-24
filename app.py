import streamlit as s

s.title("Aplikasi Perhitungan Normalitas, Kadar, dan %RPD pada Titrasi")

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

    # Deteksi jumlah angka di belakang koma
    decimal_places_1 = len(str(c1).split(".")[-1])
    decimal_places_2 = len(str(c2).split(".")[-1])
    desimal = max(decimal_places_1, decimal_places_2)

    if desimal <= 2:
        satuan = "%"
        return round(rpd, 2), round(rata2, 2), satuan
    else:
        satuan = "N"
        return round(rpd, 2), round(rata2, 4), satuan

# ----------------------------
# PERHITUNGAN KONSENTRASI
# ----------------------------
s.header("Perhitungan Konsentrasi Normalitas")

bobot_titrat_mg = s.number_input("Bobot Titrat (mg)", key="bobot_titrat_mg")
faktor_pengali = s.number_input("Faktor pengali", step=1, key="faktor_pengali")
volume_titran = s.number_input("Volume titran (mL)", key="volume_titran")
bobot_molekul_titrat = s.number_input("BE/BM", key="BE")

hasil = 0.0
if bobot_titrat_mg and volume_titran and bobot_molekul_titrat:
    hasil = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
    hasil = round(hasil, 4)
    s.success(f"Hasil Konsentrasi: {hasil} N")
else:
    s.info("⚠ Mohon isi Bobot Titrat, Volume Titran, dan BE/BM untuk menghitung Konsentrasi.")

# ----------------------------
# PERHITUNGAN KADAR
# ----------------------------
s.header("Perhitungan Kadar")

konsentrasi_input = s.number_input("Konsentrasi (N)", key="kons_n_manual")
volume_titran_kadar = s.number_input("Volume titran (mL)", key="vol_titran_kadar")
bobot_molekul_titrat_kadar = s.number_input("BE/BM", key="BE_kadar")
faktor_pengali_kadar = s.number_input("Faktor pengali", step=1, key="faktor_pengali_kadar")
volume_titrat_kadar = s.number_input("Volume titrat (mL)", key="vol_titrat_kadar")

hasil2 = 0.0
if (
    konsentrasi_input and volume_titran_kadar and
    bobot_molekul_titrat_kadar and volume_titrat_kadar
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
    s.info("⚠ Mohon isi Konsentrasi, Volume Titran, BE/BM, dan Volume Titrat untuk menghitung Kadar.")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = s.number_input("Konsentrasi/Kadar 1", key="kons1")
konsentrasi2 = s.number_input("Konsentrasi/Kadar 2", key="kons2")

if konsentrasi1 and konsentrasi2:
    rpd, rata_rata, satuan = hitung_rpd(konsentrasi1, konsentrasi2)
    s.success(f"Rata-rata: {rata_rata} {satuan}")
    s.success(f"%RPD: {rpd} %")
else:
    s.info("⚠ Isi Konsentrasi/Kadar 1 dan 2 untuk menghitung %RPD.")
