import mysql.connector
from mysql.connector import Error
 
def get_tables():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='receta',
            user='root',
            password='root'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            
            print("\n=== Tablas en la base de datos 'receta' ===")
            print("----------------------------------------")
            for table in tables:
                print(f"► {table[0]}")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    get_tables()