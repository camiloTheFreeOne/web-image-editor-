from conexionbd import conexionMysql

class modelUsuarios:
    def __init__(self):
        self.mibasededatos = conexionMysql()
        self.conexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor
    
    def obtener_conexion(self):
        return self.mibasededatos
    
    def obtener_usuario(self, id):
        self.cursor.execute("SELECT * FROM usuarios WHERE user_id = %s", (id,))
        return self.cursor.fetchone()
    
    def obtener_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
     
    def insertar_usuario(self, user_name, user_email, user_password):
        val = (user_name, user_email, user_password)
        sql = "INSERT INTO usuarios (user_name, user_email, user_password) VALUES(%s, %s, %s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()

    def actualizar_usuario(self, user_id, user_name, user_email, user_password):
            val= (user_name, user_email, user_email, user_password, user_id)
            sql= "UPDATE usuarios SET user_name= %s, user_email= %s, user_password= %s WHERE user_id= %s"
            self.cursor.execute(sql, val)
            self.conexion.commit()

    def eliminar_usuarios(self, user_id):
            val = (user_id,)
            sql = "DELETE FROM usuarios WHERE user_id = %s"
            self.cursor.execute(sql, val)
            self.conexion.commit()
            
    def cerar_conexion(self):
         self.cursor.close()
         self.conexion.close()

    def verificar_usuario(self, email, password):
         val = (email, password)
         sql = "SELECT email, clave FROM usuarios WHERE user_email = %s AND user_password = %s"
         self.cursor.execute(sql, val)
         user =  self.cursor.fetchone()
         if  user:
              return "index"
         else:
              return "contraseña incorrecta" 