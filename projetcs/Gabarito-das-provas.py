# Tupla = uma "lista" com valores imutáveis
gabarito = ('A', 'A', 'B', 'D', 'E', 'A', 'C', 'C', 'A', 'D')

alternativas = ('A', 'B', 'C', 'D', 'E')

# Quantidade de respostas desejada 
quantidade_respostas = len(gabarito)

# Lista vazia para armazenar as respostas
respostas = []

print('Responda as questões a seguir com alternativas de "A" até "E"')
# Solicitação das respostas
for i in range(quantidade_respostas):
    while True:
        resposta = input(f"Insira a resposta da questão {i + 1}: ")
        resposta = resposta.upper()
    
        if resposta in alternativas:
            break
        else: 
            print(f'Resposta inválida. Insira uma das alternativas: {alternativas}')
# Todos os valores se tornam maiúsculos 
    
    # Append = adiciona o item na lista "respostas"
    respostas.append(resposta)

# Calcula a quantidade de respostas corretas
resposta_certa = 0    
for i in range(len(gabarito)):
    if respostas[i] == gabarito[i]:
        resposta_certa += 1 

# Imprime a lista de respostas e a quantidade de respostas corretas
print(f'Suas respostas:\n{respostas}')
print(f'Nota Final: {resposta_certa}')
