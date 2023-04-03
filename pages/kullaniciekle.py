import streamlit as st
from fonksiyonlar import *
import hashlib

baglan("pet.db")
tabloYap("kullanicilar","kullaniciadi TEXT,sifre TEXT,rol TEXT")
if "key" in st.session_state:
    with st.form("kullaniciekle",clear_on_submit=True):
        kullaniciadi=st.text_input("Kullanıcı Adı")
        sifre=st.text_input("Şifre",type="password")
        sifre2=st.text_input("Şifre Tekrar",type="password")
        rol=st.selectbox("Rol Seçiniz",["Personel","Yönetici","Sahip"])
        ekle=st.form_submit_button("Kullanıcı Ekle")
        if ekle:
            if sifre==sifre2:
                sonuc = hashlib.md5(sifre.encode())
                sifresafe=sonuc.hexdigest()
                if userVarmi(kullaniciadi):
                    st.error("Böyle Bir Kullanıcı Zaten Var")
                else:
                    veriEkle("kullanicilar",kullaniciadi,sifresafe,rol)
                    st.success("Kullanıcı Başarılı Bir Şekilde Eklendi")
            else:
                st.error("Girdiğiniz Şifreler Birbirinden Farklı")
else:
    st.write("Giriş Yapınız")