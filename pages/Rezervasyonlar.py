import streamlit as st
from fonksiyonlar import *
import pandas as pd

baglan("pet.db")
rezervasyonlar=veriGetir("rezervasyonlar")
rezervasyontablo=pd.DataFrame(rezervasyonlar)
rezervasyontablo.columns=["İsim","Başlangıç","Bitiş","Fiyat",
                          "Notlar"]
st.table(rezervasyontablo)
st.title("Rezervasyon Sil")
isimsil=st.text_input("Silmek İstediğiniz İsmi Giriniz")
sil=st.button("Sil")
if sil:
    rezervasyonSil(isimsil)
    st.success("Rezervasyon Silindi")
    st.experimental_rerun()

st.title("Rezervasyon Uzatma")

col1,col2,col3,col4=st.columns(4)

with col1:
    isim=st.text_input("Ziyaretçi İsmi")
with col2:
    tarih=st.date_input("Randevu Başlangıç")
with col3:
    yenibitis=st.date_input("Yeni Bitiş Tarihi")
with col4:
    st.write("Onaylıyorum")
    getir=st.button("Randevuyu Düzenle")

if getir:
    randevuUzat(isim, tarih, yenibitis)
    st.success("Randevu Tarihi Düzenlendi")

