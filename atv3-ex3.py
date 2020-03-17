def notas():
    
    alunos={}

    while True:

        nome = input('Nome do aluno: ')

        if nome=='':
            print("Terminou")
            break

        nota1 = float(input('Nota do aluno: '))
        nota2 = float(input('Nota do aluno: '))

        alunos[nome]=[nota1,nota2] 
     
    while True:

        nome = input('Nome do aluno: ')
        
        if nome=='':
            print("Terminou")
            break
        
        aluno = alunos[nome]
        
        media=(aluno[0]+aluno[1])/2
            
        print(media)
            
notas()