import csv



def read_file(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',') # lee el archivo y se guarda en objeto 'reader'
        
        header = next(reader)  #metodo iterable, guarda el primer elemento y avanza
        
        data = [] #lista vacia donde terminaran los datos
        for row in reader: 
            iterable = zip(header,row) #se empareja 'header' con la informacion de 'row'
            
            dic = {key:value for key,value in iterable} #dict comprenhension: zip a dic 
            data.append(dic)
        return data
        
        
        
        