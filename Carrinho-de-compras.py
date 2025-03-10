frutas_mercado = ['Banana', 'Maçã', 'Uva', 'Pera', 'Laranja', 'Melancia']
quantidade = {}

while True:
    fruta_desejada = input('Qual fruta você quer?').capitalize()
    if fruta_desejada in frutas_mercado:
     print(f'Temos {fruta_desejada} disponível.')
     quantas = int(input(f'Diga a quantidade de {fruta_desejada}s que deseja: '))
     quantidade[fruta_desejada] = quantas
     print(f'Mais {quantas} {fruta_desejada}s adicionadas ao carrinho') 
    else: 
     print(f'Não temos {fruta_desejada} no momento.')

    adicionar = input('Mais alguma fruta? (Sim/Não)')
    if adicionar.lower() != 'sim':
        break

print('Carrinho de compras:')
for fruta, quantas in quantidade.items():
    print(f'{quantas} {fruta}s')
