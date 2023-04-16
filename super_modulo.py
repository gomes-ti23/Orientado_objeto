class Pessoa():
    def __init__(self, nome:str, idade:int, altura:float) -> None: #método construtor, passa caracteristicas para o objeto.
        self.nome = nome
        self.idade = idade
        self.altura = altura
                
#Instância: quando se cria um objeto, quando se atribui uma classe a uma variavel.    
registro = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
p1 = Pessoa(registro, idade, altura)
print(f'Meu nome é {p1.nome} e minha idade é {p1.idade} e minha altura é {p1.altura}')

class Endereco():
    def __init__(self, rua:str, numero:int, complemento:str, alarme: str) -> None:
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.alarme = alarme
    def indentificar (self):
        return f"Possuí alarme: {self.alarme}."
rua = input("Digite seu Endereço: ")
numero = input("Digite o número: ")
complemento = input("Digite o complemento: ")
alarme = input("Sua casa possuí alarme: ")
p2 = Endereco(rua, numero, complemento, alarme)

print(f'Seu endereço é {p2.rua} {p2.numero} {p2.complemento} e  {p2.indentificar()}.')