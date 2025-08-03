import psycopg2

#請幫我建立一個function
#傳入connection參數
#建立一個cursor
#執行SQL查詢
#並回傳查詢結果
def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"An error occurred while executing the query: {e}")
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed.")

def create_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        port="5432",
        dbname="postgres",
        user="postgres",
        password="raspberry"
    )
    return conn

def main():
    try:
        conn = create_connection()
        print("Connection to the database established successfully.")
        
        # Example query
        query = """SELECT COUNT(*) AS "筆數" "
        "FROM " 台鐵車站資訊";"""
        results = execute_query(conn, query)
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")
    main()