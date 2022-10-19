from nltk.tokenize import word_tokenize
import re
import numpy as np
from googletrans import Translator
from textblob import TextBlob
from textblob.taggers import NLTKTagger
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')


def SyntacticAnalissys(text):

    text_one_delimiter1 = text.replace("; ", ", ")
    text_one_delimiter2 = text_one_delimiter1.replace(". ", ", ")
    text_one_delimiter3 = text_one_delimiter2.replace(": ", ", ")

    textoSeparado = re.split(', ', text_one_delimiter3)

    tokeni = word_tokenize(textoSeparado[0])
    # tokeni devuelve una lista de las palabras de cada requisito

    sintactic = []

    c = [' y ',  ' e ', ' ni ', ' que ']
    cp = [' o ', ' u ', ' sea ', ' bien ']
    cps = [' a ', ' con ', ' de ', ' en ']

    listas = []
    listascp = []
    listascps = []

    # busca mas de una aparicion ce
    for x in c:
        for match in re.findall(x, textoSeparado[0]):
            listas.append(format(match))

        yes = listas.count(' y ')
        if yes > 1:
            sintactic.append(
                'posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( y ) ')
            yes = 0

        ques = listas.count(' que ')
        if ques > 1:
            sintactic.append(
                'posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( que ) ')
            ques = 0

        nis = listas.count(' ni ')
        if nis > 1:
            sintactic.append(
                'posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( ni ) ')
            nis = 0

        es = listas.count(' e ')
        if es > 1:
            sintactic.append(
                'posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( e ) ')
            es = 0

    for b in cp:
        for match in re.findall(b, textoSeparado[0]):
            listascp.append(format(match))

    oses = listascp.count(' o ')
    if oses > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( o ) ')
        oses = 0

    ues = listascp.count(' u ')
    if ues > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( u ) ')
        ues = 0

    seas = listascp.count(' sea ')
    if seas > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( sea ) ')
        seas = 0

    bienes = listascp.count(' bien ')
    if bienes > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una conjunción ( bien ) ')
        bienes = 0

    # busca mas de una aparicion ce CPS

    for d in cps:
        for match in re.findall(d, textoSeparado[0]):
            # print('Found {!r}'.format(match))
            listascps.append(format(match))

    aes = listascp.count(' a ')
    if aes > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una preposición ( a ) ')
        aes = 0

    cones = listascp.count(' con ')
    if cones > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una preposición ( con ) ')
        cones = 0

    dees = listascp.count(' de ')
    if dees > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una preposición ( de ) ')
        dees = 0

    enes = listascp.count(' en ')
    if enes > 1:
        sintactic.append(
            'Posible ambiguedad sintáctica: El requisito presenta más de una preposición ( en ) ')
        enes = 0

    return np.unique(sintactic)

    #######################################################################################################
    ############################ + 2da regla de ambiguedades sintácticas + ################################
    #######################################################################################################


def SyntacticAnalissys2(text):

    sintactyc2 = []

    # se define el conjunto de palabras a aliminar
    stop_words = set(stopwords.words('ambiguedad'))

    # se tokeniza el requisito
    word_tokens = nltk.word_tokenize(text)

    requisitosLimpios = " ".join(word_tokens)

    # se filtra el requisito
    filtered_sentence = [w for w in requisitosLimpios if not w in stop_words]

    filtered_sentence = []

    # se añaden las palabras ya filtradas a una lista
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(filtered_sentence)


# TRADUCCIÓN Y TAG

    nltk_tagger = NLTKTagger()
    translator = Translator()

    result = translator.translate(text, dest="en")

    print(result.text)

    blob = TextBlob(result.text, pos_tagger=nltk_tagger)
    blob.pos_tags

    listaDeTags = []

    for x in blob.tags:
        listaDeTags.append(x[1])

    print(listaDeTags)

    listaABuscar1 = ['JJ', 'NNS', 'CC', 'NNS']
    listaABuscar2 = ['JJ', 'NN', 'CC', 'NN']
    listaABuscar3 = ['JJ', 'NNS', 'CC', 'NN']
    listaABuscar4 = ['JJ', 'NN', 'CC', 'NNS']

    listaABuscar5 = ['NNS', 'CC', 'NNS', 'JJ']
    listaABuscar6 = ['NN', 'CC', 'NN', 'JJ']
    listaABuscar7 = ['NNS', 'CC', 'NN', 'JJ']
    listaABuscar8 = ['NN', 'CC', 'NNS', 'JJ']

    strListaABuscar1 = str(listaABuscar1).strip("[]")
    strListaABuscar2 = str(listaABuscar2).strip("[]")
    strListaABuscar3 = str(listaABuscar3).strip("[]")
    strListaABuscar4 = str(listaABuscar4).strip("[]")

    strListaABuscar5 = str(listaABuscar5).strip("[]")
    strListaABuscar6 = str(listaABuscar6).strip("[]")
    strListaABuscar7 = str(listaABuscar7).strip("[]")
    strListaABuscar8 = str(listaABuscar8).strip("[]")

    strListaTag = str(listaDeTags).strip("[]")

    if strListaABuscar1 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')
    if strListaABuscar2 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')
    if strListaABuscar3 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')
    if strListaABuscar4 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')

    if strListaABuscar5 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')
    if strListaABuscar6 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')
    if strListaABuscar7 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')
    if strListaABuscar8 in strListaTag:
        sintactyc2.append(
            'Posiblemente existe un adjetivo que no especifica al sustantivo o sustantivos a los que modifica')

    return (sintactyc2)
