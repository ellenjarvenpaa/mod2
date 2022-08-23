leiviskä = float(input("anna leiviskät\n"))
naula = float(input("anna naulat\n"))
luoti = float(input("anna luodit\n"))

naula += leiviskä*20
luoti += naula*32
massa = luoti*13.3
gramma = massa/1000

print("massa nykymittojen mukaan: {:.0f} kilogrammaa ja {:.3f} grammaa".format(gramma, massa))