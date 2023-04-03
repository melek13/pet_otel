import sqlite3
import streamlit as st
import datetime
def baglan(vt):
    global conn
    conn=sqlite3.connect(vt)
    global c
    c=conn.cursor()
    return "Veritabanı Başarılı Bir Şekilde Oluşturuldu"
def tabloYap(tabloisim,sutunlar):
    komut="CREATE TABLE IF NOT EXISTS "+tabloisim+"("+sutunlar+")"
    c.execute(komut)
    conn.commit()
def veriEkle(tabloisim,*veriler):
    komut="INSERT INTO "+tabloisim+" VALUES"+str(veriler)
    c.execute(komut)
    conn.commit()
def veriGetir(tabloisim):
    komut="SELECT * FROM "+tabloisim
    c.execute(komut)
    sonuc=c.fetchall()
    return sonuc
def hayvanisimleri():
    c.execute("SELECT isim FROM hayvanlar")
    isimler=c.fetchall()
    sonuc=[]
    for i in isimler:
        sonuc.append(i[0])
    return sonuc

def hayvantorez(hayvanisim):
    c.execute("SELECT rowid FROM rezervasyonlar WHERE isim=?",
              (hayvanisim,))
    idler=c.fetchall()
    idlist=[]
    for i in idler:
        idlist.append(i[0])
    return idlist

def storyGetir(rezid):
    c.execute("SELECT resim FROM storyler WHERE id=?",(rezid,))
    resimler=c.fetchall()
    for i in resimler:
        st.image(i[0])

def userVarmi(kullaniciadi):
    c.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=?",(kullaniciadi,))
    sonuc=c.fetchall()
    if len(sonuc)>0:
        return True
    else:
        return False

def girisYap(kullaniciadi,sifre):
    c.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=? AND sifre=?",(kullaniciadi,sifre))
    sonuc=c.fetchall()
    if len(sonuc)>0:
        return True
    else:
        return False
def rezervasyonSil(isim):
    c.execute("DELETE FROM rezervasyonlar WHERE isim=?",(isim,))
    conn.commit()
    return True

def randevuGetir(isim,baslangic):
    c.execute("SELECT * FROM rezervasyonlar WHERE isim=? AND baslangic=?",(isim,baslangic))
    sonuc=c.fetchone()
    return sonuc

def randevuUzat(isim,baslangic,yenibitis):
    yenibitis=str(yenibitis)
    c.execute("UPDATE rezervasyonlar SET bitis=? WHERE isim=? AND baslangic=?",(yenibitis,isim,baslangic))
    conn.commit()

