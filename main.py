import reading
import choices
import deploy_chart


def run():
    print("*******************************IMBD*******************************")
    print("Grafico de acuerdo a las siguientes opciones\n")
    print("1. Cantidad de peliculas en grupos de 10 años dentro del top 1000 de IMDB" )
    print("2. Cuantas peliculas estan en el top por genero")
    print("3. Cuantas peliculas superan los 90 minutos de tiempo promedio")
    
    eleccion = int(input("¿Que grafico deseas generar? "))
    
    if eleccion < 4 and eleccion >0:
        data = reading.read_file('movies.csv')
        if eleccion == 1:
          labels, values = choices.how_many_movies(data)
          deploy_chart.generate_bar_chart(labels,values,"Peliculas producidas","Años")
        elif eleccion == 2:
            choices.genre_and_year(data)
        else:
            choices.up_to_media(data)    
    else:
        print("¿No tienes curiosidad? Bueno, me retiro")


if __name__ == '__main__':
    run()