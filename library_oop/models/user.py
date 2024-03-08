from library_oop.db.database_connection import DatabaseConnection

class UserDB(DatabaseConnection):
    def add_user(self, username, email):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user (username, email) VALUES (%s, %s)",
                (username, email)
            )
        conn.commit()
        print("User added successfully!")
        
    def get_user(self, username):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,)
            )
            user = cursor.fetchone()
            if user:
                return user
            else:
                print("User not found!")
                return None
    
    def update_user_email(self, username, new_email):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET eamil = %s WHERE username = %s",
                (new_email, username)
            )
            conn.commmit()
            print("User email update successfully!")
            
    def delete_user(self, username):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM users WHERE username = %s",
                (username,)
            )
        conn.commit()
        print("User deleted successfully!")
