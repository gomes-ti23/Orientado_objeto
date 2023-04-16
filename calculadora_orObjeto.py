class Calculadora():
    def __init__(self, operador) -> None:
        self.operador = operador
        self.memoria = []
        
    def oprsomar(self, num1:int, num2:int) -> int | float:
        resultado = num1 + num2
        self.memoria.append(resultado)
        return resultado
    def oprsubtrair(self, num1:int, num2:int) -> int | float:
        resultado = num1 - num2
        self.memoria.append(resultado)
        return resultado
    def oprmultiplicar (self, num1: int, num2: int) -> int | float:
        resultado = num1 * num2
        self.memoria.append(resultado)
        return resultado
    def oprdividir (self, num1:int, num2: int) -> int | float:
        resultado = num1 / num2
        self.memoria.append(resultado)
        return resultado

