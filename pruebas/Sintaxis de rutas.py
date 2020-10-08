class rutas:
    global ruta 
    global nombre
    global peso 
    global inicio
    global fin

todo = []
cargar = "Ruta"

datos = input('Nombre del archivo para agregar')
archivo = open(datos, "r", encoding='UTF-8')
lineas = archivo.read()
archivo.close()

for i in lineas:
    iz = i.split('<')
    der = z.split('>')

for a in c:
    if cargar == a:
        todo.append(clase(ruta,nombre, peso, inicio, fin ))     


        