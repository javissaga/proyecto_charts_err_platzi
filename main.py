import reading
import choices
import deploy_chart
import os

def show_graphic(labels, values, x,y):
    
    print("**************************************************")
    try:
        grafico = int(input("Tipo de Gŕafico\n1. Gráfico de barras \n2. Gráfico pie\n"))
    except:
        print("Ingrese solo numeros")
    
    if grafico == 1:
        deploy_chart.generate_bar_chart(labels,values,y,x)
    elif grafico == 2:
        deploy_chart.generate_pie_chart(labels,values,y,x)
    else:
        print("Su elección no es válida")

def run():
    os.system('clear')
    print("*******************************IMBD*******************************")
    print("Grafico de acuerdo a las siguientes opciones\n")
    print("1. Cantidad de peliculas en grupos de 10 años dentro del top 1000 de IMDB" )
    print("2. Cuantas peliculas estan en el top por genero")
    print("3. Cuantas peliculas superan los 90 minutos de tiempo promedio")
    
    try:
        eleccion = int(input("¿Que información deseas conocer? "))
    except ValueError:
        print("Solo Numeros")
        eleccion = 50
    
    if eleccion < 4 and eleccion >0:
        data = reading.read_file('movies.csv')
        
        if eleccion == 1:
            os.system("clear")
            labels, values = choices.how_many_movies(data)
            show_graphic(labels,values,"Peliculas producidas","Años")
                
        elif eleccion == 2:
            os.system("clear")
            choices.genre_and_year(data)
            #labels, values = choices.genre_and_year(data)
            #show_graphic(labels,values,"   ","   ")
            
        else:
            labels, values = choices.up_to_media(data)    
            show_graphic(labels,values,"   ","   ")
    else:
        print("¿No tienes curiosidad? Bueno, me retiro")


if __name__ == '__main__':
    run()