
import mariadb
import sys


try:
    conn = mariadb.connect(
        user="root",
        password="password",
        host="localhost",
        port=3306,
        database="employees"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()