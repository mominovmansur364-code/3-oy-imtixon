n=int(input("Nechta son kerak: "))
sonlar=[]
for i in range(n):
    sonlar.append(int(input("Son: ")))

natija=list(map(lambda x:x*3,sonlar))
print(natija)
