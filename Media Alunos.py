from colorama import init, Fore, Style

init()

qtd_alunos = int(input("Digite a quantidade de alunos: "))

for num_alunos in range(qtd_alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    
    for num_notas in range(4):
        nota = float(input(f"Digite a nota {num_notas + 1} do aluno {nome}: "))
        notas.append(nota)
    
    soma = sum(notas)
    media = soma / len(notas)
    
    print(f"Nome do Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Media final: {media:.2f}")
    
    if media >= 7:
        print(f'Você esta {Fore.GREEN}{Style.BRIGHT}APROVADO!!!{Style.RESET_ALL}')
        print("PARABENS!!!")
    elif media >= 5:
        print(f'Você está de {Fore.YELLOW}{Style.BRIGHT}RECUPERAÇÃO!!{Style.RESET_ALL}')
        print('ESTUDE MAIS!!!') 
    else:
        print(f'Você está {Fore.RED}{Style.BRIGHT}REPROVADO!!!{Style.RESET_ALL}')
        print('SINTO MUITO!!!')   
    
    

print("=" * 30)
print(f'{Fore.BLUE}PROGRAMA ENCERRADO!!!{Style.RESET_ALL}')