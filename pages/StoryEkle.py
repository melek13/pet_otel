import streamlit as st
from fonksiyonlar import *
import random
from PIL import Image

baglan("pet.db")
tabloYap("storyler","id INTEGER,resim TEXT")

hayvanisim=st.selectbox("Hayvan Seçiniz",hayvanisimleri())
if len(hayvanisim)>0:
    idsec=st.selectbox("Rezervasyon Seçiniz",hayvantorez(hayvanisim))

with st.form("storyekle",clear_on_submit=True):
    resimal = st.file_uploader("Resim ekle")
    ekle=st.form_submit_button("Story Ekle")
    if ekle:
        resimisim="img/"+hayvanisim+str(random.randint(1,10000))+".jpg"
        img = Image.open(resimal)  # resmi açtık
        img = img.save(resimisim)  # resmi kaydettik
        veriEkle("storyler",idsec,resimisim)
        st.success("Story Başarıyla Eklendi")





