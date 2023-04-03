import streamlit as st
from fonksiyonlar import *
from PIL import Image
st.title("Pet Ekle")

baglan("pet.db")
tabloYap("hayvanlar",
         "isim TEXT,tur TEXT,irk TEXT,sahip TEXT,telefon TEXT,resim TEXT")
with st.form("hayvanekle",clear_on_submit=True):
    isim=st.text_input("İsim")
    tur=st.selectbox("Tür",["Köpek","Kedi"])
    irk=st.text_input("Irkı")
    sahip=st.text_input("Sahip İsmi")
    telefon=st.text_input("Telefon Numarası")
    #resim=st.text_input("Resim Ekle")
    resimal = st.file_uploader("Resim ekle",) #resim dosyası
    ekle=st.form_submit_button("Kayıt Ekle")
    if ekle:
        img=Image.open(resimal) #resmi açtık
        resimisim="img/"+isim+".jpg" #resme hayvan ismi verdik
        img=img.save(resimisim) #resmi kaydettik

        veriEkle("hayvanlar",isim,tur,irk,sahip,telefon,resimisim)
        st.success("Başarılı bir şekilde eklendi")
