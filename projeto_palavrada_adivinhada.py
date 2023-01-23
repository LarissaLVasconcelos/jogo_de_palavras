import os

palavra_adivinhada = 'alexa'
numero_de_tentativas = 0
letra_acertada = ''

while True:

    letra_digitada = input('Digite uma letra: ')
    numero_de_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra ou caractere.')
        continue

    if letra_digitada in palavra_adivinhada:
        letra_acertada += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_adivinhada:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra adivinhada:', palavra_formada)

    if palavra_formada == palavra_adivinhada:
        os.system('cls')
        print('Parabéns! Você acertou a palavra.')
        print('A palavra é: ', palavra_adivinhada)
        print('Número de tentivas :', numero_de_tentativas)
        numero_de_tentativas = 0
        letra_acertada = ''