from unittest import result


def fritar_batata(estado_batata):
    print('Fritando a batata - Sistema simples')
    print('Instruções para você fritar a batata')
    print('1. Pegue uma batata e a corte em palitos finos')
    print('2. Coloque óleo em uma panela e deixe o óleo esquentar no fogão')
    print('3. Ápos o óleo esquenter leve as batatas em palitos finos ate a panela e coloque ela lá')
    print('4. Deixe as batatas fritarem até ficarem douradas')
    print('5. Retire as batatas e coloque em um prato/pote com um papal toalha no fundo para tirar o excesso de óleo')
    print('6. Adicione sal e prove elas, quando achar salgado sulficiente as coma')

    if estado_batata() == 'Crocante ao ponto!':
        resultado =  'Batata recém fritada ao ponto, crocante por fora e macia por dentro.'
    elif estado_batata() == 'fria':
        resultado = 'Batata Frita a algum tempo, esfriou e perdeu o ponto'
    else:
        resultado = 'Batata queimada!'

    return resultado

    decisao =  input(" Você vai fritar a batata agora? ")
    