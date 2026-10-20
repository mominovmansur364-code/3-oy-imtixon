mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

mahsulot_nomi = input("Mahsulot nomi: ")

if mahsulot_nomi in mahsulotlar:
    print("Siz qidirayotgan mahsulot bor")
    print(f"Mahsulot narxi: {mahsulotlar[mahsulot_nomi]} so'm")

    mahsulot_narxi = int(input("yangi narx: "))
    mahsulotlar[mahsulot_nomi] = mahsulot_narxi

    print(f"Yangi narx: {mahsulotlar[mahsulot_nomi]} so'm")
else:
    print("Noto'g'ri mahsulot nomi kiritildi")

print(mahsulotlar)
