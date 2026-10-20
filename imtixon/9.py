def tahlil_qil(sonlar):
    juft=0
    toq=0
    eng_katta=sonlar[0]

    for i in sonlar:
        if i>eng_katta:
            eng_katta=i

        if i%2==0:
            juft+=i
        if i%2!=0:
            toq+=i
    return juft,toq,eng_katta

n=int(input("Nechta son kerak: "))
sonlar=[]

for i in range(n):
    sonlar.append(int(input("Son: ")))

natija=tahlil_qil(sonlar)

print(f"Juft sonlar yig'indisi: {natija[0]}")
print(f"Toq sonlar yig'indisi: {natija[1]}")
print(f"Eng katta son: {natija[2]}")