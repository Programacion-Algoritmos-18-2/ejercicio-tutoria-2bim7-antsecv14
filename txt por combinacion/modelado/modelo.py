import codecs
#class Persona
class Persona(object):
	#constructor de la clase
	def __init__(self, nombre, apellido, edad):
		#atributos
		self.nombre = nombre
		self.apellido = apellido
		self.edad = int(edad)
#metodos agregar y obtener
	def agregar_nombre(self,nombre):
		self.nombre = nombre

	def agregar_apellido(self,apellido):
		self.apellido = apellido

	def agregar_edad(self, edad):
		self.edad = int(edad)

	def obtener_nombre(self):
		return self.nombre

	def obtener_apellido(self):
		return self.apellido

	def obtener_edad(self):
		return self.edad
#Sobrescritura de metodos str y repr
	def __str__(self):
		return "%s %s %d" %(self.nombre, self.apellido, self.edad)

	def __repr__(self):
		return "%s %s %d" %(self.nombre, self.apellido, self.edad)


#Class MiArchivo
class MiArchivo:
#constructor de la clase
    def __init__(self):
        self.archivo = codecs.open("data/archivo-datos-combinacion.txt", "r")#abre el Archivo
#metodo que obtiene la informacion del archivo
    def obtener_informacion(self):
        return self.archivo.readlines()
#metodo que cierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()