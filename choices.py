# 1.Cantidad de peliculas por año dentro del top 1000 de imbd
# 2. Al seleccionar un genero, ¿Cuantas peliculas se hicieron de ese genero por año?
# 3. Peliculas que superan los 90 minutos promedio

def how_many_movies(data):
    preliminar =[]
    year = {}
    account = []
    
    for movie in data: #sacar toda la columna de años
        preliminar.append(movie['Released_Year'])
    
    conjunto = set(preliminar) #valores unicos: años
    year_label = list(conjunto)
    year_label.sort()
    for element in year_label: #eliminar valores que no corresponden con la fecha
        if len(element) != 4:
            year_label.remove(element)
        else:
            account.append(preliminar.count(element))#contar cuantos elementos existen en la lista con respecto de 'element'
            iterable = zip(year_label,account) #uso de iterable y zip para union de elementos relacionados
            years_movies = {key:value for key,value in iterable} #de iterable a dict comprenhesion

    
    return years_movies.keys(),years_movies.values()
    
def genre_and_year(data):
    pass

def up_to_media(data):
    pass


