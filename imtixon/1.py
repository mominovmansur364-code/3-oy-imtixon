
n=int(input("Nechta ustun kerak: "))
m=int(input("Nechta qator kerak: "))

sonlar=[]

for i in range(n):
    for j in range(m):
        sonlar.append(input("Son: "))

yigindi=0
for i in sonlar:
        yigindi+=int(i)
print(f"Yigindi: {yigindi}")