# Cálculo de Medidas de Dispersão

# Amplitude
def calc_amplitude():
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))
    maior_valor = max(valores_int)
    menor_valor = min(valores_int)
    amplitude = maior_valor - menor_valor
    print(f'a amplitude da sequência de dados é: {amplitude}')
# calc_amplitude()

# Variância
def calc_variancia():
    print("[1] variância populacional")
    print("[2] variância amostral")
    escolha = input("Que tipo de variância deseja calcular? ")
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))
    x = 0
    for valor in valores_int:
        x += valor

    media = x / len(valores_int)

    x1 = 0
    N = 0
    if escolha == "1":
        N = len(valores_int)
    elif escolha == "2":
        N = len(valores_int) - 1
    else:
        exit()

    for elemento in valores_int:
        x1 += pow(elemento - media, 2) #* (elemento - media)

    variancia = x1 / N
    if escolha == "1":
        print(f'a variância populacional do conjunto de dados é: {variancia:.1f}')
    elif escolha == "2":
        print(f'a variância amostral do conjunto de dados é: {variancia:.1f}')
#calc_variancia()

# Desvio Padrão
def calc_desvio_padrao():
    print("[1] desvio padrão populacional")
    print("[2] desvio padrão amostral")
    escolha = input("Que tipo de desvio padrão deseja calcular? ")
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))

    N = 0
    if escolha == "1":
        N = len(valores_int)
    elif escolha == "2":
        N = len(valores_int) - 1
    else:
        exit()

    x = 0
    for valor in valores_int:
        x += valor

    media = x / len(valores_int)

    x1 = 0
    for elemento in valores_int:
        x1 += pow(elemento - media, 2)

    variancia = x1 / N

    desvio_padrao = variancia ** 0.5
    if escolha == "1":
        print(f'o desvio padrao populacional do conjunto de dados é: {desvio_padrao:.1f}')
    elif escolha == "2":
        print(f'o desvio padrao amostral do conjunto de dados é: {desvio_padrao:.1f}')
#calc_desvio_padrao()



# Coeficiente de variação
def calc_coeficiente_variacao():
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))
    x = 0
    for valor in valores_int:
        x += valor

    media = x / len(valores_int)
    x1 = 0
    for elemento in valores_int:
        x1 += pow(elemento - media, 2)

    variancia = x1 / len(valores_int)

    desvio_padrao = variancia ** 0.5

    Cv = (desvio_padrao / media) * 100

    print(f'o coeficiente de variação do conjunto de dados é: {Cv:.1f}%')
#calc_coeficiente_variacao()

