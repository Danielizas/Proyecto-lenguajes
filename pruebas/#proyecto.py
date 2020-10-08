import CargarArchivo
import msvcrt 
import csv  

Cargar = []
listado = []
medio = []
todo = []
ruta = []
estacion = []
Color = []
estado = []
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
    print(" ")


def Cargar_Archivo():
   global Cargar
   global listado
   global medio
   global todo
   global ruta 
   global estacion
   global Color 
   global estado 

   datos= input('Escriba el nombre del archivo: ')
   Archivo = open(datos,"r", encoding='UTF-8')
   linea = Archivo.read()
   Archivo.close()
     
   for i in linea:  
       #linea = i.lstrip("<>")
       y = i.split('<')
       x = i.split('>')
       
   print (linea)
        
       

   

def Graficar_Ruta():
    print("Graficar Ruta")

def Graficar_Mapa():
    print ("Graficar Mapa")    

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
