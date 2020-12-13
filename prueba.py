import db

con = db.conectar()
if con!=None:
    datos = ('prueba@uninorte.edu.co','claveprueba','A')
    res = db.ejecutar_query(con,'''INSERT INTO usuarios(email,clave,estado) VALUES(?,?,?)''',datos)
    res = db.ejecutar_select(con, "SELECT codigo, email, clave, estado FROM usuarios")
    #res = db.ejecutar_select(con, "SELECT codigo FROM accesorios")
    if res!=None:
        for fila in res:
            print(fila)
    else:
        print("No se seleccionó ningún registro")
    db.desconectar(con)    
else:
    print('Error al conectarse a la base de datos')