#import mysql.connector
#from mysql.connector import errorcode
#from mysql.connector import Error
import pymysql.cursors



mysql = pymysql.connect(user='root',password='',host='localhost',database="hola")
print("Conexion exitosa");



def crearTabla(mysql):
    #with mysql:
        try:
            cursor=mysql.cursor()
            cursor.execute("DROP TABLE IF EXISTS usuario1")
            cursor.execute("CREATE TABLE usuario1 (Idusuario INT PRIMARY KEY AUTO_INCREMENT, \
                     nombres VARCHAR(25), apellidoPaterno varchar (25),apellidoMaterno varchar (25), user varchar (10), pwd varchar (10))")
            print("La tabla ha sido creada");
        except Error as err:
            print("Something went wrong: {}".format(err))
            #sys.exit(1)
            #mysql.close()
            



def insertarDatos(mysql):
   
    idusuario = int(input("Dame id del usuario:"))
    nombres = str(input("Dame los nombres del usuario:"))
    ap = str(input("Dame los ap  del usuario:"))
    am = str(input("Dame los am del usuario:"))
    user = str(input("Dama el user del usuario:"))
    pwd = str(input("Dame el pwd del usuario:"))
    try:

        cursor=mysql.cursor()
        sql='INSERT INTO usuario1 VALUES("%i", "%s","%s","%s","%s","%s")'%(idusuario,nombres,ap,am,user,pwd)       
        cursor.execute(sql)
        mysql.commit()
        print ("registrado correctamente")
    except Error as err:
        print("Something went wrong: {}".format(err))

 

def eliminarDatos(mysql):
    idEliminado = int(input("Dame id del usuario:"))
   
    #with mysql:
    try:
        cursor=mysql.cursor()
        sql='DELETE FROM usuario1 WHERE idusuario=("%i")'%(idEliminado)
        cursor.execute(sql)
        mysql.commit()
        print ("eliminado correctamente")
    except Error as err:
        print ("error %s" %e )


def actualizaDatos(mysql):
    idActualizado = int(input("Dame id del usuario:"))
    nombres = str(input("Dame los nombres del usuario:"))
    ap = str(input("Dame el apellido paterno del usuario:"))
    am = str(input("Dame el apellido materno del usuario :"))
    user = str(input("Dame el usuario:"))
    pwd = str(input("Dame la contraseña:"))
   
    #with mysql:
    try:
        cursor=mysql.cursor()
        sql= 'update usuario1 set nombres= "%s", apellidoPaterno ="%s", apellidoMaterno ="%s", user= "%s", pwd="%s" where idusuario = "%i"' % (nombres,ap,am,user,pwd,idActualizado)
        cursor.execute(sql)
        mysql.commit()
        print ("ACTUALIZADO correctamente")
    except Error as err:
        print ("error %s" %e )


  

def listarDatos(mysql):
        idlista = int(input("Dame id del usuario:"))
        try:
                cursor=mysql.cursor()
                sql= 'select * from usuario1 Where idusuario="%i"'%(idlista)
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                        print (rows)
        except Error as err:
                print ("error %s" %e )
         
       
crearTabla (mysql)
insertarDatos(mysql)
eliminarDatos(mysql)
actualizaDatos(mysql)
listarDatos(mysql)
            

