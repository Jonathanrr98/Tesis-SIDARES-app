
texto = 'el lunes voy a ajustar la vascula, no específico'

encon = texto.find('no específico')

ListaPalabrasAmbiguas = {
    # Palabras que denotan posibilidad
    'en caso contrario',
    'no específico',
    'puede ser',
    'podría ser',
    'es uno de',
    'debe ser',
    'deberá ser',
    'debería ser',
    'será',

    # Verbos ambiguos
    'ajustar',
    'alterar',
    'corregir',
    'calcular',
    'cambiar',
    'comparar',
    'derivar',
    'determinar',
    'habilitar',
    'indicar',
    'igualar',
    'modificar',
    'desempeñar',
    'procesar',
    'apoyar',
    'verificar',


    # Variables ambiguas (específicas del proyecto)
    'datos',
    'regla',
    'estatus',
    'valor',

    # Adjetivos cuantitativos ambiguos.

    'todos',
    'cualesquiera',
    'cada',
    'pocos',
    'muchos',
    'mismos',
    'varios',
    'similares',
    'algunos',
    'el completo',
    'el total',

    # Adverbios ambiguos

    'satisfactoriamente',
    'incondicionalmente',
    'en conformidad',
    'por poco',
    'aproximadamente',
    'por lo general',
    'comúnmente',
    'acostumbradamente',
    'frecuentemente',
    'generalmente',
    'casi nunca',
    'ocasionalmente',
    'a punto de',
    'a menudo',
    'mas o menos',
    'sobre todo',
    'casi',
    'no del todo',
    'seguido',
    'en el raro caso',
    'ordinariamente',
    'raramente',
    'aproximadamente',
    'muy pocas veces',
    'lentamente',
    'algo',
    'típicamente',
    'virtualmente',


    # Palabras o frases que denotan algo Implícito


    'también',
    'a pesar de',
    'y además',
    'aparte de',
    'pero',
    'aunque',
    'además',
    'además de',
    'eso',
    'ese',
    'asimismo',
    'por otra parte',
    'a pesar de',
    'por otro lado',
    'todavía',
    'lo antedicho',
    'lo anterior',
    'estos',
    'esto',
    'este',
    'aunque',
    'mientras que',
    'aun',
    'aquel',
    'lo previamente mencionado',


    # Ambigüedad de tiempo

    'después',
    'en un momento dado',
    'en el tiempo apropiado',
    'diariamente',
    'velozmente',
    'en un momento',
    'mas tarde',
    'mensualmente',
    'rápido',
    'pronto',
    'semanalmente',
    'anualmente',


    # Palabras que denotan ambigüedad total.
    'etcétera'

}




#VARIABLES AMBIGUAS
 # Palabras que denotan posibilidad
amb_1 =     'en caso contrario',
amb_2=     'no específico',
amb_3 =     'puede ser',
amb_4 =     'podría ser',
amb_5 =     'es uno de',
amb_6 =     'debe ser',
amb_7 =     'deberá ser',
amb_8 =     'debería ser',
amb_9 =     'será',

  # Verbos ambiguos
amb_10 =     'ajustar',
amb_11=     'alterar',
amb_12 =     'corregir',
amb_13 =     'calcular',
amb_14=     'cambiar',
amb_15 =     'comparar',
amb_16 =     'derivar',
amb_17 =     'determinar',
amb_18 =     'habilitar',
amb_19 =     'indicar',
amb_20 =     'igualar',
amb_21 =     'modificar',
amb_22 =     'desempeñar',
amb_23 =     'procesar',
amb_24 =     'apoyar',
amb_25 =     'verificar',

 # Variables ambiguas (específicas del proyecto)
amb_26 =     'datos',
amb_27 =     'regla',
amb_28 =     'estatus',
amb_29 =     'valor',


   # Adjetivos cuantitativos ambiguos.

amb_31 =     'todos',
amb_32 =     'cualesquiera',
amb_33 =     'cada',
amb_34 =     'pocos',
amb_35 =     'muchos',
amb_36 =     'mismos',
amb_37 =     'varios',
amb_38 =     'similares',
amb_39 =     'algunos',
amb_40 =     'el completo',
amb_41 =     'el total',


  # Adverbios ambiguos

amb_42 =     'satisfactoriamente',
amb_43 =     'incondicionalmente',
amb_44=     'en conformidad',
amb_45 =     'por poco',
amb_46=     'aproximadamente',
amb_47=     'por lo general',
amb_48=     'comúnmente',
amb_49=     'acostumbradamente',
amb_50=     'frecuentemente',
amb_51=     'generalmente',
amb_52=     'casi nunca',
amb_53=     'ocasionalmente',
amb_54=     'a punto de',
amb_55=     'a menudo',
amb_56=     'mas o menos',
amb_57=     'sobre todo',
amb_58=     'casi',
amb_59=     'no del todo',
amb_60=     'seguido',
amb_61=     'en el raro caso',
amb_62=     'ordinariamente',
amb_63=     'raramente',
amb_64=     'aproximadamente',
amb_65=     'muy pocas veces',
amb_66=     'lentamente',
amb_67=     'algo',
amb_68=     'típicamente',
amb_69=     'virtualmente',


  # Palabras o frases que denotan algo Implícito

amb_70 =     'también',
amb_71 =     'a pesar de',
amb_72 =     'y además',
amb_73 =     'aparte de',
amb_74 =     'pero',
amb_75 =     'aunque',
amb_76 =     'además',
amb_77 =     'además de',
amb_78 =     'eso',
amb_79 =      ' ese ',
amb_80 =     'asimismo',
amb_81 =     'por otra parte',
amb_82 =     'a pesar de',
amb_83 =     'por otro lado',
amb_84 =     'todavía',
amb_85 =       'lo antedicho',
amb_96 =     'lo anterior',
amb_87 =     'estos',
amb_88 =     'esto',
amb_89 =     'este',
amb_90 =     'aunque',
amb_91 =     'mientras que',
amb_92 =     'aun',
amb_93 =     'aquel',
amb_94 =     'lo previamente mencionado',


   # Ambigüedad de tiempo

amb_95 =     'después',
amb_96 =     'en un momento dado',
amb_97 =     'en el tiempo apropiado',
amb_98 =     'diariamente',
amb_99 =     'velozmente',
amb_100 =     'en un momento',
amb_101 =     'mas tarde',
amb_102 =     'mensualmente',
amb_103 =     'rápido',
amb_104 =     'pronto',
amb_105 =     'semanalmente',
amb_106 =     'anualmente',


    # Palabras que denotan ambigüedad total.
amb_107 = 'etcétera'

# import re

# text = "hola a todos y toda con ese ritmo"
# for x in ListaPalabrasAmbiguas:
#     resultado = re.search(x,text)


#     print(resultado.start())
#     print(resultado.end())

# for x in ListaPalabrasAmbiguas:
#     if "datos" in x:
#         print(x)


# print([x for x in  ListaPalabrasAmbiguas if 'datos' in x])