from matplotlib import pyplot

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

pyplot.plot(kunlar,daromad,color="purple",marker="o",label="Haftalik daromad")
pyplot.title("Haftalik daromad diagrammasi")
pyplot.xlabel("Hafta kunlari")
pyplot.ylabel("Daromad")
pyplot.grid(True)
pyplot.legend()

pyplot.savefig("daromad.png")

pyplot.show()