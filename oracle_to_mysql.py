import cx_Oracle
import mysql.connector

# Oracle конфигурација
oracle_config = {
    'user': 'ORACLE_USER',
    'password': 'ORACLE_PASS',
    'dsn': 'ORACLE_SID'
}

# MySQL конфигурација
mysql_config = {
    'host': 'MYSQL_HOST',
    'database': 'MYSQL_DB',
    'user': 'MYSQL_USER',
    'password': 'MYSQL_PASS'
}

try:
    # Кonekции
    oracle_conn = cx_Oracle.connect(**oracle_config)
    oracle_cur = oracle_conn.cursor()
    oracle_cur.execute("SELECT * FROM your_table")
    rows = oracle_cur.fetchall()

    mysql_conn = mysql.connector.connect(**mysql_config)
    mysql_cur = mysql_conn.cursor()

    # Пример: пренесување на податоци
    for row in rows:
        mysql_cur.execute(
            "INSERT INTO your_table (col1, col2) VALUES (%s, %s)",
            (row[0], row[1])
        )
    mysql_conn.commit()

    print("Преносот е успешен.")
except Exception as e:
    print(e)
finally:
    if 'oracle_conn' in globals():
        oracle_conn.close()
    if 'mysql_conn' in globals() and mysql_conn.is_connected():
        mysql_conn.close()
