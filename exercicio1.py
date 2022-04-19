'''Desenvolva um programa que peça o tamanho de um arquivo para download
(em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).'''

'''tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) = 
= tempo em segundos.'''

arq = int(input("Informe o tamanho(mb) do arquivo à ser baixado:"))
vel = int(input("Informe a velocidade(Mbps) da sua internet:"))

tempo = arq / (vel / 8)
minutos = tempo / 60

print("O tempo aproximado do download é de: {} minutos".format(minutos))
