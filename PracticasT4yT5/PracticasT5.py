import re #libreria de expresiones regulares

path = "Programa_Ejemplo.java"

try:
    archivo = open(path, "r")
except:
    print ("El archivo que intentas abrir no existe")
    quit()

texto = ""

for linea in archivo:
    texto += linea

#Sentencia de asignación. Ejemplo: suma = 0, factorial = 1, vidas = cont, etc.
patron = r"[a-zA-Z]{1,}[\s\S][=][\s\S]\w*.\;"

#Operaciones aritméticas básicas. Ejemplo: suma = 2.7 + 3, cont = cont + 1, etc. 
#patron1 = r"\d[.]\d+.[+].\d[.]\d+|\d+.[+]\s\d+|\d[.]\d+.[-].\d[.]\d+|\d+.[-]\s\d+|\d[.]\d+.[*].\d[.]\d+|\d+.[*]\s\d+|\d[.]\d+.[\/].\d[.]\d+|\d+.[\/]\s\d+|\d[.]\d+.[%].\d[.]\d+|\d+.[%]\s\d+"
#patron1 = r"\d[.]\d+.[+].\d[.]\d+|\d[.]\d+.[+].\d+|\d+[.]\d+.[+].+\d|\d[.]\d+.[-].\d[.]\d+|\d[.]\d+.[-].\d+|\d+[.]\d+.[-].+\d|\d[.]\d+.[*].\d[.]\d+|\d[.]\d+.[*].\d+|\d+[.]\d+.[*].+\d|\d[.]\d+.[%].\d[.]\d+|\d[.]\d+.[%].\d+|\d+[.]\d+.[%].+\d|\d[.]\d+.[\/].\d[.]\d+|\d[.]\d+.[\/].\d+|\d+[.]\d+.[\/][1].+\d"
patron1 = r"\w.[\=]{1}\w*.\w*.[+|-|*|/]{1}\w*.\w*.\;"


#Expresiones booleanas básicas. Ejemplo: edad >= 5, suma != 0, etc.
#patron2 = r"\w+.[\>=]{2}\s.\w+|\w+.[\>=]{2}\s.\w+|\w+.[\==]{2}\s.\w+|\w+.==\s+|\w+.[\!=]{2}\s.\w+"
patron2 = r"[a-zA-Z]+w*.[==|>=|<=|!=]{2}w*.[a-zA-Z0-9]"

#Formulas más complejas del tipo c = a op ( b op d)
patron3 = r"[a-zA-Z]{1,}[\d|\s]{1,}\=[\s|\w|\d.\d]{1,}[\s|\S][\*|\/|\%|\+|\-][\s|\]\([\w|\d.\d]{1,}[\S|\s][\*|\/|\%|\+|\-][\S|\s][\w|\d.\d]{1,}[ \)|\S\)]\;"

#El encabezado de estructura de control. if, while, for, etc.
patron4 = r"[for|if|while].*[\(]\w.*[\)]{"


result = re.findall(patron, texto)
result1 = re.findall(patron1, texto)
result2 = re.findall(patron2, texto)
result3 = re.findall(patron3, texto)
result4 = re.findall(patron4, texto)
print ("\n Resultado 1 \n\n", result)
print ("\n Resultado 2 \n\n", result1)
print ("\n Resultado 3 \n\n", result2)
print ("\n Resultado 4 \n\n", result3)
print ("\n Resultado 5 \n\n", result4)
