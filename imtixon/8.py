import json

try:
    with open("imtixon/products.json","r",encoding="UTF-8") as f:
        oqish=json.load(f)

        qidir=input("Mahsulot nomi: ")
        topildi=0
        for i in range(len(oqish)):
            if oqish[i]['nom']==qidir:
                topildi=1
                yangi=input("Yangi narxi: ")
                oqish[i]['miqdor']=int(yangi)
    if topildi==0:
        print("Bunday mahsulot mavjud emas!")
    else:
        with open("imtixon/products.json","w",encoding="UTF-8",newline="") as f:
            print(oqish)
            json.dump(oqish, f)
                

    

except FileNotFoundError as e:
    print("Fayl ochilmadi", e)
except Exception as e:
    print("Ko'zda tutilmagan error", e)