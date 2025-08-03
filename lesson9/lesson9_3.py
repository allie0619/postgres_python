#請幫我自訂一個function
#連線至postgres DB
#建立連線環境參數的樣版


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
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")
if __name__ == "__main__":
    main()
