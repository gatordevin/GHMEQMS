import psycopg2

try:
    conn = psycopg2.connect(
        dbname="eqms",
        user="eqms_user",
        password="yourpassword",
        host="localhost",
        port="5432"
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
