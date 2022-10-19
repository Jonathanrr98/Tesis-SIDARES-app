from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
from textblob import TextBlob
nltk.download('punkt')


def AddlexicalPolisemicalAmbiguety(text):
    t = TextBlob(text)
    raiz = PorterStemmer()
    stemers = []
    lexicals = []

    for setence in t.sentences:
        words = word_tokenize(setence.string)

        for x in words:
            stemers.append(raiz.stem(x))
        for y in stemers:
            z = stemers.count(y)

            if z > 1:
                lexicals.append(
                    "posible ambiguedad léxica cerca de " + "(" + y + ")")
    return lexicals


from textblob import TextBlob
import deepl
import nltk
from nltk.corpus import stopwords
import pandas as pd


translator = deepl.Translator("YOUR_AUTH_KEY")
	

result = translator.translate_text("hola, mundo!", target_lang="EN-US")

print(result) # “Hallo, Welt!”


text = "el carro verde y la sombrilla amarilla esta al lado de la casa del perro"

# tokenizado = nltk.word_tokenize(text)

blob = TextBlob(text)

texto = blob.translate(to='en')

print(texto)
# print(nltk.pos_tag(tokenizadoEs))

df_ambi = pd.read_csv('requierements_by_centers.csv', encoding = 'unicode_escape')

print(df_ambi)




import os
current_directory = os.getcwd()
print(current_directory) 
import numpy as np

dates = pd.date_range("20130101", periods=6)

print (dates)


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)
