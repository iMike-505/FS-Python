#Declaramos la variable
calificacion = input("Introduce tu calificación de la AZ-900: ")
calificacion =int(calificacion)

#Preguntamos si la calificacion es menor a 700
if calificacion < 700 :
    print("Reprobado!!") #Si es menor a 700, muestra eso
elif calificacion > 1000:
    print("Mentira!!!")
else :
    print("Aprovado!!!")

#Verificador de mayoria de edad
edad = input("Introduce tu edad ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Welcome!!")
elif edad > 100 : 
    print("WTF!!!")
elif edad < 0 :
    print("Viajero del tiempo")
else : 
    print("Acceso denegado")


#EN PYTHON NO HAY SWITCH - CASE :c