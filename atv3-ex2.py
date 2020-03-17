lista = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

listatimes = {'Brasil': 0, 'Italia': 0, 'Espanha': 0}

total_faltas = 0

for i in lista:
    total_faltas += sum(i[2])
    listatimes[i[0]] += i[2][0]
    listatimes[i[1]] += i[2][1]
    
print(listatimes)
    
time_mais_falta = max(listatimes)
time_menos_falta = min(listatimes)

print("Total de faltas do campeonato: ", total_faltas)
print("O time que mais fez falta: ", time_mais_falta)
print("O time que menos fez falta: ", time_menos_falta)