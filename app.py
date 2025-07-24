import streamlit as s

s.title("Aplikasi Perhitungan Normalitas, Kadar, dan %RPD pada Titrasi")

# ----------------------------
# Fungsi Perhitungan
# ----------------------------

def N(bobot_titrat_mg, faktor_pengali, volume_titran, BE):
    return bobot_titrat_mg / (max(faktor_pengali, 1) * volume_titran * BE)

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    return (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * max(faktor_pengali_kadar, 1)) / volume_titrat

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

bobot_titrat_mg = s.number_input("Bobot Titrat (mg)", value=None, placeholder="Masukkan angka", key="bobot_titrat_mg")
faktor_pengali = s.number_input("Faktor pengali", value=None, step=1, placeholder="Masukkan angka", key="faktor_pengali")
volume_titran = s.number_input("Volume titran (mL)", value=None, placeholder="Masukkan angka", key="volume_titran")
bobot_molekul_titrat = s.number_input("BE/BM", value=None, placeholder="Masukkan angka", key="BE")

if (
    bobot_titrat_mg is not None and volume_titran is not None and
    bobot_molekul_titrat is not None and faktor_pengali is not None and
    volume_titran != 0 and bobot_molekul_titrat != 0
):
    hasil = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
    s.success(f"Hasil Konsentrasi: {format(hasil, '.4f')} N")
else:
    s.info("⚠ Mohon isi Bobot Titrat, Volume Titran, dan BE/BM untuk menghitung Konsentrasi.")

# ----------------------------
# PERHITUNGAN KADAR
# ----------------------------
s.header("Perhitungan Kadar")

konsentrasi_input = s.number_input("Konsentrasi (N)", value=None, placeholder="Masukkan angka", key="kons_n_manual")
volume_titran_kadar = s.number_input("Volume titran (mL)", value=None, placeholder="Masukkan angka", key="vol_titran_kadar")
bobot_molekul_titrat_kadar = s.number_input("BE/BM", value=None, placeholder="Masukkan angka", key="BE_kadar")
faktor_pengali_kadar = s.number_input("Faktor pengali", value=None, step=1, placeholder="Masukkan angka", key="faktor_pengali_kadar")
volume_titrat_kadar = s.number_input("Volume titrat (mL)", value=None, placeholder="Masukkan angka", key="vol_titrat_kadar")

if (
    konsentrasi_input is not None and volume_titran_kadar is not None and
    bobot_molekul_titrat_kadar is not None and volume_titrat_kadar is not None and
    volume_titrat_kadar != 0
):
    hasil2 = kadar(
        volume_titran_kadar,
        konsentrasi_input,
        bobot_molekul_titrat_kadar,
        faktor_pengali_kadar or 1,
        volume_titrat_kadar
    )
    s.success(f"Hasil Kadar: {format(hasil2, '.2f')} %")
else:
    s.info("⚠ Mohon isi semua kolom dengan benar untuk menghitung Kadar.")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = s.number_input("Konsentrasi/Kadar 1", value=None, placeholder="Masukkan angka", key="kons1")
konsentrasi2 = s.number_input("Konsentrasi/Kadar 2", value=None, placeholder="Masukkan angka", key="kons2")

if konsentrasi1 is not None and konsentrasi2 is not None:
    rpd, rata_rata, satuan = hitung_rpd(konsentrasi1, konsentrasi2)
    s.success(f"Rata-rata: {format(rata_rata, '.2f') if satuan == '%' else format(rata_rata, '.4f')} {satuan}")
    s.success(f"%RPD: {rpd:.2f} %")
else:
    s.info("⚠ Isi Konsentrasi/Kadar 1 dan 2 untuk menghitung %RPD.")
