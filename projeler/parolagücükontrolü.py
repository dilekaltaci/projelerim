import string

def parola_guclu_mu(parola):
    guc_puani = 0

    if len(parola) >= 8:
        guc_puani += 1
    elif len(parola) >= 12:
        guc_puani += 2

    if any(char.isupper() for char in parola):
        guc_puani += 1

    if any(char.islower() for char in parola):
        guc_puani += 1

    if any(char.isdigit() for char in parola):
        guc_puani += 1

    ozel_karakterler = set(string.punctuation)
    if any(char in ozel_karakterler for char in parola):
        guc_puani += 2

    return guc_puani

def main():
    parola = input("Parolanızı girin: ")

    guc_puani = parola_guclu_mu(parola)

    if guc_puani <= 2:
        print("Parolanız çok zayıf.")
    elif guc_puani <= 4:
        print("Parolanız orta düzeyde güçlü.")
    else:
        print("Parolanız güçlü.")

if __name__ == "__main__":
    main()
