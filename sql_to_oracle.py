import mysql.connector
import cx_Oracle

# MySQL конфигурација
mysql_config = {
    'host': 'MYSQL_HOST',
    'database': 'MYSQL_DB',
    'user': 'MYSQL_USER',
    'password': 'MYSQL_PASS'
}

# Oracle конфигурација
oracle_config = {
    'user': 'ORACLE_USER',
    'password': 'ORACLE_PASS',
    'dsn': 'ORACLE_SID'
}

try:
    # Кonekции
    mysql_conn = mysql.connector.connect(**mysql_config)
    oracle_conn = cx_Oracle.connect(**oracle_config)

    # Читање од MySQL
    mysql_cur = mysql_conn.cursor(dictionary=True)
    mysql_cur.execute("SELECT * FROM your_table")
    rows = mysql_cur.fetchall()

    # Пишување во Oracle
    oracle_cur = oracle_conn.cursor()
    for row in rows:
        oracle_cur.execute(
            "INSERT INTO your_table(col1, col2) VALUES(:1, :2)",
            (row['col1'], row['col2'])
        )
    oracle_conn.commit()

    print("Преносот е успешен.")
except Exception as e:
    print(e)
finally:
    if 'mysql_conn' in globals() and mysql_conn.is_connected():
        mysql_conn.close()
    if 'oracle_conn' in globals():
        oracle_conn.close()
