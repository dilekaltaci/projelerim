def hesap_makinesi():
    sayi1 = float(input("İlk sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")
    if islem == '+':
        sonuc = sayi1 + sayi2
        print(f"{sayi1} + {sayi2} = {sonuc}")
    elif islem == '-':
        sonuc = sayi1 - sayi2
        print(f"{sayi1} - {sayi2} = {sonuc}")
    elif islem == '*':
        sonuc = sayi1 * sayi2
        print(f"{sayi1} * {sayi2} = {sonuc}")
    elif islem == '/':
        if sayi2 == 0:
            print("Hata! Sıfıra bölme hatası.")
        else:
            sonuc = sayi1 / sayi2
            print(f"{sayi1} / {sayi2} = {sonuc}")
    else:
        print("Geçersiz işlem! Lütfen doğru işlem seçin (+, -, *, /).")

hesap_makinesi()

