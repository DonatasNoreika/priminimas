
import sqlalchemy

class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    pass

class IslaiduIrasas(Irasas):
    pass


zurnalas = []

pajamos1 = PajamuIrasas(500)
zurnalas.append(pajamos1)

islaidos1 = IslaiduIrasas(10)
zurnalas.append(islaidos1)

islaidos2 = IslaiduIrasas(100)
zurnalas.append(islaidos2)

suma = 0
for irasas in zurnalas:
    if isinstance(irasas, PajamuIrasas):
        suma += irasas.suma
    elif isinstance(irasas, IslaiduIrasas):
        suma -= irasas.suma
print(suma)

fdlakdjflajsdlfa