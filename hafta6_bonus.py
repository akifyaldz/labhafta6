# 1. GİRDİ ve 2. DOĞRULA
numara_15 = "453914880343646"

# Doğrulama: 15 karakter ve hepsi rakam mı kontrolü
if len(numara_15) != 15 or not numara_15.isdigit():
    print("Numara tam olarak 15 basamaklı rakamlardan oluşmalıdır!")
else:
    bulunan_hane = -1

    # 3. İŞLE
    # 0-9 arası rakamları sırayla dene
    for deneme in range(10):
        tam_numara = numara_15 + str(deneme)  # 16 haneli tam numara
        toplam = 0

        # Luhn algoritması: En sağdaki basamaktan (16. hane) sola doğru ilerle
        # İndeksler: 15, 14, 13, ..., 0
        for i in range(15, -1, -1):
            basamak = int(tam_numara[i])
            konum_sagdan = 16 - i  # 1: en sağdaki (kontrol hanesi), 2: bir önceki...

            # Sağdan çift sıralı olanlar (2, 4, 6, ...) 2 ile çarpılır
            if konum_sagdan % 2 == 0:
                basamak *= 2
                if basamak > 9:
                    basamak -= 9  # veya basamak // 10 + basamak % 10

            toplam += basamak

        # Toplam 10'a tam bölünüyorsa geçerli kontrol hanesi bulunmuştur
        if toplam % 10 == 0:
            bulunan_hane = deneme
            break  # İlk geçerli olanda çık

    # 4. ÇIKTI
    print(f"15 haneli numara  : {numara_15}")
    print(f"Bulunan kontrol hanesi : {bulunan_hane}")
    print(f"Tam numara (16 hane)   : {numara_15}{bulunan_hane}")