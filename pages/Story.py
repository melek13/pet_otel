import streamlit as st
from fonksiyonlar import *

baglan("pet.db")

hayvanisim=st.selectbox("Hayvan Seçiniz",hayvanisimleri())
if len(hayvanisim)>0:
    idsec=st.selectbox("Rezervasyon Seçiniz",hayvantorez(hayvanisim))
    getir=st.button("Storyleri Getir")
    if getir:
        storyGetir(idsec)
