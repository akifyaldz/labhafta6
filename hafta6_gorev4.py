# Öğrenci Adı Soyadı: Mehmet Akif Yaldız
# Öğrenci Numarası: 20253005003
# Ders: Python ile Programlama - Hafta 6 Laboratuvarı
# Tarih: 1 Kasım 2026
# Açıklama: Görev 4 - Collatz kaşifi 


# 1. GİRDİ ve 2. DOĞRULA (a Bölümü için n değeri)

while True:
    n_giris = int(input("n: "))
    if n_giris <= 0:
        print("Uyarı: n pozitif bir tam sayı olmalıdır! Tekrar girin.\n")
        continue
    break


# 3. İŞLE ve 4. ÇIKTI (a Bölümü: Tek bir sayı için adımlar)

adim_sayisi = 0
en_yuksek_deger = n_giris
gecici_n = n_giris

while gecici_n > 1:
    # Kuralı tek satırda koşullu ifadeyle (ternary operator) yazma
    gecici_n = gecici_n // 2 if gecici_n % 2 == 0 else 3 * gecici_n + 1
    
    if gecici_n > en_yuksek_deger:
        en_yuksek_deger = gecici_n
        
    adim_sayisi += 1

print(f"{n_giris} -> 1: {adim_sayisi} adım, en yüksek değer {en_yuksek_deger}")


# 1. GİRDİ ve 2. DOĞRULA (b Bölümü için Üst Sınır)

while True:
    ust_sinir = int(input("Üst sınır: "))
    if ust_sinir <= 0:
        print("Uyarı: Üst sınır pozitif bir tam sayı olmalıdır! Tekrar girin.\n")
        continue
    break


# 3. İŞLE (b Bölümü: 1'den sınıra kadar iç içe döngüler)

maks_adim = 0
en_uzun_baslangic = 1

# Dış döngü (for): 1'den üst sınıra kadar olan sayılar
for baslangic in range(1, ust_sinir + 1):
    suanki_n = baslangic
    suanki_adim = 0
    
    # İç döngü (while): 1'e ulaşana kadar zinciri takip etme
    while suanki_n > 1:
        # Kural koşullu ifadeyle tek satırda
        suanki_n = suanki_n // 2 if suanki_n % 2 == 0 else 3 * suanki_n + 1
        suanki_adim += 1
        
    if suanki_adim > maks_adim:
        maks_adim = suanki_adim
        en_uzun_baslangic = baslangic


# 4. ÇIKTI (b Bölümü)

print(f"1-{ust_sinir} arasında en uzun zincir: {en_uzun_baslangic} ({maks_adim} adım)")