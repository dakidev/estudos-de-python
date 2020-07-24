'''
Criando um diálogo bugadasso entre dois personagens
1. Renan
2. Você
'''

#Apresentações

nome = input('Olá! Eu sou Renan, qual o seu nome? ')
gosto = input('Legal! Você gosta de música? \n'
              'Digite 1 para; Sim \n'
              'Digite 2 para; Não \n')

#Início da Conversa

if gosto == '1':
    genero = input('Hmm. De que tipo de gênero você gosta? \n'
                   'Digite 1 para: Rock \n'
                   'Digite 2 para: Pop \n'
                   'Digite 3 para: MPB \n')
    if genero == '1':
        print('Eu... Preciso te contar a verdade... \n'
              'Essa é a minha verdadeira face! \n'
              '░░░░░░▄▄▄░░▄██▄░░░ \n'
              '░░░░░▐▀█▀▌░░░░▀█▄░░░ \n'
              '░░░░░▐█▄█▌░░░░░░▀█▄░░ \n'
              '░░░░░░▀▄▀░░░▄▄▄▄▄▀▀░░ \n'
              '░░░░▄▄▄██▀▀▀▀░░░░░░░ \n'
              '░░░█▀▄▄▄█░▀▀░░ \n'
              '░░░▌░▄▄▄▐▌▀▀▀░░ \n'
              '▄░▐░░░▄▄░█░▀▀ ░░ \n'
              '▀█▌░░░▄░▀█▀░▀ ░ \n'
              '░░░░░░░▄▄▐▌▄▄░░░ \n'
              '░░░░░░░▀███▀█░▄░░\n'
              '░░░░░░▐▌▀▄▀▄▀▐▄░░\n'
              '░░░░░░▐▀░░░░░░▐▌░░ \n'
              '░░░░░░█░░░░░░░░█░░░░░░░ \n'
              '░░░░░░█░░░░░░░░█░░░░░░░ \n'
              '░░░░░░█░░░░░░░░█░░░░░░░░░ \n'
              '░░░░ ▄██▄░░░░░ ▄██▄░░░░░░░')

    elif genero == '2':
            print('Hmmm. Não conheço muitas músicas do gênero Pop. \n'
                  'Quer saber? Sai daqui! TE ODEIOOO!!!!')
            print('VOCÊ FALHOU')

    elif genero == '3':
            print('Eu gostei de você, vamos ser amigos!')
else:
    print('Você é um otário! Quer saber? Sai daqui! TE ODEIOOO!!!!')
