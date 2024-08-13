import csv
import numpy as np
#caminho do arquivo CSV com raios de dobra e números das barras
csv_path = 'C:/origem_fabrica/Arquivos para configuração de máquinas/Chassi/Dobradora/Dobras para separação de tubos/Dados de dobra para separação/Dados para classificação de dobras.csv'

#Lendo arquivo CSV
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader) #pulando linha de cabeçalho
    lista_tubos = [(float(row[0]), float(row[1]), float(row[2])) for row in csv_reader]
    
n = len(lista_tubos)
arrayTubos = np.zeros((n,n), dtype=float)
tubes_inRange= np.zeros((n,2), dtype=float)
range_hCord = 0.045

for i in range(n):
    k = 3
    hCordi = lista_tubos[i][1]
    arrayTubos[i][0] = lista_tubos[i][0]
    arrayTubos[i][1] = hCordi
    for j in range(n):
        hCordj = lista_tubos[j][1]
        dif_hCord = abs(hCordi-hCordj)
        if dif_hCord <= range_hCord:
            arrayTubos[i][k] = lista_tubos[j][0]
            k = k+1
    arrayTubos[i][2] = k-3
        

indexSort_tubesInRange = np.argsort(tubes_inRange[:,1])
sorted_tubesInRange = tubes_inRange[indexSort_tubesInRange]

indexSort_arrayTubos = np.argsort(arrayTubos[:,2])
sorted_arrayTubos = arrayTubos[indexSort_arrayTubos]

for i in range(n):
    groupSize = sorted_arrayTubos[i][2]
    
print(sorted_tubesInRange)

with open('agrupamento_de_tubos.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in sorted_arrayTubos:
        nZ_arrayTubos_row =  [value for value in row if value != 0]
        writer.writerow(nZ_arrayTubos_row)

