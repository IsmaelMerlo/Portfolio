import os
from flask import Flask, request, render_template
from datetime import date, datetime
import pytz
import locale

# Setting the locale to Spanish
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

# Defining the Flask application
app = Flask(__name__)


def obtener_fecha_actual():
    # Get the current date in the desired time zone
    # Replace 'nombre_de_la_zona_horaria' with the desired time zone
    zona_horaria = pytz.timezone('America/Panama')
    fecha_actual = datetime.now(zona_horaria)
    return fecha_actual.strftime("%d de %B de %Y")


# Saving today's date in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

# If this file doesn't exist, create it
if 'tasks.txt' not in os.listdir('.'):
    with open('tasks.txt', 'w') as f:
        f.write('')


def obtener_lista_de_tareas():
    with open('tasks.txt', 'r') as f:
        lista_de_tareas = f.readlines()
    return lista_de_tareas


def crear_nueva_lista_de_tareas():
    os.remove('tasks.txt')
    with open('tasks.txt', 'w') as f:
        f.write('')


def actualizar_lista_de_tareas(lista_de_tareas):
    os.remove('tasks.txt')
    with open('tasks.txt', 'w') as f:
        f.writelines(lista_de_tareas)

################## FUNCIONES DE RUTEO #########################

# Our main page


# Our main page
@app.route('/')
def inicio():
    return render_template('inicio.html', datetoday2=datetoday2, lista_de_tareas=obtener_lista_de_tareas(), l=len(obtener_lista_de_tareas()))


# Function to clear the task list


@app.route('/clear')
def limpiar_lista():
    crear_nueva_lista_de_tareas()
    return render_template('inicio.html', datetoday2=datetoday2, lista_de_tareas=obtener_lista_de_tareas(), l=len(obtener_lista_de_tareas()))

# Function to add a task to the task list


@app.route('/addtask', methods=['POST'])
def agregar_tarea():
    tarea = request.form.get('newtask')
    with open('tasks.txt', 'a') as f:
        f.writelines(tarea+'\n')
    return render_template('inicio.html', datetoday2=datetoday2, lista_de_tareas=obtener_lista_de_tareas(), l=len(obtener_lista_de_tareas()))

# Function to delete a task from the task list


@app.route('/deltask', methods=['GET'])
def eliminar_tarea():
    indice_tarea = int(request.args.get('deltaskid'))
    lista_de_tareas = obtener_lista_de_tareas()

    if indice_tarea < 0 or indice_tarea >= len(lista_de_tareas):
        return render_template('inicio.html', datetoday2=datetoday2, lista_de_tareas=lista_de_tareas, l=len(lista_de_tareas), mess='Índice inválido...')
    else:
        tarea_eliminada = lista_de_tareas.pop(indice_tarea)

    actualizar_lista_de_tareas(lista_de_tareas)
    return render_template('inicio.html', datetoday2=datetoday2, lista_de_tareas=lista_de_tareas, l=len(lista_de_tareas))


# Our main function that runs the Flask application
if __name__ == '__main__':
    app.run(debug=True)
