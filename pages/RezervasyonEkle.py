import streamlit as st
from fonksiyonlar import *
st.title("Rezervasyon")
baglan("pet.db")
tabloYap("rezervasyonlar",
         "isim TEXT,baslangic TEXT,bitis TEXT,fiyat REAL,notlar TEXT")

with st.form("rezervasyonekle",clear_on_submit=True):
    isim=st.selectbox("Misafir Seçin",hayvanisimleri())
    baslangic=st.date_input("Giriş Tarihi")
    bitis=st.date_input("Çıkış Tarihi")
    notlar=st.text_area("Notlar")
    ekle=st.form_submit_button("Rezervasyon Ekle")
    if ekle:
        gun=bitis-baslangic
        gun=gun.days
        fiyat=gun*200
        baslangic=str(baslangic)
        bitis=str(bitis)
        veriEkle("rezervasyonlar",isim,baslangic,bitis,fiyat,notlar)
        st.success("Rezervasyon Başarılı Bir Şekilde Eklendi")
        fiyatmesaj="Toplam Fiyat:"+str(fiyat)
        st.warning(fiyatmesaj)



