import mysql.connector


class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_los_de_mary")
        return connection

    def insert_db(self, usuario, contraseña, direccion, telefono, rtn, cuenta_bancaria):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_empleados(USUARIO, CONTRASEÑA, DIRECCION, TELEFONO, RTN, CUENTA_BANCARIA) VALUES (%s,%s,%s,%s,%s,%s)"

        data = (usuario, contraseña, direccion, telefono, rtn, cuenta_bancaria)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

    


    
