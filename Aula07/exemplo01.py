# Funções em pyhton inicia com a palavra
# reservada def.
# Funções são rotinas em seu conceito
# São Blocos de Códigos que só serão executado, se forem chamados.

# def saudacao():
#    print("Olá Mundo")


# saudacao()

# def mostrar_linha():
#    print(30*"=")

# mostrar_linha()
# print("MODULO 01")
# mostrar_linha()
# print("Teoria")

# def saudacao(texto):
#     print(f"Olá {texto}, SEJA BEM VINDO MESTRE")

# nome = input("Diga seu nome: ")
# saudacao(nome)

# def somar(a, b):
#     s = a + b
# print(soma)
#     return s


# s = 0
# somar(4, 5)
# print(f"O valor da variavel é {soma}")

def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    n1 = int(input("informar o numero: "))
    n2 = int(input("informar o numero: "))

    soma = somar_numeros(n1, n2)
    print(soma)
