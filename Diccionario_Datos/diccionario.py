print (" ") #Esta linea define el espacio para el nombre
print ("Cristian David Salas De La O 3-W ") #Esta linea muestra el nombre del programador 
print (" ") #Esta linea define el espacio para el nombre 
nombre = input("Ingrese su nombre: ") #Esta linea solicita el nombre 
edad = input("Ingrese su edad: ") #Esta linea solicita la edad
direccion = input("Ingrese su direccion: ") #Esta linea solicita su direccion
telefono = input("Ingrese su número de teléfono: ") #Esta linea solicita el telefono

informacion_usuario = {  #Esta linea define la funcion 
    "nombre": nombre,  #Esta linea define el nombre
    "edad": edad,  #Esta linea define la edad
    "direccion": direccion,  #Esta linea define la direccion 
    "telefono": telefono #Esta linea el telofono
} #Esta linea concluye 

print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']} años,") #Esta linea nmuestra los datos
print(f"vive en {informacion_usuario['direccion']} y su numero de teléfono es {informacion_usuario['telefono']}.") #Esta linea muestra los datos 
