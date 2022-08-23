leiviskä = float(input("anna leiviskät\n"))
naula = float(input("anna naulat\n"))
luoti = float(input("anna luodit\n"))

naula += leiviskä*20
luoti += naula*32
massa = luoti*13.3
gramma = massa/1000

print("massa nykymittojen mukaan: {:.1f} kilogrammaa ja {:.3f}".format(gramma, massa))