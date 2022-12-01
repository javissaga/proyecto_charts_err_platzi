# 1.Cantidad de peliculas por año dentro del top 1000 de IMDB.
# 2. Al seleccionar un genero, ¿Cuantas peliculas se hicieron de ese genero por año?  ---proximamente.
# 3. Peliculas que superan los 90 minutos promedio. ----proximamente.

def group_years(years,account):  #hacer grupos de 10 años
  decade = []
  amount = []
  counter = -1
  
  for i in range(len(years)):#creacion de grupos de 10 años
    if int(years[i]) % 10 == 0:
      counter += 1
      decade.append(years[i])#creacion de grupos
      amount.append(int(account[i]))
    else:
      amount[counter] = amount[counter] + int(account[i])
  return decade,amount


def how_many_movies(data): #¿cuantas peliculas se han producido en intervalos de 10?
  preliminar = []
  account = []

  for movie in data:  #sacar toda la columna de años
    preliminar.append(movie['Released_Year'])

  conjunto = set(preliminar)  #valores unicos: años
  year_label = list(conjunto)
  year_label.sort()
    
  for element in year_label:  #eliminar valores que no corresponden con la fecha
    try:
      int(element)
      account.append(preliminar.count(element))  #contar cuantos elementos existen en la lista con respecto de 'element'
    except ValueError:
      year_label.remove(element)
    except TypeError:
      year_label.remove(element)

  year_label,account = group_years(year_label,account) # funcion de agrupamiento de años
  iterable = zip(year_label,account)  #uso de iterable y zip para union de elementos relacionados
  years_movies = {key: value for key, value in iterable}  #de iterable a dict comprenhesion
  
  return years_movies.keys(), years_movies.values()


def genre_and_year(data):
  preliminar = []
  conjunto = set()
  account = []
  
  print(type(conjunto))
  for movie in data:  #sacar toda la columna de genero
    preliminar.append(movie['Genre'])
  
  for element in preliminar:
    print(element)
      #conjunto.add(row)
  
  #print(conjunto)
  
  
  #what_genre = input()



def up_to_media(data):
  print("Proximamente...en su localidad")