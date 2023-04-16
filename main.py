from calculadora_orObjeto import Calculadora
while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: ")) 
    oper = str(input("Digiti a operação desejada: "))        
    calc = Calculadora(oper)
    if calc.operador == "+":
        print(f'O número {num1} somado com {num2} gera o resultado {calc.oprsomar(num1, num2)}')
    elif calc.operador == "-":
        print(f'O número {num1} subtraido {num2} gera o resultado {calc.oprsubtrair(num1, num2)}')
    elif  calc.operador == "*":
        print(f'O número {num1} multiplicado {num2} gera o resultado {calc.oprmultiplicar(num1, num2)}')
    elif calc.operador == "/":
        print(f'O número {num1} dividido {num2} gera o resultado {calc.oprdividir(num1, num2)}')
    question = input("Deseja continuar calculando: ").upper().strip()
    if question == "NAO":
        break