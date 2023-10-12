# função para realizar a operação da frase dita pelo usuário
def operacao(frasedita):
    import math as mt
    # lista que contém os dois números ditos pelo usuário
    num = []
    
    for item in frasedita.split():
        
        # tratamento para números reais
        if '.' in item:
            
            # soma
            if '+' in frasedita.split() or 'mais' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return num[0] + num[1]
            
            # subtração
            elif '-' in frasedita.split() or 'menos' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return num[0] - num[1]

            # multiplicação
            elif 'x' in frasedita.split() or 'vezes' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return num[0] * num[1]
            
            # divisão
            elif '/' in frasedita.split() or 'barra' in frasedita.split() or 'dividido' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return num[0] / num[1]
            
            # potenciação
            elif '^' in frasedita.split() or 'elevado' in frasedita.split() or 'potência' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return pow(num[0], num[1])
            
            # número ao quadrado
            elif 'ao' in frasedita.split() and 'quadrado' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return num[0] ** 2
            
            # número ao cubo
            elif 'ao' in frasedita.split() and 'cubo' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return num[0] ** 3

            # raiz quadrada
            elif 'raiz' in frasedita.split() and 'quadrada' in frasedita.split():
                for item in frasedita.split():
                    if '.' in item:
                        num.append(float(item))
                return mt.sqrt(num[0])

        # tratamento para números inteiros
        else:
            # soma
            if '+' in frasedita.split() or 'mais' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return num[0] + num[1]
            
            # subtração
            elif '-' in frasedita.split() or 'menos' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return num[0] - num[1]

            # multiplicação
            elif 'x' in frasedita.split() or 'vezes' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return num[0] * num[1]
            
            # divisão
            elif '/' in frasedita.split() or 'barra' in frasedita.split() or 'dividido' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return num[0] / num[1]
            
            # potenciação
            elif '^' in frasedita.split() or 'elevado' in frasedita.split() or 'potência' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return pow(num[0], num[1])
            
            # número ao quadrado
            elif 'ao' in frasedita.split() and 'quadrado' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return num[0] ** 2
            
            # número ao cubo
            elif 'ao' in frasedita.split() and 'cubo' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return num[0] ** 3

            # raiz quadrada
            elif 'raiz' in frasedita.split() and 'quadrada' in frasedita.split():
                for item in frasedita.split():
                    if item.isnumeric():
                        num.append(int(item))
                return mt.sqrt(num[0])

    resultado = num.copy()
    return resultado

#função para ouvir e reconhecer a fala
def ouvir_microfone():
    import speech_recognition as sr
    import gtts as gt
    from playsound import playsound   
    # ligando o mic do usuário
    microfone = sr.Recognizer()
    
    # usando o mic
    with sr.Microphone() as source:
        
        # redução de ruído
        microfone.adjust_for_ambient_noise(source)

        #  comando pro usuário falar alguma coisa
        print("Fale dois números e a operação que deseja realizar com eles: ")
        
        fala = gt.gTTS("Fale dois números e a operação que deseja realizar com eles: ", lang='pt-br')
        fala.save('fala.mp3')
        playsound('fala.mp3')
        
        # armazenando oq foi dito numa variável
        audio = microfone.listen(source)

    try:
        # passando oq foi dito para o algoritmo reconhecedor de padrões e salvando-o em um arquivo de texto
        frase = microfone.recognize_google(audio, language = 'pt-BR')
        with open('frase.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write("Você disse: " + frase)

        # retorno da frase pronunciada em áudio
        arquivo = open('frase.txt', 'r', encoding='utf-8')
        for linha in arquivo:
            frase_dita = gt.gTTS(linha, lang= 'pt-br')
            frase_dita.save('frase.mp3')
        playsound('frase.mp3')
        
        print("Você disse: ", frase)
        
        # retorno do resultado da operação que o usuário deseja
        resultado = operacao(frase)
        print("O resultado da operação é", resultado)

        num_op = gt.gTTS("O resultado da operação é" + str(resultado), lang='pt-br')
        num_op.save('resul.mp3')
        playsound('resul.mp3')

        
    
    # caso houver algum erro no reconhecimento
    except sr.UnknownValueError:
        print("Erro de compreensão.")
        
        fala_erro = gt.gTTS("Erro de compreensão.", lang='pt-br')

        fala_erro.save('fala_erro.mp3')

        playsound('fala_erro.mp3')

        return 

ouvir_microfone()