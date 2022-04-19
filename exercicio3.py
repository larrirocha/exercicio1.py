'''Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código.
Os códigos utilizados são:
10, 20, 30, 70 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
80 - Voto Nulo
90 - Voto em Branco
Desenvolva um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A porcentagem de votos nulos sobre o total de votos;
A porcentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.'''

eleitores = int(input("Quantidade total de votos:"))

candidato10 = 0
candidato20 = 0
candidato30 = 0
candidato70 = 0
nulo80 = 0
branco90 = 0
votantes = 0

while (votantes < eleitores):
    voto = int(input("Digite 10 para votar no candidato A, 20 no candidato B, 30 \n"
                     "no candidato C, 70 candidato D, 80 para anular seu voto e 90 \n"
                     "para voto em branco:"))
    if (voto == 10):
        candidato10 = candidato10 + 1
    elif (voto == 20):
        candidato20 = candidato20 + 1
    elif (voto == 30):
        candidato30 = candidato30 + 1
    elif (voto == 70):
        candidato70 = candidato70 + 1
    elif (voto == 80):
        nulo80 = nulo80 + 1
    elif (voto == 90):
        branco90 = branco90 + 1
    votantes = votantes + 1

    Percentual_nulos = (nulo80 * eleitores) / 100
    Percentual_brancos = (branco90 * eleitores) / 100

    print("O candidato A teve {} votos".format(candidato10))
    print("O candidato B teve {} votos".format(candidato20))
    print("O candidato C teve {} votos".format(candidato30))
    print("O candidato D teve {} votos".format(candidato70))
    print("Houveram {} votos nulos".format(nulo80))
    print("Houveram {} votos brancos".format(branco90))
    print("Foram {:.2f}% de votos nulos".format(Percentual_nulos))
    print("Foram {:.2f}% de votos brancos".format(Percentual_brancos))
