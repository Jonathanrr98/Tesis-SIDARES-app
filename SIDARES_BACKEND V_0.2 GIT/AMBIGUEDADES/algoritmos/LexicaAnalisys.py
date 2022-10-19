import numpy as np
# nltk.download('punkt')

ListaPalabrasAmbiguas = [
    # Palabras que denotan posibilidad
    ' en caso contrario ',
    ' no específico ',
    ' puede ser ',
    ' podría ser ',
    ' es uno de ',
    ' debe ser ',
    ' deberá ser ',
    ' debería ser ',
    ' será ',

    # Verbos ambiguos
    ' ajustar ',
    ' alterar ',
    ' corregir ',
    ' calcular ',
    ' cambiar ',
    ' comparar ',
    ' derivar ',
    ' determinar ',
    ' habilitar ',
    ' indicar ',
    ' igualar ',
    ' modificar ',
    ' desempeñar ',
    ' procesar ',
    ' apoyar ',
    ' verificar ',


    # Variables ambiguas (específicas del proyecto)
    ' datos ',
    ' regla ',
    ' estatus ',
    ' valor ',

    # Adjetivos cuantitativos ambiguos.

    ' todos ',
    ' cualesquiera ',
    ' cada ',
    ' pocos ',
    ' muchos ',
    ' mismos ',
    ' varios ',
    ' similares ',
    ' algunos ',
    ' el completo ',
    ' el total ',

    # Adverbios ambiguos

    ' satisfactoriamente ',
    ' incondicionalmente ',
    ' en conformidad ',
    ' por poco ',
    ' aproximadamente ',
    ' por lo general ',
    ' comúnmente ',
    ' acostumbradamente ',
    ' frecuentemente ',
    ' generalmente ',
    ' casi nunca ',
    ' ocasionalmente ',
    ' a punto de ',
    ' a menudo ',
    ' mas o menos ',
    ' sobre todo ',
    ' casi ',
    ' no del todo ',
    ' seguido ',
    ' en el raro caso ',
    ' ordinariamente ',
    ' raramente ',
    ' aproximadamente ',
    ' muy pocas veces ',
    ' lentamente ',
    ' algo ',
    ' típicamente ',
    ' virtualmente ',


    # Palabras o frases que denotan algo Implícito


    ' también ',
    ' a pesar de ',
    ' y además ',
    ' aparte de ',
    ' pero ',
    ' aunque ',
    ' además ',
    ' además de ',
    ' eso ',
    ' ese ',
    ' asimismo ',
    ' por otra parte ',
    ' a pesar de ',
    ' por otro lado ',
    ' todavía ',
    ' lo antedicho ',
    ' lo anterior ',
    ' estos ',
    ' esto ',
    ' este ',
    ' aunque ',
    ' mientras que ',
    ' aun ',
    ' aquel ',
    ' lo previamente mencionado ',


    # Ambigüedad de tiempo

    ' después ',
    ' en un momento dado ',
    ' en el tiempo apropiado ',
    ' diariamente ',
    ' velozmente ',
    ' en un momento ',
    ' mas tarde ',
    ' mensualmente ',
    ' rápido ',
    ' pronto ',
    ' semanalmente ',
    ' anualmente ',


    # Palabras que denotan ambigüedad total.
    ' etcétera ',

]

def AddlexicalPolisemicalAmbiguety(text):
    lexicals = []
    for x in ListaPalabrasAmbiguas:
        if x in text:
            lexicals.append(
                "Ambiguedad léxica detectada en la cadena" + " " + "( " + x + " )")
    return np.unique(lexicals) 


