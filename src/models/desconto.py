import abc

class IDesconto(abc.ABC):
    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        pass

    def calcular_desconto(self, valor: float) -> float:
        return self.calcular(valor)

class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1  # 10% de desconto

    def calcular_desconto(self, valor: float) -> float:
        return self.calcular(valor)

class DescontoVIP(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2  # 20% de desconto

    def calcular_desconto(self, valor: float) -> float:
        return self.calcular(valor)

class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3  # 30% de desconto

    def calcular_desconto(self, valor: float) -> float:
        return self.calcular(valor)