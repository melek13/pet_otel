import streamlit as st
from fonksiyonlar import *
import hashlib
st.title("Ana Sayfa")

baglan("pet.db")

if "key" in st.session_state:
    st.sidebar.write("Hoşgeldin")
    cikisyap=st.sidebar.button("Çıkış Yap")
    if cikisyap:
        del st.session_state['key']
        st.experimental_rerun()
else:
    with st.sidebar.form("giris", clear_on_submit=True):
        kullaniciadi = st.text_input("Kullanıcı adı")
        sifre = st.text_input("Şifre", type="password")
        girisyap = st.form_submit_button("Giriş Yap")
        if girisyap:
            sonuc = hashlib.md5(sifre.encode())
            sifresafe = sonuc.hexdigest()
            sonuc = girisYap(kullaniciadi, sifresafe)
            if sonuc:
                st.success("Giriş Başarılı")
                st.session_state['key'] = "giriş"
                st.experimental_rerun()
            else:
                st.error("Bilgiler Yanlış")