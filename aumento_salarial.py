nome = str(input('Digite seu nome: '))
salario_atual = float(input('Digite seu salario atual: '))
aumento = int(input('Digite a porcentagem do deu aumento: '))
valor_aumento = (aumento/100) * salario_atual
salario_novo = salario_atual + valor_aumento

print('\nAUMENTO SALARIAL\n')
print(f'Funcionario: {nome}')
print(f'Salário: R${salario_atual:.2f}')
print(f'Aumento: {aumento}%')
print(F'Salário com aumento: R${salario_novo:.2f}')