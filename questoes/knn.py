# [febre, enjoo, mancha]
x_train = [
    [1, 1, 0.75], # paciente 1 = doente[1]
    [0.5, 0, 0.5], # paciente 2 = doente[1]
    [0, 1, 0], # paciente 3 = doente[1]
    [0.5, 0, 1] # paciente 4 = saudável[0]
]
y_train = [1, 1, 1, 0]

x_test = [0.5, 0, 0.25] # paciente 5
k = 3

def calc_dist_euclidiana(a, b):
    return sum((a_i - b_i) ** 2 for a_i, b_i in zip(a, b)) ** 0.5

def knn(x_train, y_train, x_test, k):
    distancias = []
    for i in range(len(x_train)):
        dist = calc_dist_euclidiana(x_train[i], x_test)
        distancias.append((dist, y_train[i]))

    distancias.sort(key=lambda x: x[0])

    vizinhos = distancias[:k]

    votos = {}
    for _, label in vizinhos:
        votos[label] = votos.get(label, 0) + 1

    return max(votos, key=votos.get)

resultado = knn(x_train, y_train, x_test, k)
if resultado == 1:
    classificacao = "doente"
else:
    classificacao = "saudavel"
print(f'classe prevista para {x_test} (paciente 5): {resultado}, {classificacao}')