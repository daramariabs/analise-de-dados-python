import operator

def soma (numero1, numero2): return operator.add(numero1,numero2)

def subtracao (numero1, numero2): return operator.sub(numero1,numero2)

def multiplicacao (numero1, numero2): return operator.mul(numero1,numero2)

def divisao (numero1, numero2): return operator.truediv(numero1,numero2)

    
print(f"{'*'*10} Calculadora em Python {'*'*10}")

print("""
Selecione o numero da opção desejada: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
""")

opcao = int(input("Digite sua opção, 1 - 2 - 3 - 4: "))
num1 = int(input("\n Digite o primeiro número: "))
num2 = int(input("\n Digite o segundo número: "))

if opcao == 1:
    print(f"\n {num1} + {num2} = {soma(num1, num2)}" )
elif opcao == 2:
    print(f"\n {num1} - {num2} = {subtracao(num1, num2)}" )
elif opcao == 3:
    print(f"\n {num1} * {num2} = {multiplicacao(num1, num2)}" )
elif opcao == 4:
    print(f"\n {num1} / {num2} = {divisao(num1, num2)}" )
else:
    print("Opção invalida!")