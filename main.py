urunler = {
    "su": 10,
    "çikolata": 25,
    "sandviç": 50,
    "meyve suyu": 30,
    "kurabiye": 20
}

sepet = []


def urunleri_goster():
    print("\n--- ÜRÜNLER ---")

    for urun, fiyat in urunler.items():
        print(urun, "-", fiyat, "TL")


def sepete_ekle():
    urun = input("Hangi ürünü almak istiyorsun? ").lower()

    if urun in urunler:
        sepet.append(urun)
        print(urun, "sepete eklendi.")
    else:
        print("Bu ürün marketimizde bulunmuyor.")


def sepeti_goster():
    print("\n--- SEPETİN ---")

    if len(sepet) == 0:
        print("Sepetin şu anda boş.")
        return

    toplam = 0

    for urun in sepet:
        fiyat = urunler[urun]
        print("-", urun, "-", fiyat, "TL")
        toplam += fiyat

    print("Toplam:", toplam, "TL")


def urun_cikar():
    if len(sepet) == 0:
        print("Sepetin zaten boş.")
        return

    urun = input("Hangi ürünü çıkarmak istiyorsun? ").lower()

    if urun in sepet:
        sepet.remove(urun)
        print(urun, "sepetten çıkarıldı.")
    else:
        print("Bu ürün sepetinde bulunmuyor.")


def odeme_yap():
    if len(sepet) == 0:
        print("Sepetin boş olduğu için ödeme yapamazsın.")
        return

    toplam = 0

    for urun in sepet:
        toplam += urunler[urun]

    print("\nÖdenecek tutar:", toplam, "TL")

    butce = int(input("Kaç TL paran var? "))

    if butce >= toplam:
        para_ustu = butce - toplam

        print("Ödeme başarılı!")
        print("Para üstün:", para_ustu, "TL")

        sepet.clear()

    else:
        eksik = toplam - butce

        print("Yeterli paran yok.")
        print(eksik, "TL daha gerekiyor.")


print("PYTHON MINI MARKET")
print("------------------")

isim = input("Adın nedir? ")

print("\nHoş geldin", isim + "!")


while True:
    print("\n--- ANA MENÜ ---")
    print("1 - Ürünleri göster")
    print("2 - Sepete ürün ekle")
    print("3 - Sepetimi göster")
    print("4 - Sepetten ürün çıkar")
    print("5 - Ödeme yap")
    print("6 - Çıkış")

    secim = input("Seçimin: ")

    if secim == "1":
        urunleri_goster()

    elif secim == "2":
        sepete_ekle()

    elif secim == "3":
        sepeti_goster()

    elif secim == "4":
        urun_cikar()

    elif secim == "5":
        odeme_yap()

    elif secim == "6":
        print("\nGörüşürüz", isim + "!")
        break

    else:
        print("Lütfen 1 ile 6 arasında bir seçim yap.")