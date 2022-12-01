import io
import csv

def get_words(lista):
    ini = 0
    out = True
    conjunto = set()
    
    # element contienen varios generos separados por comas, busco rescatar cada elemento de forma independiente, de momento medianamente he tenido exito.
    # Por algun motivo sigue buscando la "," rebasando el tamaño de element en la lista: Pendiente resolver esto. 
    
    for element in lista:
        palabra = element.replace(" ","") #eliminar espacios vacios
        while out == True:
            try:
                fin = element.index(",") + ini
            except ValueError:
                fin = len(element)
                out = False
                
            palabra = element[ini:fin]
            ini = fin
            conjunto.add(palabra)
            print(palabra)
        out = True

def run():
    conjunto = []
    ini = 0
    fin = 0
    
    lista = ["Adventure, Comedy, Family","Action, Biography, Crime","Animation, Adventure, Drama","Biography, Crime, Drama"]
    get_words(lista)

            


if __name__ == '__main__':
    run()