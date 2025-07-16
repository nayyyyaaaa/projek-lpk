import streamlit as s

def N(bobot_titrat, faktor_pengali, volume_titran, BE):

  hasil = bobot_titrat/(faktor_pengali*volume_titran*BE)
  
  return hasil

bobot_titrat_mg = s.number_input("Bobot Titrat (mg)")
faktor_pengali = s.number_input("faktor pengali")
volume_titran = s.number_input("volume titran")
bobot_molekul_titrat = s.number_input("BE")

hasil = N(bobot_titrat_mg, faktor_pengali, volume_titran, bobot_molekul_titrat)
hasil = round(hasil, 4)

s.write(hasil)
