def hitung_konsentrasi_titrat(volume_titran_ml, molaritas_titran, volume_titrat_ml, rasio_mol_titran=1, rasio_mol_titrat=1):
    """
    Menghitung konsentrasi titrat berdasarkan data titrasi.
    
    Parameters:
    - volume_titran_ml (float): Volume titran (dalam mL)
    - molaritas_titran (float): Konsentrasi titran (mol/L)
    - volume_titrat_ml (float): Volume titrat (dalam mL)
    - rasio_mol_titran (int): Perbandingan mol titran dari reaksi
    - rasio_mol_titrat (int): Perbandingan mol titrat dari reaksi

    Returns:
    - molaritas_titrat (float): Konsentrasi titrat (mol/L)
    """

    # Konversi volume dari mL ke L
    V1 = volume_titran_ml / 1000  # Titran (buret)
    V2 = volume_titrat_ml / 1000  # Titrat (erlenmeyer)

    # Jumlah mol titran
    mol_titran = molaritas_titran * V1

    # Menghitung mol titrat berdasarkan rasio stoikiometri
    mol_titrat = mol_titran * (rasio_mol_titrat / rasio_mol_titran)

    # Molaritas titrat
    molaritas_titrat = mol_titrat / V2

    return molaritas_titrat


# Contoh penggunaan
# V_titran = 25.0       # mL
# M_titran = 0.1        # mol/L
# V_titrat = 50.0       # mL

s.write(f"Vn")
V_titran = s.number_input();
s.write(f"M")
M_titran = s.number_input();
s.write(f"Vt")
V_titrat = s.number_input();


# Asumsikan rasio mol 1:1
M_titrat = hitung_konsentrasi_titrat(V_titran, M_titran, V_titrat)

import streamlit as s

s.write(f"Konsentrasi titrat adalah {M_titrat:.4f} mol/L")
