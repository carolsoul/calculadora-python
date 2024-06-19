# Calculadora simples em python só pra treinar!

num1 = 0
num2 = 0
result = 0
operacao = ''

while True:
    num1 = float(input("Digite um número: "))
    operacao = input("Digite a operação a ser executada: ")
    num2 = float(input("Digite outro número: "))

    if operacao == '+':
        result = num1 + num2
    elif operacao == '-':
        result = num1 - num2
    elif operacao == '*':
        result = num1 * num2
    elif operacao == '/':
        result = num1 / num2
    else:
        print("Operação não reconhecida!")

    print(f"{num1} {operacao} {num2} = {result}")