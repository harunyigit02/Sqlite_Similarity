import sqlite3


def custom_similarity(metin1, metin2):
    # Her iki metindeki karakter dizilerini al
    karakterler1 = set(metin1)
    karakterler2 = set(metin2)

    # İki metin arasındaki ortak karakterlerin sayısını hesapla
    ortak_karakterler = len(karakterler1.intersection(karakterler2))

    # Benzerlik skoru hesapla
    benzerlik_skoru = ortak_karakterler / max(len(karakterler1), len(karakterler2))

    return benzerlik_skoru
def jaccard_similarity(metin1, metin2):
    # Metinleri kelimelere ayırarak kümelere dönüştür
    kume1 = set()
    for kelime in metin1.split():
        kume1.add(kelime)
    kume2 = set()
    for kelime in metin2.split():
        kume2.add(kelime)

    # Kesim ve birleşim kümesini hesapla
    kesisim = 0
    for kelime in kume1:
        if kelime in kume2:
            kesisim += 1
    birlesim = len(kume1) + len(kume2) - kesisim

    # Jaccard benzerlik katsayısını hesapla
    benzerlik_katsayisi = kesisim / birlesim
    return benzerlik_katsayisi

def to_file(metin1,metin2,Jresult,Cresult):
    with open("C:/Users/ASUS/Desktop/result.txt", "w") as dosya:
        dosya.write("metin1: {}\n".format(metin1))
        dosya.write("metin2: {}\n".format(metin2))
        dosya.write("jaccard: {}\n".format(Jresult))
        dosya.write("custom: {}\n".format(Cresult))


conn = sqlite3.connect("database.db")
cursor = conn.cursor()
create_table = "CREATE TABLE IF NOT EXISTS texts (text1 TEXT , text2 TEXT)"
cursor.execute(create_table)

text1 = input("enter text1:")
text2 = input("enter text2:")

insert_table = "INSERT INTO texts (text1, text2) VALUES (?, ?)"
cursor.execute(insert_table, (text1, text2))
select_table1 = "SELECT text1 FROM texts"
cursor.execute(select_table1)
data1 = list(cursor)
metin1= data1[0][0]
select_table2 = "SELECT text2 FROM texts"
cursor.execute(select_table2)
data2=list(cursor)
metin2=data2[0][0]

delete_table = "DELETE FROM texts"
cursor.execute(delete_table)

conn.commit()

jaccard_sonuc=jaccard_similarity(metin1,metin2)
custom_sonuc=custom_similarity(metin1,metin2)
to_file(metin1,metin2,jaccard_sonuc,custom_sonuc)

