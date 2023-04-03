import streamlit as st
from fonksiyonlar import *
import hashlib

baglan("pet.db")
with st.form("giris",clear_on_submit=True):
    kullaniciadi=st.text_input("Kullanıcı adı")
    sifre=st.text_input("Şifre",type="password")
    girisyap=st.form_submit_button("Giriş Yap")
    if girisyap:
        sonuc = hashlib.md5(sifre.encode())
        sifresafe = sonuc.hexdigest()
        sonuc=girisYap(kullaniciadi,sifresafe)
        if sonuc:
            st.success("Giriş Başarılı")
            st.session_state['key'] = "giriş"
        else:
            st.error("Bilgiler Yanlış")