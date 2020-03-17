tempo_volta = {
    "Piloto1": [57, 58, 60, 56, 64, 70, 59, 58, 69, 55],
    "Piloto2": [56, 60, 72, 50, 67, 58, 61, 63, 62, 59],
    "Piloto3": [79, 52, 58, 48, 58, 59, 61, 65, 59, 60],
    "Piloto4": [56, 50, 55, 70, 85, 73, 68, 65, 56, 60],
    "Piloto5": [69, 55, 67, 50, 52, 53, 70, 75, 65, 56],
    "Piloto6": [56, 63, 63, 65, 70, 59, 55, 60, 63, 62]
}

volta=0
medias = tempo_volta
nome = ""
melhor_volta = tempo_volta["Piloto1"][0]
for chave in tempo_volta:
    soma = 0
    
    for num in tempo_volta[chave]:
        
        if num < melhor_volta:
            melhor_volta = num
            nome = chave
            volta+=1
        soma += num
        
    medias[chave] = soma / 10
    
print("A melhor volta da prova e do piloto "+str(nome)+" com o tempo de "+str(melhor_volta)+" segundos na volta "+str(volta+1))
print()
i=0
for item in sorted(medias, key = medias.get):
    i+=1
    print ("O "+str(i)+"º lugar e do piloto "+str(item)+" com a média de tempo de "+str(medias[item]))