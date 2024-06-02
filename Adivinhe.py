import random
import sys
import time

input('Bem vindo ao jogo de adivinhação, este jogo é simples.\n'
      'Neste jogo você precisará adivinhar o número gerado pelo programa, ele te dará algumas dicas.\n'
      'Tenha uma boa jogatina, pressione enter para começar!\n')

numero = random.randint(1, 11)

print('O número foi gerado, vamos começar te dar as dicas:\n')

if numero % 2 == 0:
    print('1. O número é par')

    input_message4 = 'Deseja tentar adivinhar? (sim/nao): '
    resposta4 = input(input_message4)
    if resposta4 == 'sim':
        input_message4 = ('Qual número você acredita que é?: ')
        numero_resposta2 = input(input_message4)
        if int(numero_resposta2) == numero:
            print('\nVocê acertou')
            sys.exit()
        else:
            print('\nVocê errou, o correto seria:', numero)
            print('Tenha uma boa sorte na próxima :)')
            sys.exit()
else:
    print('1. O número é impar')

    input_message5 = 'Deseja tentar adivinhar? (sim/nao): '
    resposta5 = input(input_message5)
    if resposta5 == 'sim':
        input_message5 = ('Qual número você acredita que é?: ')
        numero_resposta5 = input(input_message5)
        if int(numero_resposta5) == numero:
            print('\nVocê acertou')
            sys.exit()
        else:
            print('\nVocê errou, o correto seria:', numero)
            print('Tenha uma boa sorte na próxima :)')
            sys.exit()
    elif resposta5 == 'nao':
        print('')


def verificar(numero):
    number = numero - 1
    number2 = numero + 2
    print('2. O número está entre', number, 'e', number2)

    input_message6 = 'Deseja tentar adivinhar? (sim/nao): '
    resposta6 = input(input_message6)
    if resposta6 == 'sim':
        input_message6 = ('Qual número você acredita que é?: ')
        numero_resposta6 = input(input_message6)
        if int(numero_resposta6) == numero:
            print('\nVocê acertou')
            sys.exit()
        else:
            print('\nVocê errou, o correto seria:', numero)
            print('Tenha uma boa sorte na próxima :)')
            sys.exit()
    elif resposta6 == 'nao':
        print("A próxima dica é a última!\n")
        time.sleep(2)

    diferenca = abs(numero - number)
    diferenca2 = abs(numero - number2)

    if diferenca < diferenca2:
        return number
    elif diferenca2 > diferenca:
        return number2

numero_verificar = verificar(numero)
print('3. O mais próximo é: {}'.format(numero_verificar))

input_message6 = 'Agora vamos tentar adivinhar? (sim/nao): '
resposta = input(input_message6)
if resposta == 'sim':
    input_message2 = ('Qual número você acredita que é?: ')
    numero_resposta = input(input_message2)
    if int(numero_resposta) == numero:
        print('\nVocê acertou')
        sys.exit()
    else:
        print('\nVocê errou, o correto seria:', numero)
        print('Tenha uma boa sorte na próxima :)')
        sys.exit()
elif resposta == 'nao':
    input_message2 = ('As dicas acabaram, tente adivinhar: ')
    numero_resposta = input(input_message2)
    if int(numero_resposta) == numero:
        print('\nVocê acertou')
        sys.exit()
    else:
        print('\nVocê errou, o correto seria:', numero)
        print('Tenha uma boa sorte na próxima :)')
        sys.exit()
