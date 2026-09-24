import abc

class IDesconto(abc.ABC):
    @abc.abstractmethod
    def calcular_desconto(self, valor: float) -> float:
        pass

class DescontoNormal(IDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.1  # 10% de desconto

class DescontoVIP(IDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.2  # 20% de desconto

class DescontoPremium(IDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.3  # 30% de desconto