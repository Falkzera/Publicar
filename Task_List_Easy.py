import os

lista = []

while True:
    
    pergunta = input('Escolha uma opção: \n' '[S]air [A]dicionar [R]emover [L]istar : ').strip().lower()

    if pergunta.startswith('a'):
        adicionar = input('Valor: ')
        lista.append(adicionar)
        os.system('cls')
        print(f'{adicionar} foi adicionado.')

    elif pergunta.startswith('r'):
        try:
            for indice, nome in enumerate(lista):             
                print(indice, nome) 
            remover = int(input('Digite o indice que deseja remover?: '))      
            removido = lista.pop(remover)
            os.system('cls')
            print(f'{removido} foi removido')
        except: 
            os.system('cls')
            print('Valor digitado não contém na lista.')

    elif pergunta.startswith('l'):       
        if len(lista) != 0:
            os.system('cls')  
            for indice, nome in enumerate(lista):           
                print(indice, nome)
        else:
            print('Lista Vazia. ')
   
    elif pergunta.startswith('s'):
        os.system('cls')
        sair = input('Tem certeza que deseja sair? s/n ').strip().lower()
        if sair.startswith('s'):
            break
        else:
            continue
    else:
        os.system('cls')
        print('Opção inválida.')  