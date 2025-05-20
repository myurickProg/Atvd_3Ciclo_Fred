# Classificação de uma sequência de valores


# Simetria, Assimetria negativa e positiva
def classificar_assimetria():
    x = 0
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))
    for valor in valores_int:
        x += valor

    media = x / len(valores_int)

    n = len(valores_int)
    if n % 2 == 0:
        x1 = n / 2
        x2 = (n / 2) + 1
        pos = int((x1 + x2) / 2)
    else:
        pos = int((n + 1) / 2)

    mediana = valores_int[pos] - 1
    if media == mediana:
        print("Sequência simétrica")
    elif media < mediana:
        print("Assimétrica negativa")
    else:
        print("Assimétrica positiva")

# classificar_assimetria()

# Amodal, Unimodal e multimodal
def classificar_moda():
    lista_int = list(map(int, input("digite valores para descobrir a moda dos dados: ").split()))
    dict_int = {}
    for elemento in lista_int:
        if elemento in dict_int:
            dict_int[elemento] += 1
        else:
            dict_int[elemento] = 1

    max_frequencia = max(dict_int.values())
    modas = []
    for num, freq in dict_int.items():
        if freq == max_frequencia:
            modas.append(num)

    if len(modas) == len(dict_int):
        classificacao = "Amodal"
    elif len(modas) == 1:
        classificacao = "Unimodal"
    else:
        classificacao = "Multimodal"

    print(f'Moda(s): {modas} com frequência: {max_frequencia}')
    print(f'Classificação: {classificacao}')

classificar_moda()