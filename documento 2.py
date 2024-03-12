import pymysql

nombre=str()
edad=int()
nacionalidad=str()
destino=str()
actividad=str()
#---entrada de datos
nombre=str(input('ingrese el nombre: '))
edad=int(input('ingrese edad : '))
nacionalidad=str(input('ingrese la nacionalidad : '))
destino=str(input('ingrese el destino turistico : '))
aventura=str(input('ingrese el tipo de actividad que desea realizar : '))
#----procesos logico para guardad en la base de datos 
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='aventura')
	print('Conexion satifactoria a su base de datos ')
	try:
		with conexion.cursor() as cursor:
			consulta = "INSERT INTO tipo(nombre, edad, nacionalidad, destino, actividad) VALUES (%s, %s, %s, %s, %s);"
			cursor.execute(consulta, (nombre, edad, nacionalidad, destino, actividad))
		conexion.commit()
		print('Registro guardado satisfactoriamente en su base de datos ')
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
