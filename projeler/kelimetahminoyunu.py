import random

def kelime_sec():
    kelimeler = ["elma", "armut", "kiraz", "muz", "çilek", "portakal", "karpuz"]
    return random.choice(kelimeler)

def hangman():
    kelime = kelime_sec()
    tahmin_edilen = ["_"] * len(kelime)
    yanlis_tahmin_sayisi = 0
    max_yanlis = 5
    kullanilan_harfler = []

    print("Kelimeyi tahmin etmeye başlayın!")
    print(" ".join(tahmin_edilen))

    while True:
        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1:
            print("Lütfen sadece bir harf girin.")
            continue
        elif not tahmin.isalpha():
            print("Lütfen bir harf girin.")
            continue
        elif tahmin in kullanilan_harfler:
            print("Bu harfi zaten tahmin ettiniz. Başka bir harf deneyin.")
            continue

        kullanilan_harfler.append(tahmin)

        if tahmin in kelime:
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    tahmin_edilen[i] = tahmin
            print("Doğru tahmin! Kelime şu şekilde görünüyor:")
            print(" ".join(tahmin_edilen))
        else:
            yanlis_tahmin_sayisi += 1
            print("Yanlış tahmin!")
            print(f"Kalan can: {max_yanlis - yanlis_tahmin_sayisi}")
            if yanlis_tahmin_sayisi == max_yanlis:
                print("Üzgünüm, oyunu kaybettiniz!")
                break

        if "_" not in tahmin_edilen:
            print("Tebrikler, kelimeyi doğru tahmin ettiniz!")
            break

if __name__ == "__main__":
    hangman()
