# Cálculo de Medidas de Tendência Central


# 1 - Média arítmética:
def media_aritmetica():
    x = 0

    valores_int = list(map(int, input("digite valores para descobrir a média aritmética dos dados: ").split()))
    for valor in valores_int:
        x += valor

    media = x / len(valores_int)

    print(f'Essa é a média dos valores: {media}')

#media_aritmetica()


# 2 - Média aritmética ponderada:
def media_ponderada():
    p = 0
    pesos = []
    x = 0

    valores_int = list(map(int, input("digite valores para descobrir a média aritmética ponderada dos dados: ").split()))

    for i in range(len(valores_int)):
        pesos.append(input(f'Digite o peso do valor {valores_int[i]}: '))

    for peso in pesos:
        p += int(peso)

    for i in range(len(valores_int)):
        n1 = int(valores_int[i])
        n2 = int(pesos[i])
        x += n1 * n2

    media = x / p
    print(f'A média aritmética ponderada dos dados é {media}')

#media_ponderada()


# 3 - Mediana
def find_mediana():
    n = 0
    valores_int = list(map(int, input("digite valores para descobrir a mediana dos dados: ").split()))
    n = len(valores_int)
    if n % 2 == 0:
        x1 = n / 2
        x2 = (n / 2) + 1
        pos = int((x1 + x2) / 2)
    else:
        pos = int((n + 1) / 2)

    mediana = valores_int[pos] - 1
    #print(pos)
    print(f'A mediana dos dados é: {mediana}')

# find_mediana()


# 4 - Moda
def find_moda():
    lista_int = list(map(int, input("digite valores para descobrir a moda dos dados: ").split()))
    modas_freq = {}
    for n in lista_int:
        if n in modas_freq:
            modas_freq[n] += 1
        else:
            modas_freq[n] = 1

    freq_moda = max(modas_freq.values())
    moda = [num for num, freq in modas_freq.items() if freq == freq_moda]

    print(f'{moda} é a moda do conjunto de dados e aparece {freq_moda} vezes')
# find_moda()