import streamlit as s

s.title("Aplikasi Perhitungan Normalitas, Kadar, dan %RPD pada Titrasi")

# ----------------------------
# Fungsi Helper
# ----------------------------
def try_float(val):
    """Coba konversi string ke float, jika gagal kembalikan None."""
    try:
        return float(val)
    except:
        return None

def N(bobot_titrat_mg, faktor_pengali, volume_titran, BE):
    return bobot_titrat_mg / (max(faktor_pengali, 1) * volume_titran * BE)

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    return (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * max(faktor_pengali_kadar, 1)) / volume_titrat

def hitung_rpd(c1, c2):
    rata2 = (c1 + c2) / 2
    rpd = abs(c1 - c2) / rata2 * 100

    # Deteksi jumlah angka di belakang koma
    decimal_places_1 = len(str(c1).split(".")[-1]) if "." in str(c1) else 0
    decimal_places_2 = len(str(c2).split(".")[-1]) if "." in str(c2) else 0
    desimal = max(decimal_places_1, decimal_places_2)

    satuan = "%" if desimal <= 2 else "N"
    return round(rpd, 2), rata2, satuan, desimal

# ----------------------------
# PERHITUNGAN KONSENTRASI
# ----------------------------
s.header("Perhitungan Konsentrasi Normalitas")

bobot_titrat_str = s.text_input("Bobot Titrat (mg)")
faktor_pengali_str = s.text_input("Faktor pengali")
volume_titran_str = s.text_input("Volume titran (mL)")
be_str = s.text_input("BE/BM")

bobot_titrat = try_float(bobot_titrat_str)
faktor_pengali = try_float(faktor_pengali_str)
volume_titran = try_float(volume_titran_str)
be = try_float(be_str)

if all(val is not None for val in [bobot_titrat, faktor_pengali, volume_titran, be]) and volume_titran != 0 and be != 0:
    hasil = N(bobot_titrat, faktor_pengali, volume_titran, be)
    s.success(f"Hasil Konsentrasi: {format(hasil, '.4f')} N")
else:
    s.info("⚠ Masukkan semua nilai dengan benar untuk menghitung normalitas.")

# ----------------------------
# PERHITUNGAN KADAR
# ----------------------------
s.header("Perhitungan Kadar")

konsentrasi_input_str = s.text_input("Konsentrasi (N)")
volume_titran_kadar_str = s.text_input("Volume titran (mL)")
be_kadar_str = s.text_input("BE/BM")
faktor_pengali_kadar_str = s.text_input("Faktor pengali")
volume_titrat_kadar_str = s.text_input("Volume titrat (mL)")

konsentrasi_input = try_float(konsentrasi_input_str)
volume_titran_kadar = try_float(volume_titran_kadar_str)
be_kadar = try_float(be_kadar_str)
faktor_pengali_kadar = try_float(faktor_pengali_kadar_str)
volume_titrat_kadar = try_float(volume_titrat_kadar_str)

if all(val is not None for val in [konsentrasi_input, volume_titran_kadar, be_kadar, volume_titrat_kadar]) and volume_titrat_kadar != 0:
    hasil2 = kadar(volume_titran_kadar, konsentrasi_input, be_kadar, faktor_pengali_kadar or 1, volume_titrat_kadar)
    s.success(f"Hasil Kadar: {format(hasil2, '.2f')} %")
else:
    s.info("⚠ Masukkan semua nilai dengan benar untuk menghitung kadar.")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1_str = s.text_input("Konsentrasi/Kadar 1")
konsentrasi2_str = s.text_input("Konsentrasi/Kadar 2")

konsentrasi1 = try_float(konsentrasi1_str)
konsentrasi2 = try_float(konsentrasi2_str)

if konsentrasi1 is not None and konsentrasi2 is not None:
    rpd, rata_rata, satuan, desimal = hitung_rpd(konsentrasi1, konsentrasi2)
    if satuan == "%":
        s.success(f"Rata-rata: {format(rata_rata, '.2f')} %")
    else:
        s.success(f"Rata-rata: {format(rata_rata, '.4f')} N")
    s.success(f"%RPD: {rpd:.2f} %")
else:
    s.info("⚠ Isi Konsentrasi/Kadar 1 dan 2 untuk menghitung %RPD.")
