import psycopg2

class DatabaseConnection:
    def __init__(self, dbname, user, password):
        self._dbname = dbname
        self._user = user
        self._password = password
        self._conn = None
        
    def connect(self):
        if self._conn is None:
            try:
                self_conn = psycopg2.connect(
                    dbname = self._dbname,
                    user = self._user,
                    password = self._password
                )
            except Exception as e:
                print(f"An error occurred: {e}")
        return self_conn
    
    def disconnect(self):
        if self._conn is not None:
            self._conn.close()
