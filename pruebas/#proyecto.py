import CargarArchivo
import msvcrt 
import csv  
import Analisis

Cargar = []
listado = []
medio = []
todo = []
ruta = []
estacion = []
Color = []
estado = []
peso[]
def MENU():
    menuprincipal = """
    1. Cargar Archivo
    2. Graficar Ruta
    3. Graficar Mapa
    4. Salir """
    print(menuprincipal)

def Info():
    print(" Lenguajes Formales de programacion\n Daniel Izas 201801105")

def Sintaxis():
    #def Analisis():



def Cargar_Archivo():
   global cargar
    global listado
    global inter 
    global todos
    global ruta
    global peso
    global estacion
    global nombre
    global fin
    global inicio
    global color
    global estado 
    global estacion

   datos= input('Escriba el nombre del archivo: ')
   Archivo = open(datos,"r", encoding='UTF-8')
   linea = Archivo.read()
   Archivo.close()
     
   for i in linea:  
       #linea = i.lstrip("<>")
       linea = i.split('<')
       linea = i.split('>')

    ruta=4
    nombre=4
    peso=4
    inicio=4
    fin=4
    color=4
    estacion=4  
    estado=4
    
    while ruta!=13:
        inter.append(cosas[ruta])
        ruta=ruta+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4],inter))
    
    while nombre!=11:
        inter.append(cosas[nombre])
        nombre=nombre+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4].split(','),inter))
    
    while peso!=11:
        inter.append(cosas[peso])
        peso=peso+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4],inter))
    
    while inicio!=11:
        inter.append(cosas[inicio])
        inicio=inicio+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4],inter))
    
    while fin!=11:
        inter.append(cosas[fin])
        fin=fin+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4],inter))

    while color!=11:
        inter.append(cosas[color])
        color=color+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4],inter))

    while estacion!=11:
        inter.append(cosas[estacion])
        estacion=estacion+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4],inter))

    while estado!=11:
        inter.append(cosas[estado])
        estado=estado+1
    todos.append(archivos(cosas[0],cosas[1].split('<'),cosas[2].split('>'),cosas[3],cosas[4],inter))
       
   print ("Archivo cargado exitosamente ")
        
       

def Graficar_Ruta():
    print("Graficar Ruta")

def Graficar_Mapa():
    with open('Archivo_Prueba.txt', 's') as f:
        try:
            f.write("digraph proyecto{\n")
            f.write('rankdir=LR;\n')
            f.write("node [shape = record, style=filled]\n;")
            for course in listado:
                color = "black"
                if int(course.est) == 0:
                    color = "blue"
                if int(course.est) == 1:
                    color = "green"
                f.write(f"{course.cod} [label = \"{course.nom}\", fillcolor={color}];\n")
            for course in listado:
                if len(course.pre) == 1 and course.pre[0] != "":
                    f.write(f"{str(course.pre[0])} -> {course.cod};\n")
                elif len(course.pre) > 1:
                    for prerequisito in course.pre:
                        f.write(f"{prerequisito} -> {course.cod};\n")
            f.write('}')
        finally:
            f.close()
            os.system('txt -Tpng proyecto.dot -o proyecto.svs -Gcharset=latin1')
    print("     Mapa generado!      ")
    print("=========================================")

def Salir():
    while True:
        print("Lenguajes Formales y de Programación ")
        print("Presionar Enter para continuar")
        print("")
        n = str(msvcrt.getch(),'utf-8')
        if n == "\r":
            return False

Info()
m = 0
while m == 0:
	MENU()
	c = int(input('Selecione una opcion: '))
	if 1 == c:
			Cargar_Archivo()
	if 2 == c:
			Graficar_Ruta()
	if 3 == c:
			Graficar_Mapa
	if 4 == c:
		Salir()
		m=1 
