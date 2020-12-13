import sqlite3


def conectar():
    try:
        sal = sqlite3.connect('C:\\Users\\DEICY\\Desktop\\inventario') 
    except:
        sal = None
    return sal  

def desconectar(con):
    try:
        con.close()
    finally:
        con = None
    return con

def ejecutar_consulta_sel(con,sql):
    try:
        cur = con.cursor()                  # Crea un cursor (un lugar para almacenar los resultados de la consulta)
        sal = cur.execute(sql)
        if sal!=None:
            sal = sal.fetchall()            # Recupera todos los resultados de la consulta (recordset - resultset)
    except:
        sal = None
    return sal

def ejecutar_consulta_acc(con,sql,datos):
    try:
        cur = con.cursor()                  # Crea un cursor (un lugar para almacenar los resultados de la consulta)
        sal = cur.execute(sql,datos)
        con.commit()
    except:
        sal = 0
    return sal