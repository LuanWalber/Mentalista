import random
import time
import os

# Mostrar titulo #
def titulo():
    print('\n##########################')
    print('\t O MENTALISTA')
    print('##########################')

# Gerador de números aleatorios #
def gerador_numerico():
    numero_gerado = random.randrange(1, 101)
    return numero_gerado

    # Função principal #
def mentalista(numero, tentativa):
            while True:
                try:
                    chute = int(input('\nChute o número que estou pensando entre 1 e 100.\nResposta: '))
                    if chute > 100 or chute < 1:
                     time.sleep(1)
                     print('\nApenas um número entre 1 e 100, tente de novo.')
                    elif chute > numero:
                     time.sleep(1)
                     print(f'\nO número que pensei é menor que {chute}, tente de novo.')
                     tentativa += 1
                     time.sleep(1)
                    elif chute < numero:
                     time.sleep(1)
                     print('\nO número que pensei é maior que {chute}, tente de novo.')
                     tentativa += 1
                     time.sleep(1)
                    elif chute == numero:
                     time.sleep(1)
                     print(f'\nPARABÉNS, você acertou com {tentativa} tentativas!\n')
                     time.sleep(1)
                     opcao=input('Deseja jogar novamente? (s/n: ')
                    if opcao.lower() == 's':
                        print('\nReiniciando o jogo... Aguarde!')
                        time.sleep(3)
                        numero = gerador_numerico()
                        tentativa = 0
                        os.system('cls')
                        titulo()
                        continue
                    elif opcao.lower() == 'n' or 'não':
                        time.sleep(1)
                        print('\nOk, estarei sempre aqui.')
                        break
                except ValueError:
                     print("\nDigite um número inteiro!")
                     time.sleep(1)


titulo()
input('Digite ENTER para iniciar o game...')
numero = gerador_numerico()
tentativas = 0
chute = 0
mentalista(numero, tentativas)