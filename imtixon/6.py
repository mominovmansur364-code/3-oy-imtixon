n=int(input("Nechta son kerak: "))
sonlar=[]
for i in range(n):
    sonlar.append(int(input("Son: ")))

natija=list(filter(lambda x:x>0,sonlar))
print(natija)