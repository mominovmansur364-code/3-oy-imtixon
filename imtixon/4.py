talabalar = [("Ali", 85), ("Malika", 95), ("Vali", 78)]

natija = sorted(talabalar, key=lambda son: son[1], reverse=True)

print(natija)
