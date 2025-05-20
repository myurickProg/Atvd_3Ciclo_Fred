# Medidas de Posição ou Localidade


def interpolar(lista, percentil): # interpola quartis, decis e percentis acima de 0.1
    n = len(lista)
    pos = percentil * (n + 1)

    if pos <= 1:
        return lista[0]
    elif pos >= n:
        return lista[-1]
    else:
        i = int(pos) - 1
        fracao = pos - int(pos)
        return lista[i] + (lista[i + 1] - lista[i]) * fracao


def interpolar_percentis(lista, percentil):
    if not 0 <= percentil <= 1:
        raise ValueError("O percentil deve estar entre 0 e 1.")

    lista = sorted(lista)
    n = len(lista)

    pos = percentil * (n - 1)
    i = int(pos)
    fracao = pos - i

    if i + 1 < n:
        return lista[i] + (lista[i + 1] - lista[i]) * fracao
    else:
        return lista[i]

# Quartis:
def calc_quartis():
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))
    valores_int.sort()

    q1 = interpolar(valores_int, 0.25)
    q2 = interpolar(valores_int, 0.5)
    q3 = interpolar(valores_int, 0.75)

    print(f'primeiro quartil: {q1}')
    print(f'segundo quartil(mediana): {q2}')
    print(f'terceiro quartil: {q3}')

#calc_quartis()

# Percentis:
def calc_decis():
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))
    valores_int.sort()

    d1 = interpolar(valores_int, 0.1)
    d2 = interpolar(valores_int, 0.2)
    d3 = interpolar(valores_int, 0.3)
    d4 = interpolar(valores_int, 0.4)
    d5 = interpolar(valores_int, 0.5)
    d6 = interpolar(valores_int, 0.6)
    d7 = interpolar(valores_int, 0.7)
    d8 = interpolar(valores_int, 0.8)
    d9 = interpolar(valores_int, 0.9)
    d10 = interpolar(valores_int, 1)

    print(f'primeiro decil: {d1}')
    print(f'segundo decil: {d2}')
    print(f'terceiro decil: {d3}')
    print(f'quarto decil: {d4}')
    print(f'quinto decil: {d5}')
    print(f'sexto decil: {d6}')
    print(f'sétimo decil: {d7}')
    print(f'oitavo decil: {d8}')
    print(f'nono decil: {d9}')
    print(f'décimo decil: {d10}')
#calc_decis()

def calc_percentis():
    valores_int = list(map(int, input("digite os valores do conjunto de dados: ").split()))
    valores_int.sort()

    escolha = int(input("Escolha qual percentil deseja calcular(de 1 a 100): "))

    percentil_escolha =  escolha / 100
    percentil = interpolar_percentis(valores_int, percentil_escolha)
    print(f'percentil nº{escolha}: {percentil:.2f}')

calc_percentis()
