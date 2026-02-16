continuar = 's'

while continuar == 's':
    
    mensagem_erro = 'ERRO! O valor não pode ser negativo!'
    nome = str(input('Digite seu nome: '))
    salario_atual = float(input('Digite seu salario atual: '))
  
    if salario_atual <= 0:
        print(mensagem_erro)
    else:
        aumento = int(input('Digite a porcentagem do seu aumento: '))
        
        if aumento < 0:
            print(mensagem_erro)
        else:
            valor_aumento = (aumento/100) * salario_atual
            salario_novo = salario_atual + valor_aumento

            print('\nAUMENTO SALARIAL\n')
            print(f'Funcionario: {nome.title()}')
            print(f'Salário atual: R${salario_atual:.2f}')
            print(f'Aumento: {aumento}%')
            print(f'Salário com aumento: R${salario_novo:.2f}')
           
    continuar = input('\nDeseja calcular novamente? Digite s(sim) ou n(não): ').lower()