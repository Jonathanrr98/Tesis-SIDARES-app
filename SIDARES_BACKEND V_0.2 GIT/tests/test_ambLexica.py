# from django.test import TestCase
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize
# import nltk
# from textblob import TextBlob
# import numpy as np






# ListaPalabrasAmbiguas = [
#     # Palabras que denotan posibilidad
#     ' en caso contrario ',
#     ' no específico ',
#     ' puede ser ',
#     ' podría ser ',
#     ' es uno de ',
#     ' debe ser ',
#     ' deberá ser ',
#     ' debería ser ',
#     ' será ',

#     # Verbos ambiguos
#     ' ajustar ',
#     ' alterar ',
#     ' corregir ',
#     ' calcular ',
#     ' cambiar ',
#     ' comparar ',
#     ' derivar ',
#     ' determinar ',
#     ' habilitar ',
#     ' indicar ',
#     ' igualar ',
#     ' modificar ',
#     ' desempeñar ',
#     ' procesar ',
#     ' apoyar ',
#     ' verificar ',


#     # Variables ambiguas (específicas del proyecto)
#     ' datos ',
#     ' regla ',
#     ' estatus ',
#     ' valor ',

#     # Adjetivos cuantitativos ambiguos.

#     ' todos ',
#     ' cualesquiera ',
#     ' cada ',
#     ' pocos ',
#     ' muchos ',
#     ' mismos ',
#     ' varios ',
#     ' similares ',
#     ' algunos ',
#     ' el completo ',
#     ' el total ',

#     # Adverbios ambiguos

#     ' satisfactoriamente ',
#     ' incondicionalmente ',
#     ' en conformidad ',
#     ' por poco ',
#     ' aproximadamente ',
#     ' por lo general ',
#     ' comúnmente ',
#     ' acostumbradamente ',
#     ' frecuentemente ',
#     ' generalmente ',
#     ' casi nunca ',
#     ' ocasionalmente ',
#     ' a punto de ',
#     ' a menudo ',
#     ' mas o menos ',
#     ' sobre todo ',
#     ' casi ',
#     ' no del todo ',
#     ' seguido ',
#     ' en el raro caso ',
#     ' ordinariamente ',
#     ' raramente ',
#     ' aproximadamente ',
#     ' muy pocas veces ',
#     ' lentamente ',
#     ' algo ',
#     ' típicamente ',
#     ' virtualmente ',


#     # Palabras o frases que denotan algo Implícito


#     ' también ',
#     ' a pesar de ',
#     ' y además ',
#     ' aparte de ',
#     ' pero ',
#     ' aunque ',
#     ' además ',
#     ' además de ',
#     ' eso ',
#     ' ese ',
#     ' asimismo ',
#     ' por otra parte ',
#     ' a pesar de ',
#     ' por otro lado ',
#     ' todavía ',
#     ' lo antedicho ',
#     ' lo anterior ',
#     ' estos ',
#     ' esto ',
#     ' este ',
#     ' aunque ',
#     ' mientras que ',
#     ' aun ',
#     ' aquel ',
#     ' lo previamente mencionado ',


#     # Ambigüedad de tiempo

#     ' después ',
#     ' en un momento dado ',
#     ' en el tiempo apropiado ',
#     ' diariamente ',
#     ' velozmente ',
#     ' en un momento ',
#     ' mas tarde ',
#     ' mensualmente ',
#     ' rápido ',
#     ' pronto ',
#     ' semanalmente ',
#     ' anualmente ',


#     # Palabras que denotan ambigüedad total.
#     ' etcétera ',

# ]






# class LexicalTestClass(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         pass


#     def TestlexicalPolisemicalAmbiguety(self,text):
    
#         text="El sistema debe mostrar junto al plan de trabajo del usuario seleccionado los datos personales del mismo."
#         lexicals = []


#         for x in ListaPalabrasAmbiguas:
#             if x in text:
#                 lexicals.append(
#                 "Ambiguedad lexica detectada en la cadena" + " " + "( " + x + " )")
        


#         self.assertEqual(lexicals)




# import unittest
# from selenium import webdriver
 
# class SearchText(unittest.TestCase):
#   def setUp(self):
#     # crea la sesion con firefox
#     self.driver = webdriver.Firefox(executable_path=r'C:\Users\jonat\Desktop\TesisDocumentacion\Requisitos_por_centros\requisitos_por_centro.csv')
#     self.driver.implicitly_wait(30)
#     self.driver.maximize_window()
#     # navega hasta esa url
#     self.driver.get("http://127.0.0.1:8000/filter")        

#   def TestsintacticPolisemicalAmbiguety(self,text):
    
#         text="El sistema debe permitir seleccionar una fecha y una sesión y mostrando el listado de los miembros del proyecto."
#         sintactic = []
#         cont = 0
#         cont2 = 0
#         cont3 = 0

#         c = [' y ',  ' e ' , ' ni ', ' que ']
#         cp = [' o ', ' u ', ' sea ', ' bien ']
#         cps = [' a ', ' con ', ' de ', ' en ' ]

#         for setence in text:
#             words = word_tokenize(setence.string)
#             print(words)
#             for x in words:
#                 if x == ',' or x == ';' or x == '-':
#                     cont = 0
#                     cont2 = 0
#                     cont3 = 0
#                 for y in c:
#                     print(y)
#                     if x == y:
#                         cont = cont + 1
#                     if cont >= 2:
#                         sintactic.append(
#                         'posible ambiguedad sintáctica cerca de ' + "(" + y + ")")

#             for z in cp:
#                 if x == z:
#                     cont2 = cont2 + 1
#                 if cont2 >= 2:
#                     sintactic.append(
#                         'posible ambiguedad sintáctica cerca de ' + "(" + z + ")")

#             for h in cps:
#                 if x == h:
#                     cont3 = cont3 + 1
#                 if cont3 >= 2:
#                     sintactic.append(
#                         'posible ambiguedad sintáctica cerca de ' + "(" + h + ")")
        

#         self.assertEqual(sintactic)  

#   if TestsintacticPolisemicalAmbiguety == '__main__':
#         unittest.main()     