from abc import ABC, abstractmethod

class MokejimoProcesorius(ABC):
    # Interfeisas, kurio tikisi kliento kodas
    @abstractmethod
    def moketi(self, suma_eur: float) -> str:
        pass

class PayPalProcesorius(MokejimoProcesorius):
    def moketi(self, suma_eur: float) -> str:
        return f"Sumokėta {suma_eur:.2f} EUR per PayPal"

class StripeAPI:
    def nuskaiciuoti(self, suma_centais: int, valiuta: str) -> dict:
        return {"busena": "sėkminga", "suma": suma_centais, "valiuta": valiuta}

class StripeAdapteris(MokejimoProcesorius):
    # Adapteris - leidžia StripeAPI naudoti per MokejimoProcesorius interfeisą

    def __init__(self, stripe_api: StripeAPI):
        self._stripe = stripe_api

    def moketi(self, suma_eur: float) -> str:
        centai = round(suma_eur * 100)
        rezultatas = self._stripe.nuskaiciuoti(centai, "EUR")
        return (f"Sumokėta {rezultatas['suma'] / 100:.2f} {rezultatas['valiuta']} "
                f"per Stripe ({rezultatas['busena']})")

def atsiskaityti(procesorius: MokejimoProcesorius, suma: float):
    # Kliento pusėj
    print(procesorius.moketi(suma))


if __name__ == "__main__":
    atsiskaityti(PayPalProcesorius(), 19.99)
    atsiskaityti(StripeAdapteris(StripeAPI()), 42.50)
