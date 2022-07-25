#Nathan Raul Chavez Alvarez
import mysql.connector

conexion1 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pedidos"
    )
cursor1 = conexion1.cursor()
# cursor1.execute("show tables")
# for dato in cursor1:
#      print(dato)

##crear tablas
#sql = """CREATE TABLE clientes_minoristas (nombre VARCHAR(255), direccion VARCHAR(255))"""
#sql = """CREATE TABLE administradores (nombre VARCHAR(255), puesto VARCHAR(255))"""

##añadir valores a una tabla
# sql = """INSERT INTO clientes_minoristas (nombre, direccion) VALUES (%s, %s)"""
# valores = [
#       ("Alejandro_Alvarez", "Villa_Fatima"),
#       ("Miguel_Choque", "Villa_Adela"),
#       ("Tania_Zambrana", "Miraflores"),
#       ("Carlos_Camacho", "San_Antonio"),
#       ("Damaris_Garcia", "Obrajes"),
#       ("Roberto_Chavez", "Viacha" )
#   ]
# cursor1.executemany(sql, valores)
# print(cursor1.rowcount, "registros insertados")

##borrar algun valor de una tabla
# sql = """DELETE FROM clientes_minoristas WHERE direccion = "Viacha" """
# cursor1.execute(sql)
# sql = """SELECT * FROM clientes_minoristas"""
# cursor1.execute(sql)
# for dato in cursor1:
#        print(dato)

##mostrar los valores aumentados en la tabla
# sql = """SELECT * FROM clientes_minoristas"""
# cursor1.execute(sql)
# clientes = cursor1.fetchall()
# for cliente in clientes:
#        print(cliente)

##consultas
#sql = """SELECT * FROM empleados WHERE empleadoid = 2 """
# sql = """SELECT * FROM empleados WHERE nombre = "MARIA" """
# cursor1.execute(sql)
# for dato in cursor1:
#         print(dato)

##actualizar datos, UPDATE
sql = """UPDATE clientes SET NOMBRECONTACTO = "PEDRO" WHERE DIRECCIONCLI = "EL PINAR" """
cursor1.execute(sql)
sql = """SELECT * FROM clientes """
cursor1.execute(sql)
for dato in cursor1:
     print(dato)





conexion1.close()




