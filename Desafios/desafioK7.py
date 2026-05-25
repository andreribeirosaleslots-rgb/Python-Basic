alturaparde = float(input("Digite a altura da parede em metros: "))
larguraparde = float(input("Digite a largura da parede em metros: "))

areaparde = alturaparde * larguraparde
tintaparde = areaparde / 2

print("A área da parede é de {} m² e a quantidade de tinta necessária para pintá-la é de {} litros".format(areaparde, tintaparde))