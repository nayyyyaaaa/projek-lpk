import streamlit as s

s.title("Aplikasi Perhitungan Konsentrasi Normalitas, %Kadar, dan %RPD pada Titrasi")

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

    decimal_places_1 = len(str(c1).split(".")[-1]) if "." in str(c1) else 0
    decimal_places_2 = len(str(c2).split(".")[-1]) if "." in str(c2) else 0
    max_decimal = max(decimal_places_1, decimal_places_2)

    satuan = "%" if max_decimal <= 2 else "N"
    return round(rpd, 2), round(rata2, max_decimal), satuan, max_decimal

# ----------------------------
# PERHITUNGAN KONSENTRASI
# ----------------------------
s.header("Perhitungan Konsentrasi Normalitas")

bobot_titrat_mg = s.text_input("Bobot Titrat (mg)", key="bobot_titrat_mg")
faktor_pengali = s.text_input("Faktor pengali", key="faktor_pengali")
volume_titran = s.text_input("Volume titran (mL)", key="volume_titran")
bobot_molekul_titrat = s.text_input("BE/BM", key="BE")

try:
     # Ganti koma ke titik agar bisa dibaca sebagai sebagai float
    bt = float(bobot_titrat_mg.replace(",","."))
    fp = float(faktor_pengali.replace(",",".")) if faktor_pengali else 1
    vt = float(volume_titran.replace(",","."))
    be = float(bobot_molekul_titrat.replace(",","."))

    if vt != 0 and be != 0:
        hasil = N(bt, fp, vt, be)
        s.success(f"Hasil Konsentrasi: {hasil:.4f} N")
except:
    if bobot_titrat_mg or volume_titran or bobot_molekul_titrat:
        s.info("⚠ Mohon isi semua input dengan benar untuk menghitung Normalitas.")

# ----------------------------
# PERHITUNGAN KADAR
# ----------------------------
s.header("Perhitungan Kadar")

konsentrasi_input = s.text_input("Konsentrasi (N)", key="kons_n_manual")
volume_titran_kadar = s.text_input("Volume titran (mL)", key="vol_titran_kadar")
bobot_molekul_titrat_kadar = s.text_input("BE/BM", key="BE_kadar")
faktor_pengali_kadar = s.text_input("Faktor pengali", key="faktor_pengali_kadar")
volume_titrat_kadar = s.text_input("Volume titrat (mL)", key="vol_titrat_kadar")

try:
     # Ganti koma ke titik agar bisa dibaca sebagai sebagai float
    kon = float(konsentrasi_input.replace(",","."))
    vt_kadar = float(volume_titran_kadar.replace(",","."))
    be_kadar = float(bobot_molekul_titrat_kadar.replace(",","."))
    fp_kadar = float(faktor_pengali_kadar.replace(",",".")) if faktor_pengali_kadar else 1
    v_titrat = float(volume_titrat_kadar.replace(",","."))

    if kon != 0 and vt_kadar != 0 and be_kadar != 0 and v_titrat != 0:
        hasil2 = kadar(vt_kadar, kon, be_kadar, fp_kadar, v_titrat)
        s.success(f"Hasil Kadar: {hasil2:.2f} %")
except:
    if konsentrasi_input or volume_titran_kadar or bobot_molekul_titrat_kadar or volume_titrat_kadar:
        s.info("⚠ Mohon isi semua input dengan benar untuk menghitung Kadar.")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = s.text_input("Konsentrasi/Kadar 1", key="kons1")
konsentrasi2 = s.text_input("Konsentrasi/Kadar 2", key="kons2")

try:
    # Ganti koma ke titik agar bisa dibaca sebagai sebagai float
    k1 = float(konsentrasi1.replace(",","."))
    k2 = float(konsentrasi2.replace(",","."))

    rpd, rata2, satuan, desimal = hitung_rpd(k1, k2)

    if satuan == "%":
        s.success(f"Rata-rata Konsentrasi: {format(rata2, '.2f')} %")
    else:
        s.success(f"Rata-rata Konsentrasi: {format(rata2, '.4f')} N")

    s.success(f"%RPD: {rpd:.2f} %")
except:
    if konsentrasi1 or konsentrasi2:
        s.info("⚠ Harap isi kedua nilai Konsentrasi/Kadar dengan benar untuk menghitung %RPD.")
        
