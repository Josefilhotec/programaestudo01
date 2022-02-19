# Programa ler o nome, idade e sexo de 4 pessoas.
# no final do programa mostra:
# A média de idade do grupo.
# O nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.
pessoa = 0
soma = 0
media_idade = 0
lista = []
homem_mais_velho = ''
contador = 0
for pessoa in range(1, 5):
    print('----- Dados da {}° pessoa -----'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    soma += idade
    media_idade = soma / pessoa
    if sexo in 'Mn':
        lista.append(idade)
        homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        contador += 1
print('A media de idade das {} pessoas é de {} anos.'.format(pessoa, int(media_idade)))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(max(lista), homem_mais_velho))
print('No grupo tem {} mulheres menor de 20 anos.'.format(contador))
