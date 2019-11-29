import re #libreria de expresiones regulares

path = "codigo.java"

try:
    archivo = open(path, "r")
except:
    print ("El archivo que intentas abrir no existe")
    quit()

texto = ""

for linea in archivo:
    texto += linea

print (texto)

patron = re.compile('[a-zA-Z][\w\d]*')#VARIABLES VALIDAS
result1 = re.findall(patron, texto)
print("\n 1 - VARIABLES VALIDAS")
#print ("\n", result1)


for i in result1:
    if (i!="if" and i!="public" and i!="class" and i!="static" and i!="void" and i!="main" and i!="String" and i!="args" and i!="Scanner" and i!="teclado" and i!="nextInt" and i!="System" and i!="nextInt" and i!="out" and i!="println" and i!="else" and i!="print" and i!="new" and i!="int" and i!="in" and i!="Introduce" and i!="No" and i!="Son" and i!="iguales" and i!="otro" and i!="numero" and i!="un" and i!="son"):
        print("Validos: " + i)

patron = r"\d*\.?\d+" #NUMEROS DECIMALES
result = re.findall(patron, texto)
print("\n 2 - NUMEROS DECIMALES")
print ("\n", result)
print("\n")


patron = r"\*\*|--|\+\+|\+=|-=|/=|\%|\+|-|\*|/" #OPERADORES ARITMETICOS
result = re.findall(patron, texto)
print("\n 3 - OPERADORES ARITMETICOS")
print ("\n", result)
print("\n") 


patron = r"<|\d<=|>|\d>=|==|!="#OPERADORES_RELACIONALES
result = re.findall(patron, texto)
print("\n 4 - OPERADORES RELACIONALES")
print ("\n", result)
print("\n")

patron = r"\bint|\babstract|\bassert|\bboolean|\bbreak|\bbyte|\bcase|\bcatch|\bchar|\bclass|\bconst|\bcontinue|\bdefault|\bdo|\bdouble|\belse|\benum|\bextends|\bfinal|\bfinally|\bfloat|\bfor|\bgoto|\bif|\bimplements|\bimport|\binstanceof|\binterface|\blong|\bnative|\bnew|\bpackage|\bprivate|\bprotected|\bpublic|\breturn|\bshort|\bstatic|\bstrictfp|\bsuper|\bswitch|\bsynchronized|\bthis|\bthrow|\bthrows|\btransient|\btry|\bvoid|\bvolatile|\bwhile" #PALABRAS_RESERVADAS
result = re.findall(patron, texto)
print("\n 5 - PALABRAS RESERVADAS")
print ("\n", result)
print("\n")