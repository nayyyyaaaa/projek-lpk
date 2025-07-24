import streamlit as s

s.title("Aplikasi Perhitungan Normalitas, Kadar, dan %RPD pada Titrasi")

# ----------------------------
# Fungsi Helper
# ----------------------------
def try_float(val):
    try:
        return float(val)
    except:
        return None

def N(bobot_titrat_mg, faktor_pengali, volume_titran, BE):
    return bobot_titrat_mg / (faktor_pengali * volume_titran * BE)

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    return (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * faktor_pengali_kadar) / volume_titrat

def hitung_rpd(c1, c2):
    rata2 = (c1 + c2) / 2
    rpd = abs(c1 - c2) / rata2 * 100

    decimal_places_1 = len(str(c1).split(".")[-1]) if "." in str(c1) else 0
    decimal_places_2 = len(str(c2).split(".")[-1]) if "." in str(c2) else 0
    desimal = max(decimal_places_1, decimal_places_2)

    satuan = "%" if desimal <= 2 else "N"
    return round(rpd, 2), rata2, satuan

# ----------------------------
# PERHITUNGAN NORMALITAS
# ----------------------------
s.header("Perhitungan Konsentrasi Normalitas")

bobot_titrat = try_float(s.text_input("Bobot Titrat (mg)", key="bt"))
volume_titran = try_float(s.text_input("Volume Titran (mL)", key="vt1"))
faktor_pengali = try_float(s.text_input("Faktor Pengali", key="fp1") or "1")
be = try_float(s.text_input("BE / BM", key="be"))

if any(val is not None for val in [bobot_titrat, volume_titran, faktor_pengali, be]):
    if None in [bobot_titrat, volume_titran, faktor_pengali, be]:
        s.warning("⚠ Harap isi semua input untuk menghitung normalitas.")
    elif volume_titran == 0 or be == 0:
        s.error("❌ Volume titran dan BE tidak boleh nol.")
    else:
        hasil = N(bobot_titrat, faktor_pengali, volume_titran, be)
        s.success(f"Hasil Konsentrasi: {hasil:.4f} N")

# ----------------------------
# PERHITUNGAN KADAR
# ----------------------------
s.header("Perhitungan Kadar")

konsentrasi_input = try_float(s.text_input("Konsentrasi Titran (N)", key="kon"))
volume_titran_kadar = try_float(s.text_input("Volume Titran (mL)", key="vt2"))
faktor_pengali_kadar = try_float(s.text_input("Faktor Pengali", key="fp2") or "1")
be_kadar = try_float(s.text_input("BE / BM", key="bekadar"))
volume_titrat_kadar = try_float(s.text_input("Volume Titrat (mL)", key="vt3"))

if any(val is not None for val in [konsentrasi_input, volume_titran_kadar, faktor_pengali_kadar, be_kadar, volume_titrat_kadar]):
    if None in [konsentrasi_input, volume_titran_kadar, faktor_pengali_kadar, be_kadar, volume_titrat_kadar]:
        s.warning("⚠ Harap isi semua input untuk menghitung kadar.")
    elif volume_titrat_kadar == 0:
        s.error("❌ Volume titrat tidak boleh nol.")
    else:
        hasil_kadar = kadar(volume_titran_kadar, konsentrasi_input, be_kadar, faktor_pengali_kadar, volume_titrat_kadar)
        s.success(f"Hasil Kadar: {hasil_kadar:.2f} %")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = try_float(s.text_input("Konsentrasi/Kadar 1", key="r1"))
konsentrasi2 = try_float(s.text_input("Konsentrasi/Kadar 2", key="r2"))

if konsentrasi1 is not None or konsentrasi2 is not None:
    if konsentrasi1 is None or konsentrasi2 is None:
        s.warning("⚠ Harap isi kedua nilai konsentrasi/kadar untuk menghitung %RPD.")
    elif konsentrasi1 == 0 or konsentrasi2 == 0:
        s.error("❌ Nilai tidak boleh nol.")
    else:
        rpd, rata_rata, satuan = hitung_rpd(konsentrasi1, konsentrasi2)
        s.success(f"Rata-rata: {rata_rata:.2f} {satuan}")
        s.success(f"%RPD: {rpd:.2f} %")
    
