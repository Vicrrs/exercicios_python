def db_operation(func):
    def(**args, **kwargs):
        conn = get_postgres_connect()
        cursor = connection.cursor()
        try:
            result = func(cursor, *args, **kwargs)
            connection.commit()
            return result
        except psycopg2.DatabaseError as e:
            connection.rollback()
            loggin.error("Database operation failed: %s", str(e))
            raise
        finally:
            cursor.close()
            connection.close()
    return wrapper

@db_operation
def insert_data(cursor, table, data, returning_column='id'):
    columns = ', '.join(data.keys())
    values_placeholder = ', '.join(['%s'] * len(data))
    sql = f"INSERT INTO (table) ((columns)) VALUES ((values_placeholder)) RETURNING (returning_column)"
    cursor.execute(sql, list(data.values()))
    return cursor.fetchone()[0]

# Example usage
insert_result = insert_data("your_table", {"column1": "value1", "column2": "value2"})



