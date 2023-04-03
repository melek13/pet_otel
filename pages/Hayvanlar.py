import streamlit as st
from fonksiyonlar import *
import pandas as pd
baglan("pet.db")
hayvanlar=veriGetir("hayvanlar")
hayvantablo=pd.DataFrame(hayvanlar)
hayvantablo.columns=["İsim","Tür","Irk","Sahip","Telefon","Resim"]
st.table(hayvantablo)