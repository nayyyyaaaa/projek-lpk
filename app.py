import streamlit as s

def N(bobot_titrat, faktor_pengali, volume_titran, BE):
    hasil = bobot_titrat / (faktor_pengali * volume_titran * BE)
    return hasil

bobot_titrat_mg = s.number_input("Bobot Titrat (mg)")
faktor_pengali = s.number_input("faktor pengali")
volume_titran = s.number_input("volume titran")
bobot_molekul_titrat = s.number_input("BE")

hasil = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
hasil = round(hasil, 4)

s.write(hasil)

def kadar(volume_titran_kadar, konsentrasi_titran_kadar, BE_kadar, faktor_pengali_kadar, volume_titrat):
    hasil = (volume_titran_kadar * konsentrasi_titran_kadar * BE_kadar * 0.1 * faktor_pengali_kadar) / volume_titrat
    return hasil

volume_titran_kadar = s.number_input("volume titran (kadar)")
konsentrasi_titran_mL_kadar = hasil  # Fix: use previously calculated 'hasil' instead of re-calling N
bobot_molekul_titrat_kadar = s.number_input("BE (kadar)")
faktor_pengali_kadar = s.number_input("faktor pengali (kadar)")
volume_titrat_kadar = s.number_input("volume titrat (kadar)")

hasil2 = kadar(volume_titran_kadar, konsentrasi_titran_mL_kadar, bobot_molekul_titrat_kadar, faktor_pengali_kadar, volume_titrat_kadar)
hasil2 = round(hasil2, 2)  # Fix: use hasil2 instead of hasil

s.write(hasil2)
