import streamlit as s

# ----------------------------
# Fungsi perhitungan konsentrasi/kadar
# ----------------------------
def hitung_kadar(volume_titran, normalitas, berat_sample):
    try:
        volume = float(volume_titran.replace(",", "."))
        normal = float(normalitas.replace(",", "."))
        berat = float(berat_sample.replace(",", "."))
        hasil = (volume * normal * 0.1) / berat
        return hasil
    except:
        return None

# ----------------------------
# Fungsi perhitungan %RPD
# ----------------------------
def hitung_rpd(k1, k2):
    rata2 = (k1 + k2) / 2
    rpd = abs(k1 - k2) / rata2 * 100

    # Penentuan satuan otomatis
    satuan = "%"
    desimal = 2
    if rata2 < 1:
        satuan = "N"  # Normalitas
        desimal = 4

    return rpd, rata2, satuan, desimal

# ----------------------------
# Tampilan judul utama
# ----------------------------
s.title("Perhitungan Konsentrasi dan %RPD")

# ----------------------------
# PERHITUNGAN KONSENTRASI / KADAR
# ----------------------------
s.header("Perhitungan Konsentrasi / Kadar")

volume_titran = s.text_input("Volume titran (mL)")
normalitas = s.text_input("Normalitas titran (N)")
berat_sample = s.text_input("Berat sampel (gram)")

hasil_kadar = hitung_kadar(volume_titran, normalitas, berat_sample)

if hasil_kadar is not None:
    s.success(f"Hasil perhitungan konsentrasi/kadar: {hasil_kadar:.4f} %")
elif volume_titran or normalitas or berat_sample:
    s.warning("⚠ Harap isi semua data dengan format angka yang benar.")

# ----------------------------
# PERHITUNGAN %RPD
# ----------------------------
s.header("Perhitungan %RPD")

konsentrasi1 = s.text_input("Konsentrasi/Kadar 1", key="kons1")
konsentrasi2 = s.text_input("Konsentrasi/Kadar 2", key="kons2")

try:
    # Terima koma atau titik
    k1 = float(konsentrasi1.replace(",", "."))
    k2 = float(konsentrasi2.replace(",", "."))

    rpd, rata2, satuan, desimal = hitung_rpd(k1, k2)

    if satuan == "%":
        s.success(f"Rata-rata Konsentrasi: {format(rata2, '.2f')} %")
    else:
        s.success(f"Rata-rata Konsentrasi: {format(rata2, '.4f')} N")

    s.success(f"%RPD: {rpd:.2f} %")

except:
    if konsentrasi1 or konsentrasi2:
        s.info("⚠ Harap isi kedua nilai Konsentrasi/Kadar dengan benar untuk menghitung %RPD.")
