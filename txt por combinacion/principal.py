#importacion de clases
from modelado.modelo import *
from modelado.combinacion import *
#declaracion de objeto tipo Miarchivo
m = MiArchivo()

lista = m.obtener_informacion()#lista que obtiene la ing¿formacion del archivo

lista = [l.split(";") for l in lista]

lista2 = []

lista_edad = []
#for para recorrrer la lista
for d in lista:

	p = Persona(d[0],d[1],d[2])
	lista2.append(p)#se añade los objetos a una nueva lista
#lista para recorrrer el objeto
for d in lista2:
	lista_edad.append(d.obtener_edad())#se añade la edad en una nueva lista

operacion = merge_sort(lista_edad)#creacion de objeto se llama almetodo merge_sort

#se imprimen las listas
print(lista2)

print(lista_edad)

print(operacion)