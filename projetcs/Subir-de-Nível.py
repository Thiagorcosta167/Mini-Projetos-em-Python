import time    #para usar o time.sleep, e ter uma demora entre o retorno
from random import randint    #para importar números aleatórios


nivel_atual = 0 
nivel_final = int(input('Selecione uma dificuldade de 1 a 5')) 


print(f'Você está no nível {nivel_atual}')
while nivel_atual < nivel_final: 
    
    #inserir após o while, para mudar a cada loop
    if nivel_final <= 2:
        num1, num2 = randint(1, 10), randint(1, 10)
    elif nivel_final <= 4:
        num1, num2 = randint(3, 10), randint(3, 10)
    else:
        num1, num2 = randint(5, 15), randint(5, 15)
    num_final = num1 * num2 
    
    time.sleep(0.8)
    passar_nivel = input(f'Deseja subir de nível? (Sim/Não)')
    time.sleep(0.8)
    
    if passar_nivel.lower() == 'sim':
        tentativa = int(input(f"Para Passar de nível, resolva a equação: Quanto é {num1} x {num2}?"))
        
        if tentativa == num_final:
            nivel_atual += 1
            time.sleep(0.8)
            print(f'Parabéns! Você agora está no nível {nivel_atual}.')
        
        else:
            time.sleep(0.8)
            print('Não foi dessa vez...')
    
    else: 
        time.sleep(0.8)
        print(f'Continua no nível {nivel_atual}')
time.sleep(0.8)        
print(f'Você chegou ao nível final!({nivel_final}).\nPara ir para o próximo Minigame, acesse o próximo arquivo!')
        
        
    
