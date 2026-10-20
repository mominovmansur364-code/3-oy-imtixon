import csv

try:
    f=open("products.csv","r",encoding="UTF-8")
    f.close()
except FileNotFoundError:
    with open("products.csv","w",encoding="UTF-8",newline="") as f:
        pen=csv.writer(f)
        pen.writerow(["Nomi","Narxi","Soni"])
    nomi=input("Nomi: ")
    narxi=input("Narxi: ")
    soni=input("Soni: ")

    with open("products.csv","a",encoding="UTF-8") as f:
        pen=csv.writer(f)
        pen.writerow([nomi.capitalize(),narxi,soni])
        print("Muvaffaqiyatli saqlandi!")