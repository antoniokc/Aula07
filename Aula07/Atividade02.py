def multa():
    if peso > 100:
        excesso = peso - 100
        vl_multa = excesso * 4
        print(f"O excesso foi de {excesso}KG, sua multa é de R${vl_multa:.2f}")
    else:
        print("Não teve multa")


peso = float(input("Informar o peso: "))

multa()
