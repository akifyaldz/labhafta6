# Öğrenci Adı Soyadı: Mehmet Akif Yaldız
# Öğrenci Numarası: 20253005003
# Ders: Python ile Programlama - Hafta 6 Laboratuvarı
# Tarih: 1 Kasım 2026
# Açıklama: Görev 2 - Metin analizörü
while True:
    cumle = input("Cümle: ")

    
    if cumle.strip() == "":
        print("Uyarı: Boş bir cümle giremezsiniz! Lütfen tekrar girin.\n")
        continue

    break


sesli_harfler = "aeıioöuü"

harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0

kelime_ici_bayrak = False  # Kelimeleri saymak için bayrak (flag)
sadece_harfler = ""        # Palindrom kontrolü için biriktirilecek harfler
ters_cumle = ""            # Cümlenin ters hali

for ch in cumle:
    # Tersini oluşturma
    ters_cumle = ch + ters_cumle

    # Rakam kontrolü
    if ch.isdigit():
        rakam_sayisi += 1

    # Harf kontrolleri
    if ch.isalpha():
        harf_sayisi += 1
        kucuk_ch = ch.lower()
        sadece_harfler += kucuk_ch

        if kucuk_ch in sesli_harfler:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1

    # Kelime sayma mantığı 
    if ch != " ":
        if not kelime_ici_bayrak:
            kelime_sayisi += 1
            kelime_ici_bayrak = True
    else:
        kelime_ici_bayrak = False

# Palindrom kontrolü 
if sadece_harfler == sadece_harfler[::-1]:
    palindrom_durumu = "Palindrom"
else:
    palindrom_durumu = "Palindrom değil"

# (f-string ile biçimlendirme)
print(f"Harf: {harf_sayisi}  Sesli: {sesli_sayisi}  Sessiz: {sessiz_sayisi}  Rakam: {rakam_sayisi}  Kelime: {kelime_sayisi}")
print(f"Ters: {ters_cumle}")
print(f"{palindrom_durumu}")