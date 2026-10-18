from enum import Enum

class Dydis(Enum):
    MAZA = "maža"
    VIDUTINE = "vidutinė"
    DIDELE = "didelė"

class Padas(Enum):
    PLONAS = "plonas"
    STORAS = "storas"

class Padazas(Enum):
    POMIDORU = "pomidorų"
    BBQ = "BBQ"
    CESNAKINIS = "česnakinis"

class Priedas(Enum):
    MOCARELA = "mocarela"
    BAZILIKAS = "bazilikas"
    PEPERONI = "peperoni"
    VISTIENA = "vištiena"
    SVOGUNAI = "svogūnai"

class Pica:
    def __init__(self):
        self.dydis = None
        self.padas = None
        self.padazas = None
        self.priedai = []

    def __str__(self):
        priedai = ", ".join(p.value for p in self.priedai) if self.priedai else "be priedų"
        return (f"{self.dydis.value} pica, {self.padas.value} padas, "
                f"{self.padazas.value} padažas, priedai: {priedai}")

class PicaBuilder:
    def __init__(self):
        self._pica = Pica()

    def set_dydi(self, dydis: Dydis):
        self._pica.dydis = dydis
        return self

    def set_padas(self, padas: Padas):
        self._pica.padas = padas
        return self

    def set_padazas(self, padazas: Padazas):
        self._pica.padazas = padazas
        return self

    def prideti_prieda(self, priedas: Priedas):
        self._pica.priedai.append(priedas)
        return self

    def sukurti(self):
        if self._pica.dydis is None:
            raise ValueError("Turi būti nurodytas picos dydis")
        pica = self._pica
        self._pica = Pica()  # išvalome, kad statytoją būtų galima naudoti pakartotinai
        return pica


if __name__ == "__main__":
    builder = PicaBuilder()

    pica1 = (builder
            .set_dydi(Dydis.MAZA)
            .set_padas(Padas.STORAS)
            .set_padazas(Padazas.BBQ)
            .prideti_prieda(Priedas.VISTIENA)
            .prideti_prieda(Priedas.SVOGUNAI)
            .sukurti())
    
    pica2 = (builder
                .set_dydi(Dydis.DIDELE)
                .set_padas(Padas.PLONAS)
                .set_padazas(Padazas.POMIDORU)
                .prideti_prieda(Priedas.PEPERONI)
                .sukurti())
    
    print(pica1)
    print(pica2)
