import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

try:
    conn = pymysql.connect(

        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASS"),
        database=os.environ.get("MYSQL_DB"),
        port=3306,
       
    )
    print("✅ Connection successful!")
    conn.close()

except pymysql.MySQLError as e:
    print(" Connection failed errror")

