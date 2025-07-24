import streamlit as s

# CSS & Gaya Imut Kimia
s.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&family=Quicksand:wght@400;600&display=swap');

[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #fce4ec, #e1f5fe);
    font-family: 'Comic Neue', 'Quicksand', cursive;
    color: #6a1b9a;
    background-attachment: fixed;
}

.block-container {
    background-color: #ffffffdd;
    padding: 2rem;
    border-radius: 25px;
    box-shadow: 0 0 20px #f3d1f4;
    border: 2px dashed #f48fb1;
}

/* Judul utama */
.centered-title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #ec407a;
    margin-top: 1rem;
    text-shadow: 1px 1px 2px #f8bbd0;
}

/* Section kecil */
.cute-section-title {
    font-size: 20px;
    font-weight: 600;
    color: #7b1fa2;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    font-family: 'Comic Neue', cursive;
    background-color: #fce4ec;
    padding: 0.5rem 1rem;
    border-left: 5px solid #f48fb1;
    border-radius: 10px;
    box-shadow: 0 2px 4px #f8bbd07e;
}

/* Input */
.stTextInput > div > input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #fff5fa;
    color: #6a1b9a;
    border: 2px dashed #f48fb1;
    border-radius: 15px;
    font-family: 'Comic Neue', cursive;
    padding: 0.4rem;
}

/* Tombol */
.stButton button {
    background-color: #f48fb1;
    color: white;
    font-weight: bold;
    font-family: 'Quicksand', sans-serif;
    border-radius: 20px;
    padding: 0.5rem 1rem;
    box-shadow: 0 4px 8px rgba(255, 182, 193, 0.5);
    transition: all 0.3s ease;
}
.stButton button:hover {
    background-color: #ec407a;
}

/* Scrollbar pastel */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: #ffeef4;
}
::-webkit-scrollbar-thumb {
    background: #f8bbd0;
    border-radius: 10px;
}

/* Atom animasi */
.animated-atom {
    position: fixed;
    top: 15px;
    right: 15px;
    width: 100px;
    z-index: 9999;
    opacity: 0.9;
}

/* Footer */
.footer-text {
    font-family: 'Comic Neue', cursive;
    font-size: 0.9rem;
    color: #ba68c8;
    font-style: italic;
    line-height: 1.4;
    margin-top: 1.5rem;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: #fde0e0 !important;
    color: #4a148c !important;
}

</style>
""", unsafe_allow_html=True)
</style>

<!-- Icon lucu -->
<img src="https://media.tenor.com/Z7Z-HChjbnEAAAAi/science-love.gif" class="animated-atom">
""", unsafe_allow_html=True)

# Judul utama
s.markdown('<div class="centered-title">Aplikasi Web Perhitungan Konsentrasi Normalitas, %Kadar, dan %RPD</div>', unsafe_allow_html=True)

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
    return round(rpd, 2), round(rata2, max_decimal), satuan, max_decimal# ----------------------------
# PENDAHULUAN & KETERANGAN
# ----------------------------

s.markdown("#### 🧪 Pendahuluan", unsafe_allow_html=True)
s.markdown("""
Titrasi adalah metode analisis kuantitatif yang digunakan untuk menentukan konsentrasi suatu zat dalam larutan 
dengan mereaksikannya dengan larutan standar. Proses titrasi melibatkan penambahan larutan standar secara perlahan 
hingga reaksi selesai, yang ditandai dengan perubahan warna indikator.
""")

s.markdown("#### 📘 Rumus Titrasi", unsafe_allow_html=True)
s.markdown("###### pada web aplikasi ini rumus yang diaplikasikan adalah:")

s.markdown("**1. Normalitas (N):**")
s.latex(r"N = \frac{\text{mg titrat}}{\text{FP} \times \text{mL titran}\times \text{BE}}")

s.markdown("**2. Kadar (%):**")
s.latex(r"\% \text{kadar} = \frac{N \times \text{mL titran} \times \text{BE} \times 0.1 \times \text{FP}} {\text{volume titrat}}")

s.markdown("**3. %RPD (Relative Percent Difference):**")  
s.latex(r"\% \text{RPD} = \frac{| \text{N}_1 - \text{N}_2|} {\left(\frac{\text{N}_1 + \text{N}_2} {2}\right)} \times 100")

s.markdown("#### 🧬 Background Aplikasi", unsafe_allow_html=True)
s.markdown("""
Aplikasi ini dibuat untuk memudahkan praktikan kimia analitik dalam melakukan perhitungan titrasi secara cepat dan akurat. 
Dengan adanya fitur otomatisasi perhitungan, pengguna dapat mengurangi kesalahan manusia dan mempercepat analisis hasil percobaan.
""")
s.markdown("#### 🧮 Kalkulator titrasi", unsafe_allow_html=True)
# ----------------------------
# PERHITUNGAN KONSENTRASI
# ----------------------------
s.markdown('<div class="cute-section-title">Perhitungan Konsentrasi Normalitas</div>', unsafe_allow_html=True)

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
s.markdown('<div class="cute-section-title">Perhitungan Kadar</div>', unsafe_allow_html=True)

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
s.markdown('<div class="cute-section-title">Perhitungan %RPD</div>', unsafe_allow_html=True)

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

s.markdown("#### 👥 web ini  disusun oleh Kelompok 11 dalam project pemrograman komputer, yang beranggotakan:", unsafe_allow_html=True)
s.markdown("""
- Astrid Gustami Prameswari: 2460333
- Lailatushifa: 2460406
- Nailah Inaaya Iswadi: 2460455
- Rezhika Nur Maryam: 2460496
- Zhalva Chantika Kumala Putri: 2460547
""")
""", unsafe_allow_html=True)
