import mysql.connector

def crear_base_datos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_contraseña"
    )
    cursor = conexion.cursor()

    with open("PandaTaT.sql", "r") as archivo_sql:
        sql_script = archivo_sql.read()

    for sentencia in sql_script.split(';'):
        if sentencia.strip():
            cursor.execute(sentencia)

    conexion.commit()
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    crear_base_datos()
